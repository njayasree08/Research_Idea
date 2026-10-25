Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "  CRISPR-Cas9 Decision Support Platform (Badru et al., 2026)" -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

$pythonExe = (Get-Command python).Source
Write-Host "[*] Using Python: $pythonExe" -ForegroundColor Green

python run_app.py
