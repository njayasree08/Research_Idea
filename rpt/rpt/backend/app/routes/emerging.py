from fastapi import APIRouter
from typing import List, Dict, Any
from app.services.emerging_tech import get_emerging_tech

router = APIRouter(prefix="/api/emerging", tags=["emerging"])

@router.get("", response_model=List[Dict[str, Any]])
def get_technologies():
    return get_emerging_tech()
