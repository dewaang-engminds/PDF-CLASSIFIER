from pathlib import Path
from utils.file_utils import copy_local, upload_to_s3
from config.settings import load_config


def move_pdf(pdf_path: Path, output_path: Path, category: str, cfg: dict):
    """
    Move or upload PDF to categorized folder/S3 based on STORAGE config.
    """
    mode = cfg.get("STORAGE", {}).get("OUTPUT_MODE", "local")
    if mode == "s3":
        bucket = cfg["STORAGE"]["S3_OUTPUT_BUCKET"]
        key = f"{category}/{pdf_path.name}"
        upload_to_s3(bucket, key, pdf_path, cfg)
    else:
        dest = output_path / category / pdf_path.name
        copy_local(pdf_path, dest)