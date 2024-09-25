# PDF Last Page Remover

This Python script allows you to bulk edit PDF files in a specific folder by removing the last page of each PDF and saving the modified versions.

## Features

- Processes all PDF files in a specified input folder
- Removes the last page from each PDF
- Saves modified PDFs in a specified output folder
- Prefixes modified files with "edited_"

## Requirements

- Python 3.6+
- PyPDF2 library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/YOUR_USERNAME/pdf_editor.git
   cd pdf_editor
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open `pdf_editor.py` in a text editor.

2. Update the `input_folder` and `output_folder` variables with the appropriate paths:
   ```python
   input_folder = "/path/to/your/input/folder"
   output_folder = "/path/to/your/output/folder"
   ```

3. Run the script:
   ```
   python pdf_editor.py
   ```

The script will process all PDF files in the input folder, remove the last page from each, and save the modified versions in the output folder with "edited_" prefixed to the original filename.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

This project uses the PyPDF2 library to manipulate PDF files.