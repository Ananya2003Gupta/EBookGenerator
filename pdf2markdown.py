import os
from pdfminer.high_level import extract_text

class PDFProcessor:
    def __init__(self, pdf_directory, markdown_directory):
        """
        Initialize the PDFProcessor with the specified PDF and Markdown directories.

        Args:
            pdf_directory (str): Path to the directory containing PDF files.
            markdown_directory (str): Path to the directory where Markdown files will be saved.
        """
        self.pdf_directory = pdf_directory
        self.markdown_directory = markdown_directory
    
    def extract_text_from_pdf(self, pdf_path):
        """
        Extract text from a PDF file.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            str: Extracted text from the PDF file.
        """
        return extract_text(pdf_path)
    
    def convert_to_markdown(self, text):
        """
        Convert extracted text from PDF to Markdown format.

        Args:
            text (str): Text extracted from a PDF file.

        Returns:
            str: Text in Markdown format.
        """
        # Basic conversion: turning lines that look like titles or subtitles into Markdown headers
        lines = text.split("\n")
        for i, line in enumerate(lines):
            stripped = line.strip()
            # If a line is in ALL CAPS and not too long, treat it as a header
            if stripped.isupper() and len(stripped) < 50:
                lines[i] = f"## {stripped}"  # Convert to level-2 header
        return "\n".join(lines)
    
    def process_pdfs_in_directory(self):
        """
        Process all PDF files in the specified PDF directory and convert them to Markdown format.
        The converted Markdown files are saved in the specified Markdown directory.
        """
        for filename in os.listdir(self.pdf_directory):
            if filename.endswith(".pdf"):
                markdown_filename = filename.replace(".pdf", "_markdown.md")
                markdown_path = os.path.join(self.markdown_directory, markdown_filename)
                
                # Check if the Markdown file already exists
                if os.path.exists(markdown_path):
                    print(f"Markdown for {filename} already exists. Skipping...")
                    continue
                
                pdf_path = os.path.join(self.pdf_directory, filename)
                
                # Extract text from PDF
                extracted_text = self.extract_text_from_pdf(pdf_path)
                
                # Convert extracted text to Markdown
                markdown_text = self.convert_to_markdown(extracted_text)
                
                # Save the Markdown text
                with open(markdown_path, "w", encoding="utf-8") as md_file:
                    md_file.write(markdown_text)
                
                print(f"Processed {filename} and saved Markdown to {markdown_filename}")