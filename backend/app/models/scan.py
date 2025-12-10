from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from app.models.base import Base

class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    brand_name = Column(String, nullable=True)
    risk_score = Column(Float)
    risk_level = Column(String)
    
    # Text extracted via OCR
    ocr_text = Column(Text, nullable=True)
    
    # Full JSON blob of the analysis (factors, similar marks, etc.)
    analysis_data = Column(JSONB, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
