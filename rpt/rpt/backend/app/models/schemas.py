import math
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class TherapyParameters(BaseModel):
    gene_symbol: str = Field(default="BCL11A", description="Target gene symbol")
    cas9_concentration: float = Field(default=2.5, ge=0.1, le=10.0, description="Cas9 concentration in µM")
    mismatch_tolerance: float = Field(default=12.0, ge=0.0, le=50.0, description="Guide mismatch tolerance (%)")
    delivery_system: str = Field(default="LNP", description="LNP, Ex-Vivo Electroporation, AAV, VLP")
    cas9_variant: str = Field(default="SpCas9-HF1", description="Wild-Type SpCas9, SpCas9-HF1, HiFi Cas9, evoCas9")
    target_tissue: str = Field(default="Hematopoietic Stem Cells", description="Target tissue/cell type")

class EthicsInputs(BaseModel):
    consent_score: float = Field(default=85.0, ge=0.0, le=100.0, description="Informed consent rigor (%)")
    equity_score: float = Field(default=70.0, ge=0.0, le=100.0, description="Global access & affordability score (%)")
    tracking_score: float = Field(default=90.0, ge=0.0, le=100.0, description="Long-term registry tracking score (%)")
    is_germline: bool = Field(default=False, description="Whether therapy targets germline (disallowed clinically)")

class SimulationRequest(BaseModel):
    therapy_parameters: TherapyParameters
    ethics_inputs: EthicsInputs
    patient_id: Optional[str] = "PT-8024"
    indication: Optional[str] = "Sickle Cell Disease / Beta-Thalassemia"

class OffTargetLocus(BaseModel):
    chromosome: str
    locus: str
    gene_symbol: str
    sequence: str
    mismatches: int
    pam: str
    cleavage_probability: float
    is_oncogenic_risk: bool
    description: str

class SimulationResult(BaseModel):
    status_verdict: str  # "VIABLE THERAPY", "OPTIMIZING", "CRITICAL RISK"
    verdict_color: str   # "emerald", "amber", "rose"
    verdict_explanation: str
    on_target_efficacy: float
    off_target_risk: float
    delivery_efficiency: float
    ethics_composite_score: float
    regulatory_readiness: str
    
    # Curves for Figures 3, 4, 5
    figure3_curve: List[Dict[str, Any]]  # Efficacy vs Delivery at 3 Cas9 concentrations
    figure4_scatter: List[Dict[str, Any]] # Efficacy vs Off-Target tradeoff colored by status
    figure5_concentration_curve: List[Dict[str, Any]] # Simulated Efficacy & Off-target as Cas9 conc increases
    
    # Genomic Risk Map details
    on_target_locus: Dict[str, Any]
    predicted_off_targets: List[OffTargetLocus]
    chromosome_risk_summary: Dict[str, float]

class GeneInfo(BaseModel):
    symbol: str
    name: str
    chromosome: str
    coordinates: str
    function: str
    gain_or_loss: str
    clinical_indications: List[str]
    representative_therapy: str
    exonic_structure: str
    cleavage_strategy: str
