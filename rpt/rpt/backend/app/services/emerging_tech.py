from typing import List, Dict, Any

EMERGING_TECHNOLOGIES_COMPARISON: List[Dict[str, Any]] = [
    {
        "id": "TECH-01",
        "name": "Conventional CRISPR-Cas9",
        "architecture": "SpCas9 endonuclease + single guide RNA (sgRNA)",
        "mechanism": "Double-Strand DNA Break (DSB) followed by non-homologous end joining (NHEJ) or homology-directed repair (HDR)",
        "dna_cleavage": "Blunt or staggered double-strand break across both DNA strands",
        "editing_capabilities": "Gene knockout via frameshift indels, large genomic deletions with dual sgRNAs, targeted insertion via HDR template",
        "clinical_maturity": "Most Clinically Advanced (FDA & EMA approved therapies: Exa-cel, late-phase NTLA-2001)",
        "efficiency": "High (70% - 95% on-target editing in clinical HSCs and hepatocytes)",
        "indel_profile": "Variable indels at cut site (NHEJ error-prone repair)",
        "translocation_risk": "Moderate to High when multiple sites or homologous loci are cut simultaneously",
        "delivery_footprint": "~4.2 kb (SpCas9 cDNA) — compact enough for single AAV or LNP co-formulation",
        "strengths": [
            "Strongest human clinical track record in hematology and hepatology",
            "Highest on-target cutting efficiency across primary cells",
            "Simpler gRNA design and validated off-target assays (GUIDE-seq)"
        ],
        "limitations": [
            "Mandates double-strand breaks which trigger p53 DNA damage response",
            "High frequency of heterogeneous indels rather than clean single-base changes",
            "Potential for large chromosomal rearrangements and translocations"
        ]
    },
    {
        "id": "TECH-02",
        "name": "Base Editing (BE)",
        "architecture": "Cas9 Nickase (D10A) + Cytidine or Adenosine Deaminase + Uracil Glycosylase Inhibitor (UGI)",
        "mechanism": "Single-strand nick with enzymatic deamination of target base without double-strand break",
        "dna_cleavage": "Single-strand nick on non-edited strand to bias DNA mismatch repair (No DSB)",
        "editing_capabilities": "Transition point mutations: C•G to T•A (Cytosine Base Editors) or A•T to G•C (Adenine Base Editors)",
        "clinical_maturity": "Phase 1 / 2 Clinical Trials (e.g. PCSK9 knockout for hypercholesterolemia, sickle cell disease)",
        "efficiency": "Moderate to High (50% - 85% in target cell lines)",
        "indel_profile": "Extremely low (<1-3% indels)",
        "translocation_risk": "Near Zero (absence of simultaneous DSBs eliminates chromosomal translocations)",
        "delivery_footprint": "~5.2 kb — challenges single AAV packaging capacity (requires dual AAV or LNP mRNA)",
        "strengths": [
            "Clean point mutation installation without double-strand breaks",
            "Virtually eliminates chromosomal translocations and chromothripsis",
            "Can address up to 60% of all known pathogenic human single nucleotide variants (SNVs)"
        ],
        "limitations": [
            "Restricted to transition mutations (cannot perform transversions, insertions, or deletions)",
            "Strict PAM-distance editing window (typically 4-5 nt window; bystander editing risk)",
            "RNA off-target deamination observed with first-generation deaminases"
        ]
    },
    {
        "id": "TECH-03",
        "name": "Prime Editing (PE)",
        "architecture": "Cas9 Nickase (H840A) + Engineered Reverse Transcriptase (RT) + prime editing guide RNA (pegRNA)",
        "mechanism": "Target nicking, hybridization of pegRNA primer binding site, reverse transcription of template into genomic DNA",
        "dna_cleavage": "Targeted single-strand nick (No DSB)",
        "editing_capabilities": "Complete 'Search-and-Replace': all 12 base-to-base substitutions, insertions up to dozens of bp, and precise deletions",
        "clinical_maturity": "Early Clinical & Preclinical IND-Enabling Studies",
        "efficiency": "Moderate (25% - 65%, undergoing rapid optimization with PE6/twinPE architectures)",
        "indel_profile": "Very low (<1-2% unintended indels)",
        "translocation_risk": "Near Zero (absence of DSBs)",
        "delivery_footprint": ">6.5 kb — exceeds single viral vector limit; requires dual-AAV, split-intein, or mRNA LNP",
        "strengths": [
            "Ultimate versatility: can install any substitution, insertion, or deletion without donor DNA",
            "Far less constrained by PAM location compared to Base Editors",
            "High target specificity: three separate DNA hybridization steps required for editing"
        ],
        "limitations": [
            "Large molecular footprint makes in vivo delivery complex",
            "Lower raw editing efficiency in certain primary resting cell types",
            "pegRNA design requires optimization of PBS (primer binding site) and RT template lengths"
        ]
    }
]

def get_emerging_tech() -> List[Dict[str, Any]]:
    return EMERGING_TECHNOLOGIES_COMPARISON
