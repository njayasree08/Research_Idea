# CRISPR-Cas9 Clinical Decision Support & Simulation Platform

> **Translational Software Implementation of the Research Publication:**  
> *"CRISPR-Cas9 in Human Health: Where the Science Actually Stands — Therapeutic Progress, Safety Trade-offs, and the Ethics That Come With Them"*  
> **Authors:** Badru MD, Ghansah V, Adesanya IO, David J, Okechukwu NC, Eke DO (September 2026)  
> **Citation:** *Aust J Biomed Res. 2026;2(3):aubm024*

---

## 🔬 System Overview

This full-stack clinical platform directly implements the **Decision-Support Workflow (Figure 2)**, **Predictive Simulation Engines (Figures 3, 4, and 5)**, **Therapeutic Lifecycle & Feedback Systems (Figure 6)**, and comprehensive evidence databases (**Table 1** and **Table 2**) described in the research paper.

The software empowers clinical researchers, bioinformaticians, and regulatory reviewers to simulate therapeutic CRISPR-Cas9 protocols, inspect chromosome-wide genomic hazards across the human karyotype (GRCh38), evaluate bioethical compliance (strictly gating somatic vs germline interventions), and benchmark against landmark clinical trial programs (such as Exa-cel, NTLA-2001, NTLA-2002, CTX310, and EDIT-101).

---


### 1. Backend (Python 3.12 / FastAPI)
- **FastAPI**: Asynchronous RESTful endpoints with automatic OpenAPI/Swagger documentation.
- **Biophysical Simulation Engine**:
  - **On-Target Efficacy**: Modeled via cooperative Hill kinetics:
    $$\text{Efficacy} = 96.0 \times \left( \frac{C^{1.75}}{C^{1.75} + K_d^{1.75}} \right) \times \left(\frac{\text{Delivery}}{100}\right) \times \left(1 - 0.22 \times \frac{\text{Mismatch}}{50}\right) \times \text{VariantFactor}$$
    *(with $K_d = 1.15\,\mu\text{M}$)*
  - **Off-Target Cleavage Risk**: Modeled as superlinear concentration and mismatch tolerance power laws:
    $$\text{Risk}_{\text{off}} = 1.65 \times C^{1.52} \times \left(\frac{\text{Mismatch}}{10}\right)^{1.38} \times \text{Delivery}^{0.8} \times \text{FidelityModifier} \times \text{DurabilityMultiplier}$$
  - **Variant Fidelity Modifiers**:
    - Wild-Type SpCas9: `1.0x` baseline hazard
    - SpCas9-HF1: `0.28x` (72% off-target risk reduction)
    - HiFi Cas9: `0.22x` (78% off-target risk reduction)
    - evoCas9: `0.18x` (82% off-target risk reduction)
- **Ethical Gatekeeper**: Enforces somatic demarcation. Any protocol attempting heritable germline editing is immediately placed on **"REGULATORY HOLD / RESTRICTED"** per WHO international governance guidelines.

### 2. Frontend (React 19 / TypeScript / Vite / Tailwind CSS)
- **Interactive Decision-Support Simulator**: Real-time slider parameter controls for reagent concentration ($\mu\text{M}$), mismatch tolerance, delivery vector, and tissue targeting.
- **Figure 4 Scatter Plot**: Dynamic multi-colored cohort plot showing active patient simulation dot relative to published clinical trial cohorts (Exa-cel, NTLA-2001, etc.).
- **Figure 3 Line Plot**: Exact reproduction of delivery efficiency vs. efficacy across Cas9 concentrations (0.8 $\mu\text{M}$, 2.5 $\mu\text{M}$, 5.0 $\mu\text{M}$).
- **Figure 5 Dose-Response Curve**: Visualizes the saturation of on-target efficacy alongside accelerating off-target cut rates as concentration increases.
- **Human Karyotype Genomic Risk Map**: 24-chromosome visual ideogram (Chr 1 - Chr Y) highlighting on-target and off-target chromosomal risk distributions.
- **Clinical Trials Explorer**: Filterable database of Table 1 therapies and PRISMA-ScR studies with expandable clinical endpoints and published citations.
- **Lifecycle & Manufacturing Stepper (Figure 6)**: Step-by-step interactive workflow for ex-vivo stem cell apheresis and in-vivo liver LNP infusions with closed-loop registry feedback.
- **Emerging Technologies Head-to-Head**: Direct comparison of Conventional CRISPR-Cas9 vs Base Editing vs Prime Editing.
- **Dossier Generator**: Instant export of regulatory dossiers in Markdown and printable format.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10+ (Python 3.12 recommended)
- Node.js 18+ (Node 22 recommended)

### One-Command Launch (Recommended)
From the project root directory:

```bash
# Using Python runner:
python run_app.py

# Or on Windows PowerShell:
.\start.ps1

# Or on Windows Command Prompt:
start.bat
```

This single command will:
1. Verify backend and frontend dependencies.
2. Build frontend assets if needed.
3. Launch the FastAPI server on `http://127.0.0.1:8000`.
4. Automatically open your default web browser to the interactive application.

---

### Running in Developer Mode (Hot-Reloading)

If you wish to make live modifications to frontend or backend code:

#### Terminal 1: Backend
```bash
cd backend
python -m uvicorn app.main:app --reload --port 8000
```
- API Docs: `http://127.0.0.1:8000/docs`
- Root endpoint: `http://127.0.0.1:8000/`

#### Terminal 2: Frontend
```bash
cd frontend
npm run dev
```
- Frontend dev server: `http://localhost:5173` (proxies `/api` to port 8000).

---

## 📋 Direct Mapping to Research Paper Content

| Paper Section / Figure | Platform Module / Component | File Location |
| :--- | :--- | :--- |
| **Figure 1 (PRISMA-ScR Architecture)** | PRISMA Scoping Modal & Methodology Flowchart | [`frontend/src/components/PrismaScopingModal.tsx`](file:///frontend/src/components/PrismaScopingModal.tsx) |
| **Figure 2 (Decision Workflow)** | Core Decision Support Dashboard & Status Verdict | [`frontend/src/components/SimulationEngineView.tsx`](file:///frontend/src/components/SimulationEngineView.tsx) |
| **Figure 3 (Efficacy vs Delivery)** | Figure 3 Delivery Efficiency Curve (3 Cas9 Doses) | [`backend/app/services/simulation_engine.py`](file:///backend/app/services/simulation_engine.py) |
| **Figure 4 (Tradeoff Plot)** | Figure 4 Scatter Plot Colored by Status Verdict | [`frontend/src/components/SimulationEngineView.tsx`](file:///frontend/src/components/SimulationEngineView.tsx) |
| **Figure 5 (Concentration Curve)** | Figure 5 Concentration-Response Kinetic Curve | [`backend/app/services/simulation_engine.py`](file:///backend/app/services/simulation_engine.py) |
| **Figure 6 (Lifecycle & Feedback)** | Therapeutic Lifecycle & Manufacturing Pipeline | [`frontend/src/components/LifecycleWorkflow.tsx`](file:///frontend/src/components/LifecycleWorkflow.tsx) |
| **Table 1 (Clinical Pipeline)** | Clinical Trials Atlas & PRISMA ScR Studies | [`frontend/src/components/ClinicalTrialsExplorer.tsx`](file:///frontend/src/components/ClinicalTrialsExplorer.tsx) |
| **Table 2 (Safety & Mitigations)** | Safety Hazard Matrix & 15-Year Registry | [`frontend/src/components/SafetyMatrixView.tsx`](file:///frontend/src/components/SafetyMatrixView.tsx) |
| **Section 5 & 8 (Bioethics & Policy)** | Ethics Demarcation, Consent, & Equity Gatekeeper | [`frontend/src/components/EthicsGovernanceView.tsx`](file:///frontend/src/components/EthicsGovernanceView.tsx) |
| **Section 7 (Emerging Technologies)** | Conventional CRISPR vs Base vs Prime Editing | [`frontend/src/components/EmergingTechComparison.tsx`](file:///frontend/src/components/EmergingTechComparison.tsx) |



