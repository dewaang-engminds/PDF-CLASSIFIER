import boto3
from botocore.exceptions import NoCredentialsError
from pathlib import Path
import shutil
from typing import List
from utils.logger import setup_logger

logger = setup_logger()


def list_local_pdfs(folder: str) -> List[Path]:
    """
    Return a list of all PDF files in the local folder.
    """
    p = Path(folder)
    if not p.exists():
        logger.warning(f"Input folder not found: {folder}")
        return []
    return list(p.glob("*.pdf"))


def get_s3_client(cfg: dict):
    return boto3.client(
        "s3",
        aws_access_key_id=cfg.get("STORAGE", {}).get("AWS_ACCESS_KEY"),
        aws_secret_access_key=cfg.get("STORAGE", {}).get("AWS_SECRET_KEY"),
        region_name=cfg.get("STORAGE", {}).get("AWS_REGION"),
    )


def download_from_s3(bucket: str, key: str, dst: Path, cfg: dict) -> bool:
    s3 = get_s3_client(cfg)
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        s3.download_file(bucket, key, str(dst))
        return True
    except NoCredentialsError:
        logger.error("S3 credentials invalid or missing.")
        return False
    except Exception as e:
        logger.error(f"Failed to download from S3: {e}")
        return False


def upload_to_s3(bucket: str, key: str, src: Path, cfg: dict) -> bool:
    s3 = get_s3_client(cfg)
    try:
        s3.upload_file(str(src), bucket, key)
        return True
    except Exception as e:
        logger.error(f"S3 upload failed: {e}")
        return False


def copy_local(src: Path, dst: Path):
    """
    Copy file locally with folder creation.
    """
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dst)
    logger.info(f"Copied {src} -> {dst}")