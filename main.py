import pandas as pd
from pathlib import Path
from config.settings import FACTURA_DIRS
from processing.pdf_reader import extract_text_from_pdf
from processing.gemini_extractor import extract_json_from_text
import json

def run_pipeline():
    results = []

    for folder in FACTURA_DIRS:
        for pdf_path in Path(folder).rglob("DSE*.pdf"):
            print(f"Procesando: {pdf_path}")
            text = extract_text_from_pdf(pdf_path)
            if not text:
                continue

            json_data = extract_json_from_text(
                text,
                filename=pdf_path.name,
                folder=pdf_path.parent.name
            )

            if json_data:
                results.append(json_data)

    if results:
        df = pd.json_normalize(results)
        with open("data/output.json", "w", encoding="utf-8") as f:
            json.dump(df.to_dict(orient="records"), f, ensure_ascii=False, indent=2)
        print("Datos exportados a data/output")
    else:
        print("No se encontraron datos válidos.")

if __name__ == "__main__":
    run_pipeline()
