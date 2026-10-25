import math
import random
from typing import Dict, Any, List, Tuple
from app.models.schemas import TherapyParameters, EthicsInputs, SimulationResult, OffTargetLocus
from app.services.genomic_service import get_gene_info, get_off_targets_for_gene

DELIVERY_FACTORS = {
    "LNP": {
        "efficiency_baseline": 88.0,
        "liver_affinity": 1.15,
        "hsc_affinity": 0.55,
        "retina_affinity": 0.40,
        "immunogenicity_penalty": 0.05,
        "transient_expression": True
    },
    "Ex-Vivo Electroporation": {
        "efficiency_baseline": 94.0,
        "liver_affinity": 0.0,
        "hsc_affinity": 1.20,
        "retina_affinity": 0.0,
        "immunogenicity_penalty": 0.02,
        "transient_expression": True
    },
    "AAV": {
        "efficiency_baseline": 82.0,
        "liver_affinity": 0.85,
        "hsc_affinity": 0.45,
        "retina_affinity": 1.25,
        "immunogenicity_penalty": 0.25,
        "transient_expression": False  # Sustained expression elevates off-target cuts
    },
    "VLP": {
        "efficiency_baseline": 86.0,
        "liver_affinity": 1.05,
        "hsc_affinity": 0.90,
        "retina_affinity": 0.85,
        "immunogenicity_penalty": 0.04,
        "transient_expression": True
    }
}

CAS9_VARIANTS = {
    "Wild-Type SpCas9": {"fidelity_modifier": 1.0, "on_target_factor": 1.0},
    "SpCas9-HF1": {"fidelity_modifier": 0.28, "on_target_factor": 0.96},
    "HiFi Cas9": {"fidelity_modifier": 0.22, "on_target_factor": 0.98},
    "evoCas9": {"fidelity_modifier": 0.18, "on_target_factor": 0.92}
}

def calculate_efficacy(
    concentration: float,
    delivery_eff: float,
    mismatch_tol: float,
    cas9_variant: str
) -> float:
    """
    On-target efficacy modeled via Hill kinetics coupled to delivery efficiency:
    Efficacy = E_max * (C^n / (C^n + Kd^n)) * (delivery_eff / 100) * (1 - penalty(mismatch))
    """
    variant_data = CAS9_VARIANTS.get(cas9_variant, CAS9_VARIANTS["SpCas9-HF1"])
    n = 1.75
    kd = 1.15
    hill_binding = (concentration ** n) / (concentration ** n + kd ** n)
    
    # Mild penalty if guide is overly promiscuous / mismatched
    mismatch_factor = 1.0 - (0.22 * (mismatch_tol / 50.0))
    raw_efficacy = 96.0 * hill_binding * (delivery_eff / 100.0) * mismatch_factor * variant_data["on_target_factor"]
    return round(min(98.5, max(5.0, raw_efficacy)), 1)

def calculate_off_target_risk(
    concentration: float,
    delivery_eff: float,
    mismatch_tol: float,
    delivery_sys: str,
    cas9_variant: str
) -> float:
    """
    Off-target cleavage risk rises superlinearly with excess Cas9 concentration and mismatch tolerance:
    Risk_off = baseline * (C^1.55) * ((mismatch_tol/10)^1.35) * fidelity_modifier * delivery_durability
    """
    variant_data = CAS9_VARIANTS.get(cas9_variant, CAS9_VARIANTS["SpCas9-HF1"])
    del_data = DELIVERY_FACTORS.get(delivery_sys, DELIVERY_FACTORS["LNP"])
    
    durability_mult = 1.5 if not del_data["transient_expression"] else 0.85
    base_rate = 1.65
    
    # Power curve for concentration and mismatch
    conc_factor = (concentration ** 1.52)
    mismatch_factor = ((mismatch_tol / 10.0) ** 1.38)
    delivery_scaling = (delivery_eff / 100.0) ** 0.8
    
    risk = base_rate * conc_factor * mismatch_factor * delivery_scaling * variant_data["fidelity_modifier"] * durability_mult
    return round(min(95.0, max(0.5, risk)), 1)

def determine_system_verdict(
    efficacy: float,
    off_target_risk: float,
    is_germline: bool,
    ethics_score: float
) -> Tuple[str, str, str]:
    """
    Determines status verdict matching Figure 2 & 4 from the paper:
    'VIABLE THERAPY', 'OPTIMIZING', or 'CRITICAL RISK'
    """
    if is_germline:
        return (
            "CRITICAL RISK / RESTRICTED",
            "rose",
            "GERMLINE MODIFICATION DETECTED: Violates international consensus and Section 5 regulatory governance. Only somatic therapies are clinically permitted."
        )
    
    if off_target_risk >= 38.0 or efficacy < 45.0 or ethics_score < 40.0:
        return (
            "CRITICAL RISK",
            "rose",
            f"High genomic hazard or subtherapeutic editing threshold (Risk: {off_target_risk}%, Efficacy: {efficacy}%). Risk of oncogenic indels and translocation exceeds safety boundary."
        )
    elif efficacy >= 70.0 and off_target_risk <= 18.0 and ethics_score >= 65.0:
        return (
            "VIABLE THERAPY",
            "emerald",
            f"Robust therapeutic profile (Efficacy: {efficacy}%, Off-Target Risk: {off_target_risk}%). Meets PRISMA ScR clinical viability benchmark for translational delivery."
        )
    else:
        return (
            "OPTIMIZING",
            "amber",
            f"Intermediate therapeutic index (Efficacy: {efficacy}%, Off-Target: {off_target_risk}%). Dose titration, high-fidelity Cas9 selection, or delivery tuning required to achieve clearance."
        )

def generate_figure3_curves(mismatch_tol: float, cas9_variant: str) -> List[Dict[str, Any]]:
    """
    Figure 3: Efficacy vs delivery efficiency at three Cas9 concentrations (0.8 µM, 2.5 µM, 5.0 µM)
    Delivery efficiency tested from 0% to 90% (matching the exact axes of Figure 3 in the paper)
    """
    data = []
    # Test delivery efficiency points from 0 to 90
    delivery_points = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    c_low = 0.8
    c_med = 2.5
    c_high = 5.0
    
    for d in delivery_points:
        eff_low = calculate_efficacy(c_low, d, mismatch_tol, cas9_variant)
        eff_med = calculate_efficacy(c_med, d, mismatch_tol, cas9_variant)
        eff_high = calculate_efficacy(c_high, d, mismatch_tol, cas9_variant)
        data.append({
            "delivery_efficiency": d,
            "cas9_low_0_8uM": eff_low,
            "cas9_med_2_5uM": eff_med,
            "cas9_high_5_0uM": eff_high
        })
    return data

def generate_figure4_tradeoff_cohort(current_eff: float, current_risk: float) -> List[Dict[str, Any]]:
    """
    Figure 4: Efficacy vs off-target risk tradeoff, colored by system status
    Shows population cohort trials across 3 clusters: Optimizing, Viable Therapy, and Critical Risk
    """
    cohort: List[Dict[str, Any]] = []
    
    # Cluster 1: Viable Therapy (high efficacy, low off-target)
    viable_anchors = [
        ("Exa-cel Cohort (BCL11A)", 88.4, 4.2),
        ("NTLA-2001 Liver Cohort (TTR)", 91.2, 5.1),
        ("NTLA-2002 HAE Cohort (KLKB1)", 86.7, 6.4),
        ("CTX310 Phase 1 Cohort", 82.5, 7.8),
        ("High-Fidelity RNP Cohort", 89.0, 3.5),
        ("Optimized HSC Ex-Vivo", 84.1, 8.2),
        ("AAV Subretinal CEP290 (EDIT-101)", 76.5, 9.8),
    ]
    for name, eff, risk in viable_anchors:
        cohort.append({
            "name": name,
            "efficacy": eff,
            "off_target_risk": risk,
            "status": "VIABLE THERAPY",
            "color": "#10b981"
        })
        
    # Cluster 2: Optimizing (moderate efficacy or borderline off-target)
    optimizing_anchors = [
        ("WT-Cas9 Low-Dose Trial", 62.0, 14.5),
        ("CTX130 CAR-T Trial (CD70)", 68.3, 16.2),
        ("LNP Liver Escalation Step 1", 58.7, 12.0),
        ("Proviral HIV Disruption + RNAi", 64.2, 19.4),
        ("ELANE Neutropenia Pilot", 61.5, 15.8),
        ("Artemis Immunodeficiency HSC", 66.0, 17.1),
    ]
    for name, eff, risk in optimizing_anchors:
        cohort.append({
            "name": name,
            "efficacy": eff,
            "off_target_risk": risk,
            "status": "OPTIMIZING",
            "color": "#f59e0b"
        })
        
    # Cluster 3: Critical Risk (excessive off-target or inadequate efficacy)
    risk_anchors = [
        ("High-Dose WT-Cas9 Unoptimized", 74.0, 44.5),
        ("Sub-therapeutic Vector AAV", 34.0, 22.0),
        ("Non-specific gRNA Screening", 51.0, 41.2),
        ("Solid Tumor Direct In-Vivo", 38.5, 48.0),
        ("Excessive Mismatch Probe (>25%)", 69.0, 39.5)
    ]
    for name, eff, risk in risk_anchors:
        cohort.append({
            "name": name,
            "efficacy": eff,
            "off_target_risk": risk,
            "status": "CRITICAL RISK",
            "color": "#f43f5e"
        })
        
    # Add active simulated patient/therapy
    current_status = "VIABLE THERAPY" if (current_eff >= 70 and current_risk <= 18) else ("CRITICAL RISK" if current_risk >= 38 or current_eff < 45 else "OPTIMIZING")
    current_color = "#10b981" if current_status == "VIABLE THERAPY" else ("#f43f5e" if current_status == "CRITICAL RISK" else "#f59e0b")
    cohort.append({
        "name": "YOUR SIMULATION ACTIVE PROFILE",
        "efficacy": current_eff,
        "off_target_risk": current_risk,
        "status": current_status,
        "color": current_color,
        "isActive": True
    })
    
    return cohort

def generate_figure5_concentration_response(
    delivery_eff: float,
    mismatch_tol: float,
    delivery_sys: str,
    cas9_variant: str
) -> List[Dict[str, Any]]:
    """
    Figure 5: Simulated efficacy vs off-target risk as Cas9 concentration increases (0.1 µM to 10.0 µM)
    Efficacy plateaus via Hill curve while off-target risk accelerates
    """
    curve: List[Dict[str, Any]] = []
    concs = [0.2, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.5, 9.0, 10.0]
    for c in concs:
        eff = calculate_efficacy(c, delivery_eff, mismatch_tol, cas9_variant)
        risk = calculate_off_target_risk(c, delivery_eff, mismatch_tol, delivery_sys, cas9_variant)
        curve.append({
            "cas9_concentration": c,
            "efficacy": eff,
            "off_target_risk": risk
        })
    return curve

def run_simulation(
    params: TherapyParameters,
    ethics: EthicsInputs
) -> SimulationResult:
    # 1. Resolve Delivery efficiency
    del_config = DELIVERY_FACTORS.get(params.delivery_system, DELIVERY_FACTORS["LNP"])
    tissue_mult = 1.0
    if "Hepatocyte" in params.target_tissue or "Liver" in params.target_tissue:
        tissue_mult = del_config["liver_affinity"]
    elif "Stem" in params.target_tissue or "HSC" in params.target_tissue or "Hematopoietic" in params.target_tissue:
        tissue_mult = del_config["hsc_affinity"]
    elif "Retina" in params.target_tissue or "Eye" in params.target_tissue:
        tissue_mult = del_config["retina_affinity"]
        
    delivery_efficiency = round(min(98.0, max(15.0, del_config["efficiency_baseline"] * tissue_mult)), 1)
    
    # 2. Calculate Efficacy & Off-target risk
    on_target_efficacy = calculate_efficacy(
        params.cas9_concentration,
        delivery_efficiency,
        params.mismatch_tolerance,
        params.cas9_variant
    )
    
    off_target_risk = calculate_off_target_risk(
        params.cas9_concentration,
        delivery_efficiency,
        params.mismatch_tolerance,
        params.delivery_system,
        params.cas9_variant
    )
    
    # 3. Calculate Ethics composite score
    if ethics.is_germline:
        ethics_composite = 0.0
    else:
        # Weighted: Consent 40%, Equity 30%, Tracking 30%
        ethics_composite = round((ethics.consent_score * 0.40) + (ethics.equity_score * 0.30) + (ethics.tracking_score * 0.30), 1)
        
    # 4. Status verdict & explanation
    verdict, color, explanation = determine_system_verdict(
        on_target_efficacy,
        off_target_risk,
        ethics.is_germline,
        ethics_composite
    )
    
    # Regulatory readiness description
    if verdict == "VIABLE THERAPY" and ethics_composite >= 75.0:
        reg_readiness = "INVESTIGATIONAL NEW DRUG (IND) / ATMP READY"
    elif verdict == "CRITICAL RISK / RESTRICTED":
        reg_readiness = "REGULATORY HOLD / NON-COMPLIANT WITH WHO HERITABLE EDITING BAN"
    elif verdict == "CRITICAL RISK":
        reg_readiness = "SAFETY SIGNAL FLAGGED — PRE-CLINICAL PAUSE REQUIRED"
    else:
        reg_readiness = "PRE-CLINICAL OPTIMIZATION (PHASE 0 GUIDANCE)"
        
    # 5. Genomic Risk Map & Chromosome Distribution
    gene_info = get_gene_info(params.gene_symbol)
    if not gene_info:
        # Fallback gene
        gene_info = get_gene_info("BCL11A")
        
    off_targets = get_off_targets_for_gene(params.gene_symbol)
    
    # Adjust off-target cleavage probability based on current Cas9 dose and variant
    adjusted_off_targets: List[OffTargetLocus] = []
    chromosome_risk_summary: Dict[str, float] = {f"chr{i}": 0.0 for i in range(1, 23)}
    chromosome_risk_summary["chrX"] = 0.0
    chromosome_risk_summary["chrY"] = 0.0
    
    variant_mult = CAS9_VARIANTS.get(params.cas9_variant, CAS9_VARIANTS["SpCas9-HF1"])["fidelity_modifier"]
    dose_mult = (params.cas9_concentration / 2.5) ** 1.3
    
    for ot in off_targets:
        calc_prob = round(min(0.25, ot.cleavage_probability * variant_mult * dose_mult * (params.mismatch_tolerance / 12.0)), 4)
        adjusted_ot = OffTargetLocus(
            chromosome=ot.chromosome,
            locus=ot.locus,
            gene_symbol=ot.gene_symbol,
            sequence=ot.sequence,
            mismatches=ot.mismatches,
            pam=ot.pam,
            cleavage_probability=calc_prob,
            is_oncogenic_risk=ot.is_oncogenic_risk,
            description=ot.description
        )
        adjusted_off_targets.append(adjusted_ot)
        if ot.chromosome in chromosome_risk_summary:
            chromosome_risk_summary[ot.chromosome] += round(calc_prob * 100.0, 2)
            
    # Mark on-target chromosome
    if gene_info.chromosome in chromosome_risk_summary:
        chromosome_risk_summary[gene_info.chromosome] = round(chromosome_risk_summary[gene_info.chromosome] + 25.0, 2)

    # 6. Generate Figures 3, 4, 5
    fig3_data = generate_figure3_curves(params.mismatch_tolerance, params.cas9_variant)
    fig4_data = generate_figure4_tradeoff_cohort(on_target_efficacy, off_target_risk)
    fig5_data = generate_figure5_concentration_response(
        delivery_efficiency,
        params.mismatch_tolerance,
        params.delivery_system,
        params.cas9_variant
    )
    
    return SimulationResult(
        status_verdict=verdict,
        verdict_color=color,
        verdict_explanation=explanation,
        on_target_efficacy=on_target_efficacy,
        off_target_risk=off_target_risk,
        delivery_efficiency=delivery_efficiency,
        ethics_composite_score=ethics_composite,
        regulatory_readiness=reg_readiness,
        figure3_curve=fig3_data,
        figure4_scatter=fig4_data,
        figure5_concentration_curve=fig5_data,
        on_target_locus={
            "symbol": gene_info.symbol,
            "name": gene_info.name,
            "chromosome": gene_info.chromosome,
            "coordinates": gene_info.coordinates,
            "clinical_indications": gene_info.clinical_indications,
            "strategy": gene_info.cleavage_strategy,
            "representative_therapy": gene_info.representative_therapy
        },
        predicted_off_targets=adjusted_off_targets,
        chromosome_risk_summary=chromosome_risk_summary
    )
