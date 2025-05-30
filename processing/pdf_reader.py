import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as doc:
            return "\n".join(page.get_text() for page in doc)
    except Exception as e:
        print(f"Error leyendo PDF {pdf_path}: {e}")
        return ""
