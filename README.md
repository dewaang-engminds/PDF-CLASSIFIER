🧩 CATEGORIZE — Configurable PDF Classification System

CATEGORIZE is a modular, customizable, and lightweight pipeline that classifies PDF documents into user-defined categories (for example, Type A, Type B, Type C, etc.) using keywords, weights, normalization, and threshold-based logic.

It supports:
🖥️ Command Line Interface (CLI)
🌐 FastAPI Server
☁️ Local or AWS S3 Storage

🚀 Installation & Usage
🔹 Option 1 — Local Installation (Recommended)

Step 1 — Clone the Repository

Windows PowerShell
git clone https://github.com/dewaang-engminds/PDF-CLASSIFIER.git

cd PDF-CLASSIFIER

Mac/Linux Terminal
git clone https://github.com/dewaang-engminds/PDF-CLASSIFIER.git

cd PDF-CLASSIFIER

Step 2 — Create & Activate a Virtual Environment

Windows PowerShell
python -m venv venv
venv\Scripts\activate

Mac/Linux Terminal
python3 -m venv venv
source venv/bin/activate

Step 3 — Install the Package
pip install .

▶️ Using the CLI

Windows PowerShell / Mac/Linux Terminal
categorize --config config/env.yaml

Example with input & output paths:
categorize --input data/pdfs --output data/output --config config/env.yaml

▶️ Running the API Server

You can launch the API directly via CLI.

PowerShell or Bash
categorize api

Then open:
http://127.0.0.1:8000/docs

Best Practices:
✔ Keep the terminal open
✔ Upload PDFs via Swagger UI
✔ Monitor logs in real-time through the console

▶️ Running the Frontend (Local Development)

The frontend is a static HTML interface. You can run it via a lightweight local server.

Windows PowerShell
cd frontend
python -m http.server 3000

Mac/Linux Terminal
cd frontend
python3 -m http.server 3000

Then open:
http://127.0.0.1:3000/app.html

This frontend communicates with your API endpoint at:
http://127.0.0.1:8000/classify/

🟢 Best Practices for Frontend + API Setup

✔ Run frontend and API in separate terminals.
• Terminal 1 — API: categorize api
• Terminal 2 — Frontend: cd frontend && python -m http.server 3000

✔ Keep env.yaml outside source folder if it contains sensitive data (for example, AWS credentials).
✔ Avoid port conflicts — API runs on port 8000 and Frontend runs on port 3000.
✔ Ensure correct fetch URL in app.html: http://127.0.0.1:8000/classify/

🎯 Optional: Run Backend Directly (Without CLI)

PowerShell or Bash
uvicorn api.server:app --reload

🌟 Option 2 — Using pipx (Recommended for CLI Tools)

pip install pipx
pipx install git+https://github.com/dewaang-engminds/PDF-CLASSIFIER.git

Run the CLI:
categorize --config config/env.yaml

💾 Option 3 — Download EXE (No Python Required)

Step 1 — Download
Go to the latest release:
PDF-CLASSIFIER Releases (https://github.com/dewaang-engminds/PDF-CLASSIFIER/releases
)

Download categorize.zip

Step 2 — Extract
Inside, you’ll find:
categorize.exe

Step 3 — Run

▶️ CLI Mode
categorize.exe --config env.yaml

🌐 API Server
categorize.exe api
Then open: http://127.0.0.1:8000/docs

💻 Frontend UI
categorize.exe ui
Then open: http://127.0.0.1:3000/

🖱️ Double-Click Mode
You can also double-click categorize.exe to launch the default mode.

🧠 Best Practice — Virtual Environments

Creating a virtual environment helps isolate dependencies and keep your system clean.

python -m venv venv
venv\Scripts\activate
pip install .

All packages install inside:
venv\Lib\site-packages\

To uninstall completely, simply delete the venv/ folder.

📄 Configuration — env.yaml

Below is an example configuration file:

NUM_TYPES: 2
THRESHOLD: 0.65
BETA: 0.8
EPSILON: 0.05

INPUT_PATH: "data/pdfs"
OUTPUT_PATH: "data/output"

STORAGE:
INPUT_MODE: "local" # local / s3
OUTPUT_MODE: "local" # local / s3
S3_INPUT_BUCKET: "my-input-bucket"
S3_OUTPUT_BUCKET: "my-output-bucket"
AWS_ACCESS_KEY: "YOUR_AWS_ACCESS_KEY"
AWS_SECRET_KEY: "YOUR_AWS_SECRET_KEY"
AWS_REGION: "ap-south-1"

TYPES:
TYPE_A:
keywords: ["Invoice No", "GST (18%)", "Date of Purchase", "Total Amount", "Product", "Payment Mode", "Model", "Seller", "IMEI", "Warranty", "Price", "Quantity"]
weights: [1.2, 1.1, 1.0, 1.3, 0.9, 1.0, 0.8, 0.9, 1.1, 0.8, 1.0, 0.9]

TYPE_B:
keywords: ["Bill No", "Tax Rate", "Invoice Date", "Grand Total", "Item", "Mode Of Payment", "Model Name", "Retailer", "Serial No", "Service Duration", "Rate", "Count"]
weights: [1.2, 1.0, 1.1, 1.3, 0.9, 1.0, 0.8, 0.9, 1.1, 0.8, 0.9, 0.8]

🧾 License

This project is licensed under the MIT License — you are free to use, modify, and distribute it.

❤️ Contributors

Dewaang Mathur — Lead Developer

Contributions are always welcome!
Feel free to submit pull requests or open issues.

✨ Tip: Customize your categories, keywords, and thresholds in env.yaml to adapt this classifier for invoices, resumes, or any other domain-specific document classification.
