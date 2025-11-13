# CATEGORIZE — Configurable PDF Classification System

CATEGORIZE is a modular pipeline to classify PDFs into user-defined categories (Type A, B, C …) based on keywords, weights, normalization, and threshold logic.  
It supports both **CLI** and **FastAPI** modes and can read/write to **local folders** or **AWS S3**.

---

## ⚙️ Quick Start

```bash
# 1️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Edit config/env.yaml
#    Define types, keywords, weights, threshold, and storage mode.

# 4️⃣ Place PDFs inside data/pdfs/

# 5️⃣ Run CLI
python main.py --input data/pdfs --output data/output --config config/env.yaml

**HOW TO USE**

****✅ How users will now install and run****
**🔹 Local installation**
git clone https://github.com/dewaang-engminds/PDF-CLASSIFIER.git
cd PDF-CLASSIFIER
pip install .

**🔹 Run the CLI**
categorize --config config/env.yaml


OR 

⭐ Encouraging you all to use venv (best practice)

python -m venv venv
venv\Scripts\activate
pip install .

Then everything installs in:

venv\Lib\site-packages\

And uninstalling is as easy as deleting the venv/ folder.


OR


**# Installation**

**## Option 1 — Install with pip (recommended)**

git clone https://github.com/dewaang-engminds/PDF-CLASSIFIER.git
cd PDF-CLASSIFIER

python -m venv venv
venv\Scripts\activate     # Windows
**# or**
source venv/bin/activate # Mac/Linux

pip install .

**# Run CLI**
categorize --config config/env.yaml

**# Run API**
categorize api

**# Run Frontend**
categorize ui


**## Option 2 — Install using pipx (best for CLI tools)**

pip install pipx
pipx install git+https://github.com/dewaang-engminds/PDF-CLASSIFIER.git

categorize --config config/env.yaml


**## Option 3 — Download EXE (no Python required)**

1. Download categorize.exe from Releases
2. Run:

categorize.exe --config env.yaml

