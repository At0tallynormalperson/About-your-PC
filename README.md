# About your PC

A small Python script that prints information about a Windows PC (CPU, RAM, storage, GPU, manufacturer, etc.).

## Prerequisites
- A computer running Windows 10 or later
- Python 3.8+ (3.x)
- The dependency listed in `requirements.txt` (psutil)

## Installation
1. Clone the repo:
   git clone https://github.com/At0tallynormalperson/About-your-PC.git
   cd About-your-PC

2. (Optional) Create and activate a virtual environment:
   - Windows (PowerShell):
     python -m venv venv
     .\venv\Scripts\Activate.ps1
   - Windows (cmd):
     python -m venv venv
     .\venv\Scripts\activate.bat

3. Install dependencies:
   pip install -r requirements.txt

## Usage
Run the script from PowerShell or cmd on Windows:
python About_your_PC_test.py

The script prints system information such as device name, OS, processor, CPU cores, installed RAM, storage for C:, GPU, manufacturer, model, and Windows edition.

## Notes
- This script is Windows-specific: it calls PowerShell and uses `C:\` paths. It will not work on a Linux/macOS runner without modification.
- `requirements.txt` should contain `psutil` (example: `psutil==5.9.5`) so CI and other users can install the dependency.
- If you want GitHub Actions to run the script as-is, change the workflow job to run on a Windows runner:
  ```yaml
  runs-on: windows-latest
