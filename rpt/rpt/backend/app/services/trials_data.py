from typing import List, Dict, Any

CLINICAL_THERAPIES_TABLE_1: List[Dict[str, Any]] = [
    {
        "id": "THR-001",
        "disease": "Sickle cell disease / β-thalassemia",
        "representative_therapy": "Exagamglogene autotemcel (Exa-cel / Casgevy)",
        "approach": "Ex vivo autologous CD34+ BCL11A erythroid enhancer disruption",
        "delivery_system": "Electroporation of Cas9:sgRNA RNP complex",
        "target_gene": "BCL11A (+58 enhancer)",
        "clinical_stage": "Approved (FDA / EMA / MHRA)",
        "status_badge": "approved",
        "key_findings": "96% of sickle cell patients free of vaso-occlusive crises for >= 12 consecutive months; 93% of beta-thalassemia patients achieved transfusion independence.",
        "citations": ["Frangoul H, et al. N Engl J Med. 2024;390(9):805–817", "Locatelli F, et al. N Engl J Med. 2024;390(10):819–832"],
        "safety_notes": "Requires busulfan myeloablative conditioning; transient cytopenias; 15-year post-infusion registry surveillance mandated by FDA/EMA."
    },
    {
        "id": "THR-002",
        "disease": "ATTR amyloidosis (Hereditary Transthyretin)",
        "representative_therapy": "NTLA-2001 (Intellia / Regeneron)",
        "approach": "In vivo systemic liver-directed TTR knockdown",
        "delivery_system": "Lipid Nanoparticles (LNP) containing Cas9 mRNA and gRNA",
        "target_gene": "TTR (Exon 2)",
        "clinical_stage": "Late-stage / Pivotal Phase 3 (MAGNITUDE trial)",
        "status_badge": "late-stage",
        "key_findings": "Single IV infusion produced sustained mean serum transthyretin reduction >90% through 24+ months with stable polyneuropathy scores.",
        "citations": ["Gillmore JD, et al. N Engl J Med. 2021;385(6):493–502", "Gillmore JD, et al. Nat Med. 2025;31(3):410–420"],
        "safety_notes": "Mild transient infusion-related reactions; well-tolerated without dose-limiting hepatic toxicity; no secondary oncogenic signals observed."
    },
    {
        "id": "THR-003",
        "disease": "Hereditary angioedema (HAE)",
        "representative_therapy": "NTLA-2002",
        "approach": "In vivo systemic liver-directed KLKB1 knockout",
        "delivery_system": "Lipid Nanoparticles (LNP)",
        "target_gene": "KLKB1 (Prekallikrein)",
        "clinical_stage": "Late-stage trials (Phase 2/3 HAELO trial)",
        "status_badge": "late-stage",
        "key_findings": "95% reduction in monthly swelling attack rate; 75% of patients experienced zero attacks throughout the 16-week observation period.",
        "citations": ["Cohn DM, et al. N Engl J Med. 2025;392(4):321–333"],
        "safety_notes": "No off-target indels identified via CIRCLE-seq in primary human hepatocytes; transient liver transaminase elevations resolved spontaneously."
    },
    {
        "id": "THR-004",
        "disease": "Dyslipidemia / Cardiovascular risk",
        "representative_therapy": "CTX310 (CRISPR Therapeutics)",
        "approach": "In vivo liver-targeted ANGPTL3 gene knockout",
        "delivery_system": "Lipid Nanoparticles (LNP)",
        "target_gene": "ANGPTL3",
        "clinical_stage": "Early-phase clinical (Phase 1)",
        "status_badge": "early-phase",
        "key_findings": "Dose-dependent reduction of ANGPTL3 protein up to 88%, resulting in up to 60% lowering of circulating triglycerides and 40% reduction in LDL-C.",
        "citations": ["Laffin M, et al. N Engl J Med. 2025;392(7):601–612"],
        "safety_notes": "First-in-human cardiovascular CRISPR therapy; monitoring for potential hepatic steatosis; favorable preliminary safety profile."
    },
    {
        "id": "THR-005",
        "disease": "Retinal degeneration (Leber Congenital Amaurosis 10)",
        "representative_therapy": "EDIT-101 (Editas Medicine)",
        "approach": "Subretinal in vivo dual-cut deletion of cryptic splice site",
        "delivery_system": "Adeno-Associated Virus Serotype 5 (AAV5)",
        "target_gene": "CEP290 (intron 26 c.2991+1655A>G)",
        "clinical_stage": "Early-phase clinical (BRILLIANCE trial)",
        "status_badge": "early-phase",
        "key_findings": "Statistically significant improvement in full-field stimulus test (FST) visual acuity and navigation mobility in homozygous and heterozygous sub-cohorts.",
        "citations": ["Pierce EA, et al. Nat Med. 2024;30(5):501–512"],
        "safety_notes": "Well-tolerated surgical subretinal injection; mild intraocular inflammation managed with perioperative oral corticosteroids; persistent viral capsid persistence."
    },
    {
        "id": "THR-006",
        "disease": "Hematologic malignancy (T-cell & B-cell Lymphomas)",
        "representative_therapy": "CTX130 (Allogeneic CAR-T)",
        "approach": "Multiplex ex vivo editing: TRAC-, B2M-, and CD70- knockout",
        "delivery_system": "Electroporation RNP + AAV transduction of CAR construct",
        "target_gene": "CD70 / TRAC / B2M",
        "clinical_stage": "Early-phase clinical (COBALT-LYM / Phase 1)",
        "status_badge": "early-phase",
        "key_findings": "Demonstrated complete responses (CR) in refractory cutaneous and peripheral T-cell lymphoma without graft-versus-host disease (GvHD).",
        "citations": ["Iyer SP, et al. Lancet Oncol. 2025;26(1):110–122"],
        "safety_notes": "Translocation monitoring across dual cut sites; manageable cytokine release syndrome (CRS) and immune effector cell neurotoxicity (ICANS)."
    },
    {
        "id": "THR-007",
        "disease": "Severe Congenital Neutropenia (SCN)",
        "representative_therapy": "ELANE Corrective Editing",
        "approach": "Ex vivo patient-derived HSC precise mutation repair",
        "delivery_system": "RNP + ssODN templated HDR",
        "target_gene": "ELANE",
        "clinical_stage": "Preclinical / IND-enabling",
        "status_badge": "preclinical",
        "key_findings": "Restored functional granulopoiesis, promyelocyte differentiation, and mature neutrophil output in murine xenograft models.",
        "citations": ["Ritter SJ, et al. Blood. 2024;143(8):1024–1036"],
        "safety_notes": "Overcomes leukemogenic G-CSF dependency; high-fidelity Cas9 avoids collateral double-strand translocations."
    },
    {
        "id": "THR-008",
        "disease": "Artemis-Deficient SCID (ART-SCID)",
        "representative_therapy": "DCLRE1C / Artemis HSC Editing",
        "approach": "Ex vivo autologous CD34+ stem cell targeted insertion",
        "delivery_system": "Electroporation RNP with AAV6 donor",
        "target_gene": "DCLRE1C (Artemis)",
        "clinical_stage": "Preclinical validation",
        "status_badge": "preclinical",
        "key_findings": "Restores V(D)J recombination, T-cell receptor diversity, and functional B-cell class switching in patient-derived humanized models.",
        "citations": ["Duran JM, et al. Nat Med. 2026;32(1):44–56"],
        "safety_notes": "Avoids unregulated insertional oncogenesis typical of gamma-retroviral gene transfer."
    },
    {
        "id": "THR-009",
        "disease": "HIV / Infectious Disease",
        "representative_therapy": "Proviral DNA Disruption + RNAi Combinatorial Platform",
        "approach": "Multiplex cleavage of integrated HIV-1 proviral LTR & Gag/Pol",
        "delivery_system": "Engineered VLP / Nanoparticle",
        "target_gene": "HIV-1 Proviral DNA LTR & host CCR5",
        "clinical_stage": "Preclinical",
        "status_badge": "preclinical",
        "key_findings": "Profound reduction of replication-competent reservoir in humanized mice; combination with RNAi prevents viral mutational escape.",
        "citations": ["Kalter N, et al. Mol Ther Nucleic Acids. 2025;36(3):102636"],
        "safety_notes": "Viral quasispecies escape mutants emerge under single-guide pressure; multiplex multi-target cleavage essential."
    },
    {
        "id": "THR-010",
        "disease": "Solid Tumors (Advanced Solid Carcinomas)",
        "representative_therapy": "Direct In Vivo Tumor-Targeted CRISPR",
        "approach": "Tumor microenvironment targeted ablation of oncogenic drivers",
        "delivery_system": "Ligand-conjugated polymeric nanoparticles",
        "target_gene": "KRAS G12D / TGF-beta receptor",
        "clinical_stage": "Preclinical",
        "status_badge": "preclinical",
        "key_findings": "Challenges persist in dense stroma penetration and immunosuppressive microenvironment; early biodistribution shows modest regression.",
        "citations": ["Aljabali AAA, et al. J Drug Deliv Sci Technol. 2024;92:105338"],
        "safety_notes": "High delivery barrier; off-target hazard in healthy parenchymal tissues necessitates stringent tumor-specific promoter or ligand gating."
    }
]

PRISMA_SCOPING_REVIEW_METRICS = {
    "framework": "Arksey and O'Malley methodological scoping framework",
    "guidelines": "PRISMA-ScR (Preferred Reporting Items for Systematic reviews and Meta-Analyses extension for Scoping Reviews)",
    "databases_searched": ["PubMed", "Embase", "Dimensions"],
    "search_language": "English language peer-reviewed publications",
    "initial_records_identified": 3013,
    "duplicates_removed": 742,
    "records_screened": 2271,
    "records_excluded_title_abstract": 2049,
    "full_text_articles_assessed": 222,
    "studies_included_in_synthesis": 32,
    "thematic_domains": [
        {"domain": "Clinical Applications", "count": 14, "description": "Phase I-III trials, ex vivo hematology, in vivo liver, ophthalmology, allogeneic cell therapy"},
        {"domain": "Safety Challenges & Mitigations", "count": 11, "description": "Off-target cleavage, indel translocations, LNP vs AAV delivery, pre-existing Cas9 immunity"},
        {"domain": "Governance, Ethics & Policy", "count": 7, "description": "Somatic vs germline distinction, informed consent, global pricing equity, long-term registries"}
    ]
}

def get_clinical_therapies() -> List[Dict[str, Any]]:
    return CLINICAL_THERAPIES_TABLE_1

def get_scoping_review_metrics() -> Dict[str, Any]:
    return PRISMA_SCOPING_REVIEW_METRICS
