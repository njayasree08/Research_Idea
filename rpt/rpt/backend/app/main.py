import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import simulation, genes, trials, safety, emerging, reports

app = FastAPI(
    title="CRISPR-Cas9 Clinical Decision Support Platform",
    description="Translational simulation engine, genomic risk mapper, and ethical decision-support system based on 'CRISPR-Cas9 in Human Health: Where the Science Actually Stands' (September 2026).",
    version="1.0.0"
)

# Enable CORS for local Vite development and production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(simulation.router)
app.include_router(genes.router)
app.include_router(trials.router)
app.include_router(safety.router)
app.include_router(emerging.router)
app.include_router(reports.router)

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "service": "crispr-cas9-backend"}

@app.get("/api/paper-info")
def get_paper_metadata():
    return {
        "platform": "CRISPR-Cas9 Clinical Decision Support System",
        "paper_title": "CRISPR-Cas9 in Human Health: Where the Science Actually Stands — Therapeutic Progress, Safety Trade-offs, and the Ethics That Come With Them",
        "authors": "Badru MD, Ghansah V, Adesanya IO, David J, Okechukwu NC, Eke DO",
        "publication_date": "September 2026",
        "citation": "Badru MD, et al. Aust J Biomed Res. 2026;2(3):aubm024",
        "modules": [
            "Therapy Simulation Engine (Hill Kinetics & Off-Target Power Model)",
            "Genomic Risk Map & Karyotype Locus Visualizer",
            "PRISMA ScR Clinical Trials Explorer (Table 1 & 32 Studies)",
            "Safety Barriers & Risk Mitigation Matrix (Table 2)",
            "Emerging Editing Technologies Comparison (Base & Prime Editing)",
            "Ethical & Regulatory Decision Dossier Generator"
        ]
    }

# Mount static frontend build if present
BASE_DIR = Path(__file__).resolve().parent.parent.parent
FRONTEND_DIST = BASE_DIR / "frontend" / "dist"

if FRONTEND_DIST.exists() and (FRONTEND_DIST / "index.html").exists():
    app.mount("/assets", StaticFiles(directory=FRONTEND_DIST / "assets"), name="assets")

    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        file_path = FRONTEND_DIST / full_path
        if file_path.exists() and file_path.is_file():
            return FileResponse(file_path)
        return FileResponse(FRONTEND_DIST / "index.html")
else:
    @app.get("/")
    def read_root():
        return get_paper_metadata()
