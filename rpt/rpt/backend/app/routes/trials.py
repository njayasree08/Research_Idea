from fastapi import APIRouter
from typing import List, Dict, Any
from app.services.trials_data import get_clinical_therapies, get_scoping_review_metrics

router = APIRouter(prefix="/api/trials", tags=["trials"])

@router.get("", response_model=List[Dict[str, Any]])
def get_trials_table():
    return get_clinical_therapies()

@router.get("/scoping-metrics")
def get_prisma_scoping_data():
    return get_scoping_review_metrics()
