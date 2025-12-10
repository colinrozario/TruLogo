from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.core.database import get_db
from app.models.scan import Scan

router = APIRouter()

@router.get("/dashboard/stats")
async def get_dashboard_stats(db: AsyncSession = Depends(get_db)):
    """
    Returns aggregated stats for the dashboard.
    """
    # Count Safe Scans (Low Risk)
    result_safe = await db.execute(select(func.count(Scan.id)).where(Scan.risk_level == 'Low'))
    safe_scans = result_safe.scalar() or 0
    
    # Count Risk Alerts (Medium/High/Critical)
    result_risk = await db.execute(select(func.count(Scan.id)).where(Scan.risk_level != 'Low'))
    risk_alerts = result_risk.scalar() or 0
    
    # Pending Filings - Mock for now or based on some status column if we had one
    pending_filings = 1 # Mock
    
    return {
        "stats": {
            "safeScans": safe_scans,
            "riskAlerts": risk_alerts,
            "pendingFilings": pending_filings
        }
    }

@router.get("/dashboard/recent")
async def get_recent_scans(limit: int = 5, db: AsyncSession = Depends(get_db)):
    """
    Returns recent activity log.
    """
    result = await db.execute(select(Scan).order_by(Scan.created_at.desc()).limit(limit))
    scans = result.scalars().all()
    
    logs = []
    for scan in scans:
        # Determine status color/text
        status = "SAFE"
        color = "text-emerald-400"
        
        if scan.risk_level == "High" or scan.risk_level == "Critical":
            status = "CRITICAL"
            color = "text-red-400"
        elif scan.risk_level == "Medium":
            status = "WARNING"
            color = "text-yellow-400"
            
        logs.append({
            "action": f"Scan: '{scan.brand_name or 'Unknown'}'",
            "date": scan.created_at.strftime("%H:%M") if scan.created_at else "Just now", # formatting relative time in frontend is better but simple for now
            "status": status,
            "color": color
        })
        
    return {
        "recentLogs": logs
    }
