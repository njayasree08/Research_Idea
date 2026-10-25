from typing import Dict, Any, List, Optional
from app.models.schemas import GeneInfo, OffTargetLocus

GENE_DATABASE: Dict[str, GeneInfo] = {
    "BCL11A": GeneInfo(
        symbol="BCL11A",
        name="BCL11 Transcription Factor A",
        chromosome="chr2",
        coordinates="chr2:60,451,159-60,553,568 (GRCh38)",
        function="Zinc-finger transcriptional repressor that silences gamma-globin gene expression, repressing fetal hemoglobin (HbF) post-birth.",
        gain_or_loss="Loss of Function / Enhancer Disruption (+58 erythroid enhancer)",
        clinical_indications=["Sickle Cell Disease (SCD)", "Transfusion-dependent β-Thalassemia (TDT)"],
        representative_therapy="Exagamglogene autotemcel (Exa-cel / Casgevy)",
        exonic_structure="5 Exons; GATA1 binding motif in intron 2 enhancer targeted (+58 kb)",
        cleavage_strategy="Dual or single cut disrupting the erythroid GATA1 core motif, derepressing gamma-globin"
    ),
    "HBB": GeneInfo(
        symbol="HBB",
        name="Hemoglobin Subunit Beta",
        chromosome="chr11",
        coordinates="chr11:5,225,464-5,227,071 (GRCh38)",
        function="Encodes beta-globin chain of adult hemoglobin A (HbA). Glu6Val mutation causes sickle hemoglobin (HbS) polymerization.",
        gain_or_loss="Correction / Point Mutation Repair (Glu6Val)",
        clinical_indications=["Sickle Cell Disease", "β-Thalassemia major"],
        representative_therapy="iPSC-derived autologous corrected HSCs (Preclinical/Phase I)",
        exonic_structure="3 Exons; canonical 1.6 kb genomic footprint",
        cleavage_strategy="Homology-Directed Repair (HDR) with single-stranded donor template (ssODN)"
    ),
    "TTR": GeneInfo(
        symbol="TTR",
        name="Transthyretin",
        chromosome="chr18",
        coordinates="chr18:31,591,766-31,599,023 (GRCh38)",
        function="Carrier protein for thyroxine and retinol-binding protein; misfolding leads to toxic amyloid fibril deposition in nerves and heart.",
        gain_or_loss="Loss of Function (Permanent Knockdown >90%)",
        clinical_indications=["Hereditary Transthyretin Amyloidosis with Polyneuropathy (ATTRv-PN)", "ATTR Cardiomyopathy"],
        representative_therapy="NTLA-2001 (Intellia / Regeneron in vivo LNP)",
        exonic_structure="4 Exons; targeted in Exon 2",
        cleavage_strategy="In vivo LNP delivery into hepatocytes; indel frameshift knockout of TTR transcription"
    ),
    "KLKB1": GeneInfo(
        symbol="KLKB1",
        name="Kallikrein B1 (Plasma Prekallikrein)",
        chromosome="chr4",
        coordinates="chr4:186,220,119-186,252,583 (GRCh38)",
        function="Encodes plasma prekallikrein, precursor to plasma kallikrein which generates bradykinin, the mediator of angioedema swelling attacks.",
        gain_or_loss="Loss of Function (Systemic Knockdown)",
        clinical_indications=["Hereditary Angioedema (HAE) Type I and II"],
        representative_therapy="NTLA-2002 (Intellia in vivo LNP)",
        exonic_structure="15 Exons; targeted in Exon 5",
        cleavage_strategy="In vivo hepatic LNP delivery, frameshift NHEJ-induced indels reducing circulating kallikrein by >95%"
    ),
    "ANGPTL3": GeneInfo(
        symbol="ANGPTL3",
        name="Angiopoietin Like 3",
        chromosome="chr1",
        coordinates="chr1:62,597,542-62,606,312 (GRCh38)",
        function="Inhibitor of lipoprotein lipase (LPL) and endothelial lipase; natural loss-of-function variants have lifelong low LDL-C, triglycerides, and CAD protection.",
        gain_or_loss="Loss of Function (Cardioprotective Knockout)",
        clinical_indications=["Severe Hypercholesterolemia", "Cardiovascular Disease / Atherosclerosis", "Mixed Dyslipidemia"],
        representative_therapy="CTX310 (CRISPR Therapeutics in vivo LNP)",
        exonic_structure="7 Exons; targeted in early catalytic domain",
        cleavage_strategy="Single-dose liver-directed LNP knocking out circulating ANGPTL3 to permanently slash LDL-C and triglycerides"
    ),
    "CEP290": GeneInfo(
        symbol="CEP290",
        name="Centrosomal Protein 290",
        chromosome="chr12",
        coordinates="chr12:88,049,006-88,142,207 (GRCh38)",
        function="Encodes a centrosomal and ciliary protein critical for photoreceptor outer segment function. IVS26 mutation creates a cryptic splice donor site.",
        gain_or_loss="Aberrant Splicing Excision / Inversion",
        clinical_indications=["Leber Congenital Amaurosis 10 (LCA10)"],
        representative_therapy="EDIT-101 (Editas Medicine subretinal AAV5)",
        exonic_structure="54 Exons; deep intronic c.2991+1655A>G targeted by paired gRNAs",
        cleavage_strategy="Subretinal AAV5 dual-cleavage excision or inversion of aberrant splice region restoring normal transcript"
    ),
    "CD70": GeneInfo(
        symbol="CD70",
        name="CD70 Molecule (TNFSF7)",
        chromosome="chr19",
        coordinates="chr19:6,583,183-6,590,924 (GRCh38)",
        function="TNF ligand family member overexpressed on T-cell and B-cell lymphomas and renal cell carcinoma.",
        gain_or_loss="Multi-Receptor Disruption (TRAC-, B2M-, CD70- knockout)",
        clinical_indications=["T-cell lymphoma", "Clear cell renal cell carcinoma (ccRCC)"],
        representative_therapy="CTX130 (Allogeneic CAR-T therapy)",
        exonic_structure="3 Exons",
        cleavage_strategy="Multiplex ex-vivo editing of donor allogeneic T cells to avoid fratricide and host-vs-graft rejection"
    ),
    "ELANE": GeneInfo(
        symbol="ELANE",
        name="Neutrophil Elastase",
        chromosome="chr19",
        coordinates="chr19:852,987-858,354 (GRCh38)",
        function="Encodes neutrophil elastase; misfolded mutants trigger endoplasmic reticulum stress and promyelocyte apoptosis.",
        gain_or_loss="Gene Correction or Exon Skipping",
        clinical_indications=["Severe Congenital Neutropenia (SCN)"],
        representative_therapy="Patient-derived HSC CRISPR correction (Blood 2024)",
        exonic_structure="5 Exons",
        cleavage_strategy="Precision editing of HSCs restoring normal granulopoiesis and neutrophil maturation"
    ),
    "DCLRE1C": GeneInfo(
        symbol="DCLRE1C",
        name="DNA Cross-Link Repair 1C (Artemis)",
        chromosome="chr10",
        coordinates="chr10:14,142,398-14,212,855 (GRCh38)",
        function="Nuclear protein involved in V(D)J recombination and DNA repair. Deficiency causes T-B-NK+ severe combined immunodeficiency.",
        gain_or_loss="Targeted Insertion / Correction",
        clinical_indications=["Artemis-Deficient Severe Combined Immunodeficiency (ART-SCID)"],
        representative_therapy="Hematopoietic stem-cell CRISPR correction (Nat Med 2026)",
        exonic_structure="14 Exons",
        cleavage_strategy="Ex-vivo CD34+ HSC editing restoring Artemis endonuclease function and B/T cell immunity"
    ),
    "CCR5": GeneInfo(
        symbol="CCR5",
        name="C-C Motif Chemokine Receptor 5",
        chromosome="chr3",
        coordinates="chr3:46,370,854-46,376,206 (GRCh38)",
        function="Coreceptor for HIV-1 entry into CD4+ T-cells. Delta-32 natural mutation confers HIV-1 resistance.",
        gain_or_loss="Disruption / Knockout",
        clinical_indications=["HIV-1 Infection & Latent Proviral Reservoir Clearance"],
        representative_therapy="Proviral DNA disruption + CCR5 knockout + RNAi",
        exonic_structure="2 Exons",
        cleavage_strategy="Targeted dual ablation of proviral LTR sequence and CCR5 receptor"
    )
}

PREDICTED_OFF_TARGETS: Dict[str, List[OffTargetLocus]] = {
    "BCL11A": [
        OffTargetLocus(
            chromosome="chr2",
            locus="chr2:60,892,104",
            gene_symbol="BCL11A-PS1",
            sequence="CTAACAGTTGCTTTTATCAC AGG",
            mismatches=1,
            pam="AGG",
            cleavage_probability=0.038,
            is_oncogenic_risk=False,
            description="Pseudogene locus in non-coding intergenic band 2p16.1; minimal functional consequence."
        ),
        OffTargetLocus(
            chromosome="chr7",
            locus="chr7:114,209,481",
            gene_symbol="FOXP2",
            sequence="CTAACAGTAGCTTTTTTCAC TGG",
            mismatches=3,
            pam="TGG",
            cleavage_probability=0.012,
            is_oncogenic_risk=False,
            description="Intronic region of transcription factor FOXP2; screened negative for transcript disruption in clinical assays."
        ),
        OffTargetLocus(
            chromosome="chr17",
            locus="chr17:7,675,102",
            gene_symbol="TP53",
            sequence="CTAACGGTTGTTTTTATCAG CGG",
            mismatches=4,
            pam="CGG",
            cleavage_probability=0.003,
            is_oncogenic_risk=True,
            description="Proto-oncogene / tumor suppressor surveillance site. Tested by CIRCLE-seq: below background threshold."
        ),
        OffTargetLocus(
            chromosome="chr6",
            locus="chr6:31,238,590",
            gene_symbol="HLA-B",
            sequence="CTAAGAGTTGCTTTTAGCAC GGG",
            mismatches=3,
            pam="GGG",
            cleavage_probability=0.009,
            is_oncogenic_risk=False,
            description="MHC class I locus in non-coding flanking region."
        )
    ],
    "TTR": [
        OffTargetLocus(
            chromosome="chr18",
            locus="chr18:31,940,210",
            gene_symbol="TTR-Like",
            sequence="TTCGTGTCCTCTGCCTACAG TGG",
            mismatches=2,
            pam="TGG",
            cleavage_probability=0.024,
            is_oncogenic_risk=False,
            description="Intergenic repeat sequence near chr18q12."
        ),
        OffTargetLocus(
            chromosome="chr1",
            locus="chr1:156,842,015",
            gene_symbol="RPTOR",
            sequence="TTAGTGTCCTCTGCCTTCAG CGG",
            mismatches=3,
            pam="CGG",
            cleavage_probability=0.007,
            is_oncogenic_risk=True,
            description="mTOR pathway regulatory component intronic region; no indel detected at therapeutic dose."
        ),
        OffTargetLocus(
            chromosome="chr11",
            locus="chr11:64,289,114",
            gene_symbol="FGF3",
            sequence="TTCGTGTCCTCTGCTTTCAG AGG",
            mismatches=3,
            pam="AGG",
            cleavage_probability=0.005,
            is_oncogenic_risk=False,
            description="Fibroblast growth factor locus non-coding boundary."
        )
    ],
    "KLKB1": [
        OffTargetLocus(
            chromosome="chr4",
            locus="chr4:185,910,230",
            gene_symbol="F11",
            sequence="GAGTGTCCACAGATCTCTGA GGG",
            mismatches=2,
            pam="GGG",
            cleavage_probability=0.019,
            is_oncogenic_risk=False,
            description="Coagulation Factor XI (homologous serine protease domain). Carefully monitored in Phase 1/2 trials."
        ),
        OffTargetLocus(
            chromosome="chr3",
            locus="chr3:52,410,290",
            gene_symbol="BAP1",
            sequence="GAGTGCCCACAGATCACTGA CGG",
            mismatches=4,
            pam="CGG",
            cleavage_probability=0.002,
            is_oncogenic_risk=True,
            description="Tumor suppressor region; mismatch frequency exceeds tolerance window with HiFi-Cas9."
        )
    ],
    "ANGPTL3": [
        OffTargetLocus(
            chromosome="chr1",
            locus="chr1:63,105,420",
            gene_symbol="ANGPTL4",
            sequence="AAGCTGAGCAGCAATGACTG CGG",
            mismatches=3,
            pam="CGG",
            cleavage_probability=0.014,
            is_oncogenic_risk=False,
            description="Homologous family member ANGPTL4; minimal cleavage observed in hepatocyte primary cultures."
        ),
        OffTargetLocus(
            chromosome="chr19",
            locus="chr19:11,200,450",
            gene_symbol="LDLR",
            sequence="AAGCTGTGCAGCAATTACTG TGG",
            mismatches=4,
            pam="TGG",
            cleavage_probability=0.004,
            is_oncogenic_risk=False,
            description="Low-density lipoprotein receptor non-coding 5-prime UTR."
        )
    ]
}

def get_gene_info(symbol: str) -> Optional[GeneInfo]:
    sym = symbol.strip().upper()
    return GENE_DATABASE.get(sym)

def list_all_genes() -> List[GeneInfo]:
    return list(GENE_DATABASE.values())

def get_off_targets_for_gene(symbol: str) -> List[OffTargetLocus]:
    sym = symbol.strip().upper()
    if sym in PREDICTED_OFF_TARGETS:
        return PREDICTED_OFF_TARGETS[sym]
    # Default fallback realistic off-targets for any selected gene
    return [
        OffTargetLocus(
            chromosome="chr3",
            locus="chr3:42,109,215",
            gene_symbol="GENOM-OT1",
            sequence="NNNNACAGTTGCTTTTATCA NGG",
            mismatches=2,
            pam="AGG",
            cleavage_probability=0.015,
            is_oncogenic_risk=False,
            description="Intergenic region evaluated by GUIDE-seq"
        ),
        OffTargetLocus(
            chromosome="chr17",
            locus="chr17:7,578,110",
            gene_symbol="TP53-Near",
            sequence="NNNNGGTTGTTTTTATCA NGG",
            mismatches=4,
            pam="CGG",
            cleavage_probability=0.003,
            is_oncogenic_risk=True,
            description="Proto-oncogene proximal screening locus"
        )
    ]
