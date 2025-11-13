# this extract.py saves the markdown text files alongside the pdfs

# from pathlib import Path
# from markitdown import MarkItDown
# from utils.logger import setup_logger

# logger = setup_logger()


# def extract_text(input_file: Path, output_folder: Path, save_text: bool = True) -> str:
#     """
#     Extract text from a PDF using MarkItDown and optionally save as .txt file.
#     """
#     md = MarkItDown(enable_plugins=False)
#     result = md.convert(input_file)
#     text = result.text_content or ""

#     if save_text:
#         text_path = output_folder / f"{input_file.stem}.txt"
#         output_folder.mkdir(parents=True, exist_ok=True)
#         with open(text_path, "w", encoding="utf-8") as f:
#             f.write(text)
#         logger.info(f"Extracted and saved text for {input_file.name}")

#     return text




# this extract.py do not saves the markdown text files alongside the pdfs

from pathlib import Path
from markitdown import MarkItDown
from utils.logger import setup_logger

logger = setup_logger()


def extract_text(input_file: Path, output_folder: Path = None, save_text: bool = False) -> str:
    """
    Extract text from a PDF using MarkItDown.
    
    No .txt files are saved. Only pure text is returned.
    """
    md = MarkItDown(enable_plugins=False)
    result = md.convert(input_file)
    text = result.text_content or ""

    logger.info(f"Extracted text for {input_file.name}")

    return text