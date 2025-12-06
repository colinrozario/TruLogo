from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.embedding_service import embedding_service
from app.services.vector_store import vector_store
from app.services.heatmap_service import heatmap_service
from app.services.metadata_service import metadata_service
from app.services.safety_service import safety_service
from app.services.remedy_engine import remedy_engine
from app.services.regeneration_service import regeneration_service
from typing import Optional
import json

router = APIRouter()

@router.post("/analyze/logo")
async def analyze_logo(file: UploadFile = File(...)):
    try:
        content = await file.read()
        
        # 1. Basic AI Analysis (Existing)
        embedding = embedding_service.get_image_embedding(content)
        phash = embedding_service.get_phash(content)
        heatmap_b64 = heatmap_service.generate_heatmap(content)
        results = vector_store.search_image(embedding)
        
        # 2. Metadata Extraction
        metadata = metadata_service.extract_metadata(content, file.filename)
        
        # 3. Safety Checks
        safety_results = safety_service.check_safety(metadata)
        
        # 4. Risk Calculation
        risk_score = 0
        similar_marks = []
        
        if results:
            min_distance = results[0]['score']
            similarity = 1 - (min_distance / 2)
            raw_score = max(0, similarity * 100)
            
            # Stricter Risk Assessment
            if similarity > 0.20:
                 risk_score = 50 + ((similarity - 0.20) / 0.80) * 50
            else:
                 risk_score = raw_score
            
            # Process all results
            for res in results:
                dist = res['score']
                sim = 1 - (dist / 2)
                res['similarity'] = max(0, sim)
                similar_marks.append(res)
        
        # Adjust risk based on safety flags
        if not safety_results['is_safe']:
            risk_score = max(risk_score, 85) # High risk if safety flags are critical

        # 5. Legal Remedy
        remedy = remedy_engine.get_remedy(risk_score, safety_results)

        return {
            "filename": file.filename,
            "risk_score": round(risk_score, 2),
            "phash": phash,
            "heatmap": heatmap_b64,
            "similar_marks": similar_marks,
            "metadata": metadata,
            "safety": safety_results,
            "remedy": remedy
        }
    except Exception as e:
        print(f"Error in analyze_logo: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate/logo")
async def generate_logo(file: UploadFile = File(...), risk_score: float = Form(...)):
    try:
        content = await file.read()
        variants = regeneration_service.generate_alternatives(content, risk_score)
        return {"variants": variants}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze/text")
async def analyze_text(text: str = Form(...)):
    try:
        embedding = embedding_service.get_text_embedding(text)
        results = vector_store.search_text(embedding)
        return {
            "text": text,
            "similar_marks": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
