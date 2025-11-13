# 🧩 CATEGORIZE — Configurable PDF Classification System

**CATEGORIZE** is a modular and configurable pipeline that classifies PDFs into user-defined categories (Type A, Type B, Type C, etc.) based on **keywords**, **weights**, **normalization**, and **threshold logic**.

It supports both:
- 🖥️ **CLI (Command Line Interface)**  
- 🌐 **FastAPI Server**  
- ☁️ **Local or AWS S3 Storage**

___________________________________________________________________________________________________________________________________________________________________________
**🚀 Installation & Usage**
___________________________________________________________________________________________________________________________________________________________________________
**🔹 Option 1 — Local Installation (Recommended)**
1️⃣ Clone the repository
Windows PowerShell
git clone https://github.com/dewaang-engminds/PDF-CLASSIFIER.git
cd PDF-CLASSIFIER

Mac/Linux Bash
git clone https://github.com/dewaang-engminds/PDF-CLASSIFIER.git
cd PDF-CLASSIFIER

2️⃣ Create & activate a virtual environment
Windows PowerShell
python -m venv venv
venv\Scripts\activate

Mac/Linux Bash
python3 -m venv venv
source venv/bin/activate

3️⃣ Install the package
Both PowerShell & Bash
pip install .

▶️ Using the CLI
Windows PowerShell
categorize --config config/env.yaml

Mac/Linux Bash
categorize --config config/env.yaml


**Example with input & output paths:**

categorize --input data/pdfs --output data/output --config config/env.yaml

**▶️ Running the API Server**

You can run via the CLI:

PowerShell
categorize api

Bash
categorize api


Then open:

http://127.0.0.1:8000/docs


Best practice:
✔ Keep terminal open
✔ Upload PDFs via Swagger UI
✔ Monitor logs in the console

**▶️ Running the Frontend (Local Development)**

_The frontend is static HTML. You run a tiny local server:_

Windows PowerShell
cd frontend
python -m http.server 3000

Mac/Linux Bash
cd frontend
python3 -m http.server 3000


Now open:

http://127.0.0.1:3000/app.html


This frontend will interact with your API at:

http://127.0.0.1:8000/classify/

🟢 Best Practices for Frontend + API
✔ Run frontend and API in separate terminals

Example:

Terminal 1 — API

categorize api


Terminal 2 — Frontend

cd frontend && python -m http.server 3000

✔ Keep env.yaml outside source code if sensitive

(e.g., AWS keys)

✔ Avoid mixing ports

API → 8000

Frontend → 3000

✔ Use correct Fetch URL in app.html
http://127.0.0.1:8000/classify/

🎯 OPTIONAL: Run backend directly (without CLI)

If you prefer:

PowerShell
uvicorn api.server:app --reload

Bash
uvicorn api.server:app --reload

___________________________________________________________________________________________________________________________________________________________________________

**🌟 Option 2 — Using pipx (Best for CLI Tools)**
bash
Copy code
pip install pipx
pipx install git+https://github.com/dewaang-engminds/PDF-CLASSIFIER.git

# Run
categorize --config config/env.yaml


___________________________________________________________________________________________________________________________________________________________________________

**💾 Option 3 — Download EXE (No Python Required)**
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

___________________________________________________________________________________________________________________________________________________________________________

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

___________________________________________________________________________________________________________________________________________________________________________
📄 Configuration (env.yaml)
Example snippet from config/env.yaml:

NUM_TYPES: 2
THRESHOLD: 0.65
BETA: 0.8
EPSILON: 0.05

INPUT_PATH: "data/pdfs"
OUTPUT_PATH: "data/output"

STORAGE:
  INPUT_MODE: "local"        # local / s3
  OUTPUT_MODE: "local"       # local / s3
  S3_INPUT_BUCKET: "my-input-bucket"
  S3_OUTPUT_BUCKET: "my-output-bucket"
  AWS_ACCESS_KEY: "YOUR_AWS_ACCESS_KEY"
  AWS_SECRET_KEY: "YOUR_AWS_SECRET_KEY"
  AWS_REGION: "ap-south-1"

TYPES:
  TYPE_A:
    keywords: ["Invoice No", "GST (18%)", "Date of Purchase", "Total Amount", "Product", "Payment Mode", "Model", "Seller", "IMEI", "Warranty", "Price", "Quantity"]
    weights:  [1.2, 1.1, 1.0, 1.3, 0.9, 1.0, 0.8, 0.9, 1.1, 0.8, 1.0, 0.9]

  TYPE_B:
    keywords: ["Bill No", "Tax Rate", "Invoice Date", "Grand Total", "Item", "Mode Of Payment", "Model Name", "Retailer", "Serial No", "Service Duration", "Rate", "Count"]
    weights:  [1.2, 1.0, 1.1, 1.3, 0.9, 1.0, 0.8, 0.9, 1.1, 0.8, 0.9, 0.8]
___________________________________________________________________________________________________________________________________________________________________________

🧾 License
This project is licensed under the MIT License — you are free to use, modify, and distribute it.

___________________________________________________________________________________________________________________________________________________________________________


Contributions welcome! Feel free to submit pull requests or report issues.
