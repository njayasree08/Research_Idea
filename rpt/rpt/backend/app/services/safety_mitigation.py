from typing import List, Dict, Any

SAFETY_BARRIERS_TABLE_2: List[Dict[str, Any]] = [
    {
        "id": "BAR-01",
        "barrier": "Off-target editing",
        "severity": "CRITICAL",
        "primary_concern": "Unintended double-strand cuts generating indels, large chromosomal translocations, chromothripsis, and p53 stress-response activation leading to oncogenic transformation.",
        "biological_mechanism": "Cas9 tolerance for 1-4 base mismatches between guide RNA and non-target genomic DNA loci containing an adjacent PAM (NGG) site.",
        "current_mitigations": [
            "Engineered high-fidelity Cas9 variants (SpCas9-HF1, HiFi Cas9, eSpCas9) reducing non-specific binding energy",
            "Comprehensive empirical off-target nomination assays: GUIDE-seq, CIRCLE-seq, DISCOVER-seq",
            "Transient RNP delivery limiting intracellular Cas9 exposure window to <24-48 hours",
            "Next-generation sequencing (NGS) deep amplicon validation with >100,000x coverage depth"
        ],
        "regulatory_requirement": "Pre-clinical genome-wide off-target profiling required by FDA CBER / EMA Committee for Advanced Therapies (CAT) prior to IND clearance."
    },
    {
        "id": "BAR-02",
        "barrier": "Delivery bottlenecks",
        "severity": "HIGH",
        "primary_concern": "Viral vector immunogenicity and insertional mutagenesis vs non-viral inefficiency and limited extrahepatic biodistribution.",
        "biological_mechanism": "AAV capsids elicit neutralizing antibodies preventing re-dosing and carry risk of genomic integration; LNPs naturally accumulate in hepatocytes via ApoE adsorption, limiting access to brain, heart, and kidney.",
        "current_mitigations": [
            "Ionizable Lipid Nanoparticle (LNP) formulation optimization for high mRNA/gRNA entrapment and endosomal escape",
            "Tissue-targeted ligand conjugation (GalNAc for hepatocytes, anti-CD4/CD34 ligands for lymphocytes)",
            "Engineered Virus-Like Particles (VLPs) delivering pre-formed ribonucleoprotein complexes without viral genetic material",
            "Subretinal and local intra-compartmental micro-injections for immune-privileged organs (eye/CNS)"
        ],
        "regulatory_requirement": "Biodistribution and tissue-specific clearance validation across rodent and non-human primate GLP toxicology studies."
    },
    {
        "id": "BAR-03",
        "barrier": "Host Immunogenicity & Conditioning Toxicity",
        "severity": "HIGH",
        "primary_concern": "Humoral and cytotoxic T-cell responses against bacterial Cas9 protein; acute infusion-related reactions; toxicities associated with myeloablative conditioning.",
        "biological_mechanism": "Streptococcus pyogenes (SpCas9) and Staphylococcus aureus (SaCas9) are ubiquitous human commensal pathogens; up to 60-70% of healthy humans possess pre-existing antibodies and reactive CD4+/CD8+ T-cells.",
        "current_mitigations": [
            "Pre-screening patients for anti-Cas9 IgG antibodies and Cas9-specific ELISpot reactivity prior to therapy",
            "Transient immunosuppressive regimens and steroid pre-medication for in vivo infusions",
            "Development of Cas9 orthologs from non-pathogenic extremophiles or epitope-masked de-immunized variants",
            "Replacement of toxic alkylating myeloablation (busulfan) with targeted non-genotoxic antibody-drug conjugates (anti-CD117 / briquilimab)"
        ],
        "regulatory_requirement": "Mandatory monitoring of anti-drug antibodies (ADA) and cytokine storm panels across all Phase 1-3 clinical protocols."
    },
    {
        "id": "BAR-04",
        "barrier": "Durability & Sparse Multi-Year Follow-up",
        "severity": "MODERATE / LONG-TERM",
        "primary_concern": "Lack of 10-15 year human clinical outcome data; theoretical risk of stem cell senescence, loss of edited clones over time, or delayed clonal expansion.",
        "biological_mechanism": "Epigenetic silencing of edited promoters or gradual exhaustion of engineered long-term repopulating hematopoietic stem cells (LT-HSCs).",
        "current_mitigations": [
            "Mandatory 15-year post-treatment registry surveillance (US FDA Post-Marketing Commitment / European EBMT Registry)",
            "Serial clonal tracking via single-cell RNA-seq and V(D)J deep sequencing to detect clonal dominance early",
            "Standardized real-world evidence (RWE) registries with centralized safety signal monitoring and pausing criteria",
            "Annual bone marrow biopsies and digital droplet PCR (ddPCR) for vector and indel stability"
        ],
        "regulatory_requirement": "Global registry compliance tied to conditional marketing authorization with annual renewal audits."
    }
]

def get_safety_barriers() -> List[Dict[str, Any]]:
    return SAFETY_BARRIERS_TABLE_2
