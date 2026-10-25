"""
CRISPR-Cas9 Decision Support Platform
Translating 'CRISPR-Cas9 in Human Health: Where the Science Actually Stands' (September 2026)
Badru MD, Ghansah V, Adesanya IO, David J, Okechukwu NC, Eke DO.

Usage:
    python run_app.py
"""

import sys
import os
import subprocess
import webbrowser
import time
from pathlib import Path

def main():
    root_dir = Path(__file__).resolve().parent
    backend_dir = root_dir / "backend"
    frontend_dist = root_dir / "frontend" / "dist"

    print("=" * 70)
    print("  CRISPR-Cas9 Clinical Decision Support & Simulation Platform")
    print("  Where the Science Actually Stands (September 2026)")
    print("=" * 70)

    # Check if frontend is built
    if not (frontend_dist / "index.html").exists():
        print("[*] Building frontend assets...")
        frontend_dir = root_dir / "frontend"
        subprocess.run(["npm", "run", "build"], cwd=frontend_dir, check=True, shell=True)

    print("\n[*] Starting FastAPI server on http://127.0.0.1:8000...")
    print("[*] API Documentation available at: http://127.0.0.1:8000/docs")
    print("[*] Interactive Full-Stack Application: http://127.0.0.1:8000\n")

    # Change directory to backend so relative imports work
    os.chdir(backend_dir)
    sys.path.insert(0, str(backend_dir))

    import uvicorn
    # Open browser automatically after half a second
    def open_browser():
        time.sleep(1.2)
        webbrowser.open("http://127.0.0.1:8000")
        
    import threading
    threading.Thread(target=open_browser, daemon=True).start()

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False)

if __name__ == "__main__":
    main()
