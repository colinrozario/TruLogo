from app.services.vector_store import vector_store
from app.services.embedding_service import embedding_service
import os

def seed_data():
    print("Seeding dummy data...")
    
    # Dummy text trademarks
    trademarks = ["Starbucks", "Nike", "Apple", "Google", "Microsoft"]
    for tm in trademarks:
        print(f"Processing {tm}...")
        # Add to text index (SBERT)
        text_emb = embedding_service.get_text_embedding(tm)
        vector_store.add_text(tm, text_emb, {"name": tm, "type": "text"})
        
        # Add to image index (CLIP Text) - Zero-Shot Concept Matching
        clip_emb = embedding_service.get_clip_text_embedding(tm)
        vector_store.add_image(tm, clip_emb, {"name": tm, "type": "text_concept"})
        
    # TODO: Add dummy images if available
    
    print("Seeding complete.")

if __name__ == "__main__":
    seed_data()
