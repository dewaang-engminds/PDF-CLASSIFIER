from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from pathlib import Path
from pipeline.runner import run_pipeline
from utils.logger import setup_logger
from config.settings import load_config

logger = setup_logger()
app = FastAPI(title="CATEGORIZE API", version="1.0")

@app.post("/classify/")
async def classify_pdf(
    file: UploadFile = File(...),
    config_text: str = Form(None),
    input_mode: str = Form("local"),
    output_mode: str = Form("local")
):
    """
    Upload a PDF and (optionally) provide a YAML config string.
    The file is temporarily stored in /temp and processed through the pipeline.
    """
    tmp_dir = Path("temp")
    tmp_dir.mkdir(exist_ok=True)

    pdf_path = tmp_dir / file.filename
    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    # if YAML config provided from frontend textarea, save temp config
    cfg_path = "config/env.yaml"
    if config_text:
        cfg_temp = tmp_dir / "temp_env.yaml"
        with open(cfg_temp, "w", encoding="utf-8") as f:
            f.write(config_text)
        cfg_path = str(cfg_temp)

    logger.info(f"Processing upload via API: {file.filename}")
    predicted = run_pipeline(str(tmp_dir), "data/output", cfg_path, single=True)
    return JSONResponse({"file": file.filename, "predicted_type": predicted})

# run with uvicorn api.server:app --reload
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)