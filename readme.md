
# PDF Editor (Last Page Remover)

This Python script processes PDF files in a specified input folder, removes the last page from each PDF, and saves the modified versions in an output folder.

## Features

- **Batch Processing**: Processes all PDF files in a folder.
- **Page Removal**: Removes only the last page of each PDF.
- **Progress Bar**: Provides real-time feedback on the progress of the operation using `tqdm`.
- **Logging**: Logs information about the files processed and any warnings or errors encountered.
- **Parallel Processing**: Uses multi-threading to process multiple PDFs concurrently for better performance.

## Requirements

- Python 3.7+
- `PyPDF2`: For reading and writing PDFs.
- `tqdm`: For displaying a progress bar.

You can install the required dependencies using `pip3`:

```bash
pip3 install PyPDF2 tqdm
```

## Usage

### 1. Clone the repository or download the script

You can either clone this repository or download the `pdf_editor.py` script to your local machine.

```bash
git clone https://github.com/Yvancg/pdf_editor.git
```

### 2. Set up your input and output folders

- Place your PDF files in the input folder (e.g., `/path/to/your/input/folder`).
- The script will save the modified PDFs (with the last page removed) in the output folder (e.g., `/path/to/your/output/folder`).

### 3. Run the script

Run the script by executing the following command:

```bash
python pdf_editor.py
```

You can modify the `input_folder` and `output_folder` paths inside the script if needed. By default, the script is set to:

```python
input_folder = "/path/to/your/input/folder"
output_folder = "/path/to/your/output/folder"
```

### 4. Example folder structure

```
Documents/
    PDF/
        input/
            file1.pdf
            file2.pdf
        output/
```

- All original PDFs should be placed in the `input/` folder.
- After processing, the modified PDFs will be saved in the `output/` folder, with `edited_` prefixed to the filename (e.g., `edited_file1.pdf`).

## Code Overview

The script consists of several key functions, each serving a specific purpose:

### 1. `process_pdf(input_path: Path, output_path: Path) -> bool`

- This function reads a PDF from the input path and removes its last page.
- It uses the `PdfReader` and `PdfWriter` classes from the `PyPDF2` library.
- If the PDF has fewer than two pages, it logs a warning and skips the file.
- Ensures the output file does not overwrite an existing file by calling `_ensure_unique_filename()`.

### 2. `remove_last_page(input_folder: str, output_folder: str)`

- The main function that orchestrates the removal of the last page from all PDFs in the input folder.
- Uses a progress bar (`tqdm`) for visual feedback on the processing status.
- Files are processed in parallel using Python’s `ThreadPoolExecutor` for improved performance.

### 3. `_ensure_unique_filename(file_path: Path) -> Path`

- This helper function ensures that if a file with the same name already exists in the output folder, it appends a number to the file name to avoid overwriting.
- The function checks if the file exists and iteratively appends a counter (e.g., `_1`, `_2`) to the file name.

### 4. Logging and Error Handling

- The script uses Python’s `logging` module for tracking events, warnings, and errors.
- In case of an exception, it logs the full traceback using `logging.exception()` for easier debugging.

### 5. Parallel Processing

- The `ThreadPoolExecutor` is used to process PDFs concurrently, which is beneficial when handling a large number of files.
- The results of the threads are monitored to ensure that any exceptions are raised and logged.

## Contributions

Feel free to submit pull requests, report issues, or request additional features!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project uses the PyPDF2 library to manipulate PDF files.
