"""
PDF Last Page Remover

This script processes PDF files in a specified input folder, removing the last page
from each PDF and saving the modified versions in an output folder.

It includes logging for tracking the process and a progress bar for visual feedback.
"""

import os
import logging
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm
import traceback
from concurrent.futures import ThreadPoolExecutor

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_pdf(input_path: Path, output_path: Path) -> bool:
    """
    Remove the last page of the PDF and save it to the output path.

    Args:
        input_path (Path): Path to the input PDF file.
        output_path (Path): Path where the modified PDF will be saved.

    Returns:
        bool: True if processing was successful, False otherwise.
    """
    try:
        with input_path.open('rb') as file:
            pdf_reader = PdfReader(file)
            pdf_writer = PdfWriter()

            total_pages = len(pdf_reader.pages)

            if total_pages < 2:
                logging.warning(f"Skipping {input_path.name}: not enough pages to remove the last one.")
                return False

            for page_num in range(total_pages - 1):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            # Ensure the output file doesn't overwrite an existing file unless necessary
            output_path = _ensure_unique_filename(output_path)

            with output_path.open('wb') as output_file:
                pdf_writer.write(output_file)

        logging.info(f"Processed: {input_path.name}")
        return True

    except Exception as e:
        logging.error(f"Failed to process {input_path.name}: {e}")
        logging.exception(traceback.format_exc())  # Log full traceback for debugging
        return False

def remove_last_page(input_folder: str, output_folder: str):
    """
    Iterate through all PDF files in the input folder and remove the last page.

    Args:
        input_folder (str): Path to the folder containing input PDF files.
        output_folder (str): Path to the folder where modified PDFs will be saved.
    """
    input_folder_path = Path(input_folder)
    output_folder_path = Path(output_folder)

    # Create the output folder if it doesn't exist
    output_folder_path.mkdir(parents=True, exist_ok=True)

    # Get list of PDF files
    pdf_files = list(input_folder_path.glob('*.pdf'))

    # Setup progress bar
    with tqdm(total=len(pdf_files), desc="Processing PDFs") as pbar:
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_pdf, input_path, output_folder_path / f"edited_{input_path.name}") 
                       for input_path in pdf_files]
            for future in futures:
                future.result()  # Will raise any exception thrown in threads
                pbar.update(1) # Update progress bar regardless of success/failure

#def remove_last_page(input_folder: str, output_folder: str):
#    """
#    Iterate through all PDF files in the input folder and remove the last page.

#    Args:
#        input_folder (str): Path to the folder containing input PDF files.
#        output_folder (str): Path to the folder where modified PDFs will be saved.
#    """
#    input_folder_path = Path(input_folder)
#    output_folder_path = Path(output_folder)

#    # Create the output folder if it doesn't exist
#    output_folder_path.mkdir(parents=True, exist_ok=True)

#    # Get list of PDF files
#    pdf_files = list(input_folder_path.glob('*.pdf'))
    
#    # Setup progress bar
#    with tqdm(total=len(pdf_files), desc="Processing PDFs") as pbar:
#        for input_path in pdf_files:
#            output_path = output_folder_path / f"edited_{input_path.name}"
#            process_pdf(input_path, output_path)
#            pbar.update(1)  # Update progress bar regardless of success/failure

    logging.info("All PDF files have been processed.")

def _ensure_unique_filename(file_path: Path) -> Path:
    """
    Ensure the file name is unique by appending a number to the file name if needed.

    Args:
        file_path (Path): Original file path.

    Returns:
        Path: Modified file path with a unique name.
    """
    counter = 1
    new_file_path = file_path
    while new_file_path.exists():
        new_file_path = file_path.with_stem(f"{file_path.stem}_{counter}")
        counter += 1
    return new_file_path

if __name__ == "__main__":
    input_folder = "/Users/yvan/Documents/PDT"
    output_folder = "/Users/yvan/Documents/PDT/output"
    remove_last_page(input_folder, output_folder)
