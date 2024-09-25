import os
from PyPDF2 import PdfReader, PdfWriter

def remove_last_page(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all PDF files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"edited_{filename}")

            # Open the PDF file
            with open(input_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                pdf_writer = PdfWriter()

                # Get the total number of pages
                total_pages = len(pdf_reader.pages)

                # Copy all pages except the last one
                for page_num in range(total_pages - 1):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)

                # Save the new PDF without the last page
                with open(output_path, 'wb') as output_file:
                    pdf_writer.write(output_file)

            print(f"Processed: {filename}")

    print("All PDF files have been processed.")

# Example usage
input_folder = "/path/to/your/input/folder"
output_folder = "/path/to/your/output/folder"
remove_last_page(input_folder, output_folder)
