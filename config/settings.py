import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FACTURA_DIRS = [
    "./Cuentas de Cobro Abril",
    "./Cuentas de Cobro Marzo"
]
