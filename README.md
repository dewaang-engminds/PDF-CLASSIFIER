# 🧩 CATEGORIZE — Configurable PDF Classification System

**CATEGORIZE** is a modular and configurable pipeline that classifies PDFs into user-defined categories (Type A, Type B, Type C, etc.) based on **keywords**, **weights**, **normalization**, and **threshold logic**.

It supports both:
- 🖥️ **CLI (Command Line Interface)**  
- 🌐 **FastAPI Server**  
- ☁️ **Local or AWS S3 Storage**

---

## ⚙️ Quick Start

```bash
# 1️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
# or
venv\Scripts\activate         # Windows

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Edit config/env.yaml
#    Define categories, keywords, weights, and thresholds.

# 4️⃣ Place PDFs inside data/pdfs/

# 5️⃣ Run the CLI
python main.py --input data/pdfs --output data/output --config config/env.yaml
🚀 Installation & Usage
🔹 Option 1 — Local Installation (Recommended)
bash
Copy code
# Clone the repository
git clone https://github.com/dewaang-engminds/PDF-CLASSIFIER.git
cd PDF-CLASSIFIER

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # Mac/Linux

# Install the package
pip install .
▶️ Run CLI
bash
Copy code
categorize --config config/env.yaml
▶️ Run API
bash
Copy code
categorize api
# Open http://127.0.0.1:8000/docs
▶️ Run Frontend
bash
Copy code
categorize ui
# Open http://127.0.0.1:3000/
🌟 Option 2 — Using pipx (Best for CLI Tools)
bash
Copy code
pip install pipx
pipx install git+https://github.com/dewaang-engminds/PDF-CLASSIFIER.git

# Run
categorize --config config/env.yaml
💾 Option 3 — Download EXE (No Python Required)
🧱 Step 1: Download
Go to the latest release:
👉 PDF-CLASSIFIER Releases

Download categorize.zip

📦 Step 2: Extract
Unzip the archive — inside, you’ll find:

Copy code
categorize.exe
⚡ Step 3: Run
▶️ CLI Mode
bash
Copy code
categorize.exe --config env.yaml
🌐 API Server
bash
Copy code
categorize.exe api
# Opens: http://127.0.0.1:8000/docs
💻 Frontend UI
bash
Copy code
categorize.exe ui
# Opens: http://127.0.0.1:3000/
🖱️ Double-Click Mode
Just double-click categorize.exe to launch the default mode.

🧠 Best Practice: Virtual Environments
Creating a virtual environment isolates dependencies and keeps your system clean.

bash
Copy code
python -m venv venv
venv\Scripts\activate
pip install .
📂 Everything installs in:

vbnet
Copy code
venv\Lib\site-packages\
🧹 To uninstall, simply delete the venv/ folder.

📄 Configuration (env.yaml)
Example snippet from config/env.yaml:

yaml
Copy code
categories:
  TypeA:
    keywords: ["invoice", "bill"]
    weight: 1.2
  TypeB:
    keywords: ["resume", "profile"]
    weight: 0.8

threshold: 0.6
storage: local
📦 Directory Structure
css
Copy code
PDF-CLASSIFIER/
│
├── config/
│   └── env.yaml
│
├── data/
│   ├── pdfs/
│   └── output/
│
├── src/
│   ├── main.py
│   └── utils/
│
└── README.md
🧾 License
This project is licensed under the MIT License — you are free to use, modify, and distribute it.

❤️ Contributors
Dewaang Mathur — Lead Developer

Contributions welcome! Feel free to submit pull requests or report issues.
