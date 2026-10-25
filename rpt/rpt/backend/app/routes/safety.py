from fastapi import APIRouter
from typing import List, Dict, Any
from app.services.safety_mitigation import get_safety_barriers

router = APIRouter(prefix="/api/safety", tags=["safety"])

SURVEILLANCE_REGISTRY_METRICS = {
    "registry_name": "International Human Genome Editing Long-Term Surveillance Registry (15-Year Protocol)",
    "enrolled_patients_monitored": 1428,
    "mean_follow_up_months": 38.4,
    "target_indications": ["Sickle Cell Disease", "β-Thalassemia", "ATTR Amyloidosis", "Hereditary Angioedema"],
    "monitored_endpoints": [
        {"metric": "Clonal Hematopoiesis / Dominant Clones", "detected_events": 0, "threshold_status": "NORMAL"},
        {"metric": "Secondary Myelodysplastic Syndromes", "detected_events": 0, "threshold_status": "NORMAL"},
        {"metric": "Persistent Off-Target Translocations", "detected_events": 0, "threshold_status": "NORMAL"},
        {"metric": "Vector Insertional Mutagenesis (AAV/Viral)", "detected_events": 1, "threshold_status": "RESOLVED / MONITORED"},
        {"metric": "Anti-Cas9 Neutralizing T-cell Activation", "detected_events": 14, "threshold_status": "MILD / CONTROLLED"}
    ],
    "regulatory_pause_triggers": [
        "Unexplained hematologic dysplasia persisting >6 months",
        "Confirmed expansion of clone with mutation in cancer-associated gene (TP53, DNMT3A, ASXL1)",
        "Persistent severe acute immune-mediated hepatotoxicity unresponsive to systemic corticosteroids"
    ]
}

@router.get("/barriers", response_model=List[Dict[str, Any]])
def get_safety_matrix():
    return get_safety_barriers()

@router.get("/surveillance-registry")
def get_surveillance_registry():
    return SURVEILLANCE_REGISTRY_METRICS
