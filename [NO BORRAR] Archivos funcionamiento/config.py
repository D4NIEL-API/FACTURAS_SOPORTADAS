"""
config.py — Configuración central de la aplicación.

Edita GEMINI_API_KEY con tu clave de Google AI Studio,
o defínela como variable de entorno para mayor seguridad:
  set GEMINI_API_KEY=tu_clave_aqui   (Windows CMD)
  $env:GEMINI_API_KEY="tu_clave"     (Windows PowerShell)
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Busca [API KEY].env en la misma carpeta que este archivo (independientemente del CWD)
_BASE_DIR = Path(__file__).parent
load_dotenv(dotenv_path=_BASE_DIR / "[API KEY].env")

# ---------------------------------------------------------------------------
# API KEY
# Se intenta leer de la variable de entorno (por defecto desde el .env); 
# de lo contrario, deja un string vacío o mensaje genérico.
# ---------------------------------------------------------------------------
GEMINI_API_KEY: str = os.environ.get("GEMINI_API_KEY", "")

# ---------------------------------------------------------------------------
# MODELO
# Comprueba en https://aistudio.google.com/ cuál tienes habilitado.
# Ejemplos válidos (marzo 2025):
#   "gemini-2.0-flash"
#   "gemini-1.5-pro"
#   "gemini-2.5-pro-preview-03-25"
# ---------------------------------------------------------------------------
GEMINI_MODEL: str = "gemini-3.1-flash-lite-preview"

# ---------------------------------------------------------------------------
# RUTAS
# ---------------------------------------------------------------------------
FACTURAS_DIR: str = str(_BASE_DIR.parent / "BUZON_DE_FACTURAS_SOPORTADAS")  # Carpeta PDFs (en raíz)
OUTPUT_FILE: str  = str(_BASE_DIR.parent / "FACTURAS_SOPORTADAS.xlsx")       # Excel (en raíz)

# ---------------------------------------------------------------------------
# LÍMITES
# ---------------------------------------------------------------------------
OCR_MIN_CHARS: int = 50   # Si el texto extraído tiene menos caracteres → Warning OCR
