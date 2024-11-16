if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
  throw "Python is not installed. Please install Python to proceed."
}
python -m venv myenv
Set-Location myenv/Scripts
./Activate.ps1
Set-Location ../..
pip install --upgrade pip
pip install -r requirements.txt
