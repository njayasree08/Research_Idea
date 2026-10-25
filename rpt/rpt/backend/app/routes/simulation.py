from fastapi import APIRouter, HTTPException
from app.models.schemas import SimulationRequest, SimulationResult
from app.services.simulation_engine import run_simulation

router = APIRouter(prefix="/api/simulation", tags=["simulation"])

PRESETS = {
    "exa_cel": {
        "id": "exa_cel",
        "name": "Exa-cel (Sickle Cell / Thalassemia)",
        "gene_symbol": "BCL11A",
        "cas9_concentration": 2.5,
        "mismatch_tolerance": 10.0,
        "delivery_system": "Ex-Vivo Electroporation",
        "cas9_variant": "SpCas9-HF1",
        "target_tissue": "Hematopoietic Stem Cells",
        "consent_score": 92.0,
        "equity_score": 68.0,
        "tracking_score": 95.0,
        "is_germline": False,
        "indication": "Severe Sickle Cell Disease & Transfusion-Dependent β-Thalassemia"
    },
    "ntla_2001": {
        "id": "ntla_2001",
        "name": "NTLA-2001 (ATTR Amyloidosis)",
        "gene_symbol": "TTR",
        "cas9_concentration": 2.8,
        "mismatch_tolerance": 8.0,
        "delivery_system": "LNP",
        "cas9_variant": "HiFi Cas9",
        "target_tissue": "Hepatocytes / Liver",
        "consent_score": 90.0,
        "equity_score": 75.0,
        "tracking_score": 92.0,
        "is_germline": False,
        "indication": "Hereditary Transthyretin Amyloidosis with Polyneuropathy / Cardiomyopathy"
    },
    "ntla_2002": {
        "id": "ntla_2002",
        "name": "NTLA-2002 (Hereditary Angioedema)",
        "gene_symbol": "KLKB1",
        "cas9_concentration": 2.2,
        "mismatch_tolerance": 9.0,
        "delivery_system": "LNP",
        "cas9_variant": "HiFi Cas9",
        "target_tissue": "Hepatocytes / Liver",
        "consent_score": 88.0,
        "equity_score": 80.0,
        "tracking_score": 90.0,
        "is_germline": False,
        "indication": "Hereditary Angioedema (HAE) Attack Prevention"
    },
    "ctx310": {
        "id": "ctx310",
        "name": "CTX310 (Dyslipidemia & CAD Risk)",
        "gene_symbol": "ANGPTL3",
        "cas9_concentration": 3.0,
        "mismatch_tolerance": 11.0,
        "delivery_system": "LNP",
        "cas9_variant": "SpCas9-HF1",
        "target_tissue": "Hepatocytes / Liver",
        "consent_score": 85.0,
        "equity_score": 82.0,
        "tracking_score": 88.0,
        "is_germline": False,
        "indication": "Severe Hypercholesterolemia & Atherosclerotic Cardiovascular Disease"
    },
    "edit_101": {
        "id": "edit_101",
        "name": "EDIT-101 (Retinal Degeneration LCA10)",
        "gene_symbol": "CEP290",
        "cas9_concentration": 1.8,
        "mismatch_tolerance": 12.0,
        "delivery_system": "AAV",
        "cas9_variant": "Wild-Type SpCas9",
        "target_tissue": "Retinal Pigment Epithelium / Photoreceptors",
        "consent_score": 86.0,
        "equity_score": 60.0,
        "tracking_score": 85.0,
        "is_germline": False,
        "indication": "Leber Congenital Amaurosis 10 (CEP290 intronic c.2991+1655A>G)"
    },
    "ctx130": {
        "id": "ctx130",
        "name": "CTX130 (Allogeneic CAR-T CD70)",
        "gene_symbol": "CD70",
        "cas9_concentration": 3.2,
        "mismatch_tolerance": 14.0,
        "delivery_system": "Ex-Vivo Electroporation",
        "cas9_variant": "SpCas9-HF1",
        "target_tissue": "Hematopoietic Stem Cells / T-cells",
        "consent_score": 84.0,
        "equity_score": 62.0,
        "tracking_score": 86.0,
        "is_germline": False,
        "indication": "Relapsed/Refractory T-cell Lymphoma & Clear Cell Renal Cell Carcinoma"
    }
}

@router.post("/run", response_model=SimulationResult)
def run_clinical_simulation(req: SimulationRequest):
    try:
        return run_simulation(req.therapy_parameters, req.ethics_inputs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Simulation calculation failed: {str(e)}")

@router.get("/presets")
def get_clinical_presets():
    return list(PRESETS.values())
