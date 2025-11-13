from pathlib import Path
from config.settings import load_config
from pipeline.extract import extract_text
from pipeline.classify import classify_document
from pipeline.organize import move_pdf
from pipeline.analytics import generate_analytics
from utils.file_utils import list_local_pdfs
from utils.logger import setup_logger

logger = setup_logger()


def run_pipeline(input_folder: str, output_folder: str, config_path: str = None, single: bool = False):
    """
    Orchestrates extraction, classification, organization, and analytics.
    """
    cfg = load_config(config_path)
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # this is only for folders
    # pdfs = list_local_pdfs(str(input_path))
    # if not pdfs:
    #     logger.warning("No PDFs found in input folder.")
    #     return

    #this is now for single file and folders both
    # --- Support both single file and folder input ---
    pdfs = []

    if input_path.is_file() and input_path.suffix.lower() == ".pdf":
        # Single PDF path
        pdfs = [input_path]

    elif input_path.is_dir():
        # Folder of PDFs
        pdfs = list_local_pdfs(str(input_path))

    else:
        logger.warning(f"Input path is neither a PDF nor a directory: {input_path}")
        return

    if not pdfs:
        logger.warning("No PDFs found in provided path.")
        return

    analytics_data = []

    for pdf in pdfs:
        logger.info(f"Processing: {pdf.name}")
        text = extract_text(pdf, output_path)
        predicted, scores, details = classify_document(text, config_path)

        # organize into folders
        move_pdf(pdf, output_path, predicted, cfg)

        analytics_data.append({
            "FileName": pdf.name,
            "PredictedType": predicted,
            "PredictedScore": scores.get(predicted, 0.0),
            "AllScores": scores,
            "KeywordDetails": details,
        })

        logger.info(f"{pdf.name} -> {predicted} (score={scores.get(predicted, 0.0):.3f})")


    generate_analytics(output_path, analytics_data)

    if single:
        return analytics_data[-1]["PredictedType"]