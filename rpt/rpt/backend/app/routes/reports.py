from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any, Optional
from datetime import datetime

router = APIRouter(prefix="/api/reports", tags=["reports"])

class DossierRequest(BaseModel):
    patient_id: str
    target_gene: str
    indication: str
    simulation_result: Dict[str, Any]
    therapy_parameters: Dict[str, Any]
    ethics_inputs: Dict[str, Any]

@router.post("/generate-dossier")
def generate_clinical_dossier(req: DossierRequest):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    sim = req.simulation_result
    params = req.therapy_parameters
    ethics = req.ethics_inputs
    
    verdict = sim.get("status_verdict", "UNKNOWN")
    efficacy = sim.get("on_target_efficacy", 0)
    risk = sim.get("off_target_risk", 0)
    ethics_score = sim.get("ethics_composite_score", 0)
    
    markdown_content = f"""# CRISPR-Cas9 Translational Decision Dossier
**Generated:** {timestamp}  
**Protocol Ref:** {req.patient_id} | Target: **{req.target_gene}**  
**Indication:** {req.indication}  
**Regulatory Status:** {sim.get("regulatory_readiness", "EVALUATING")}  

---

### Executive Clinical Verdict
- **System Classification:** **{verdict}**
- **Predicted On-Target Efficacy:** **{efficacy}%**
- **Calculated Off-Target Cleavage Risk:** **{risk}%**
- **Ethical & Governance Index:** **{ethics_score} / 100**
- **Delivery Modality:** {params.get("delivery_system", "N/A")} ({sim.get("delivery_efficiency", 0)}% target bioavailability)
- **Enzyme Variant:** {params.get("cas9_variant", "N/A")} (Dose: {params.get("cas9_concentration", 0)} µM)

---

### Quantitative Evaluation Summary
1. **Therapeutic Window Assessment**:
   The modeled regimen delivers an on-target indel efficiency of {efficacy}%. Off-target genomic perturbation is estimated at {risk}%.
   {sim.get("verdict_explanation", "")}

2. **Bioethical & Regulatory Alignment**:
   - Somatic Verification: {"COMPLIANT (Somatic cell editing strictly maintained)" if not ethics.get("is_germline") else "VIOLATION (Germline modification flag detected)"}
   - Informed Consent Rigor: {ethics.get("consent_score", 0)}%
   - Global Equity & Access Score: {ethics.get("equity_score", 0)}%
   - Mandatory 15-Year Registry Tracking: {ethics.get("tracking_score", 0)}%

3. **Genomic Hazard Surveillance**:
   On-target target site locus: {sim.get("on_target_locus", {}).get("coordinates", "N/A")} ({req.target_gene})
   Predicted candidate off-targets evaluated across GRCh38 human genome build. High-fidelity variants suppress cleavage at non-homologous pseudogene loci.

---
*Based on the PRISMA-ScR methodological framework for CRISPR-Cas9 therapeutics in human health.*
"""
    return {
        "status": "success",
        "timestamp": timestamp,
        "dossier_id": f"DOSSIER-{req.patient_id}-{req.target_gene}",
        "markdown": markdown_content,
        "summary": {
            "verdict": verdict,
            "efficacy": efficacy,
            "off_target_risk": risk,
            "ethics_score": ethics_score,
            "regulatory_status": sim.get("regulatory_readiness")
        }
    }
