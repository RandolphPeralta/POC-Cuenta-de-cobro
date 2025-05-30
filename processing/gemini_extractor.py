import google.generativeai as genai
import json
from config.settings import GEMINI_API_KEY
from processing.utils import load_prompt

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192
    }
)


def extract_json_from_text(pdf_text, filename, folder):
    prompt = load_prompt()
    input_text = f"{pdf_text}\n\nNombre del archivo: {filename}\nCarpeta origen: {folder}"

    try:
        response = model.generate_content([
            {"role": "user", "parts": [{"text": prompt}]},
            {"role": "user", "parts": [{"text": input_text}]}
        ])
        raw = response.text.strip()
        print(f"\n---- RAW GEMINI ({filename}) ----\n{raw}\n-------------------------\n")
        if raw.startswith("Documento no corresponde"):
            return None
        # quita ```, ```json, etc.
        cleaned = raw.strip().lstrip("```").rstrip("```").strip()
        if cleaned.lower().startswith("json"):
            cleaned = cleaned[4:].strip()
        return json.loads(cleaned)
    except Exception as e:
        print(f"Error procesando Gemini: {e}")
        return None

