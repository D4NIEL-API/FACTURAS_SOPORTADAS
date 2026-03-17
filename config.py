"""
config.py — Configuración central de la aplicación.

Edita GEMINI_API_KEY con tu clave de Google AI Studio,
o defínela como variable de entorno para mayor seguridad:
  set GEMINI_API_KEY=tu_clave_aqui   (Windows CMD)
  $env:GEMINI_API_KEY="tu_clave"     (Windows PowerShell)
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables desde el archivo .env si existe

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
FACTURAS_DIR: str = "buzon_de_facturas"                # Carpeta donde dejar los PDFs
OUTPUT_FILE: str  = "facturas_soportadas.xlsx"

# ---------------------------------------------------------------------------
# LÍMITES
# ---------------------------------------------------------------------------
OCR_MIN_CHARS: int = 50   # Si el texto extraído tiene menos caracteres → Warning OCR
