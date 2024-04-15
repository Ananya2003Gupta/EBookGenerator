import os
from pdf2markdown import PDFProcessor

def main():
    pdf_directory = os.path.join("example", "examplepdf") # Replace with the path to your PDF directory
    markdown_directory = os.path.join("example", "generatedmarkdown", "docs")  # Replace with the path to your Markdown directory
    processor = PDFProcessor(pdf_directory, markdown_directory)
    processor.process_pdfs_in_directory()

if __name__ == "__main__":
    main()