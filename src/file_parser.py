import os
from PyPDF2 import PdfReader

def parse_pdf(file_path):
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def parse_files(directory):
    """Parse all files in the given directory."""
    parsed_data = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if file_name.endswith(".pdf"):
            text = parse_pdf(file_path)
            if not text.strip():
                print(f"Warning: No text extracted from {file_name}. Skipping file.")
                continue
            print(f"Extracted text from {file_name}: {text[:100]}...")
            parsed_data.append({"file_name": file_name, "text": text})
    return parsed_data
