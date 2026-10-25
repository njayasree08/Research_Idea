from fastapi import APIRouter, HTTPException
from typing import List
from app.models.schemas import GeneInfo, OffTargetLocus
from app.services.genomic_service import list_all_genes, get_gene_info, get_off_targets_for_gene

router = APIRouter(prefix="/api/genes", tags=["genes"])

@router.get("", response_model=List[GeneInfo])
def get_all_target_genes():
    return list_all_genes()

@router.get("/{symbol}", response_model=GeneInfo)
def get_single_gene(symbol: str):
    info = get_gene_info(symbol)
    if not info:
        raise HTTPException(status_code=404, detail=f"Target gene '{symbol}' not found in CRISPR therapeutic atlas.")
    return info

@router.get("/{symbol}/off-targets", response_model=List[OffTargetLocus])
def get_predicted_off_targets(symbol: str):
    return get_off_targets_for_gene(symbol)
