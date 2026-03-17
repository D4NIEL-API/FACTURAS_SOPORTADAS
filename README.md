# Facturas Soportadas DBS

Este proyecto es una aplicación Python que extrae automáticamente, mediante OCR e Inteligencia Artificial (Google Gemini), los datos clave de facturas en formato PDF para contabilidad (fiscalidad española), y los exporta a un archivo Excel estructurado (listo para presentar o exportar a otros programas contables).

## Instalación en un Nuevo PC

Para instalar este programa en otro ordenador con Windows, sigue estos pasos:

### 1. Requisitos Previos
- Instalar **Python 3.9 o superior**. (Durante la instalación, asegúrate de marcar la casilla *"Add Python to PATH"*).

### 2. Descargar el Proyecto
Puedes descargar este repositorio como un archivo ZIP desde GitHub y descomprimirlo, o bien clonarlo usando Git:
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd <nombre_de_la_carpeta>
```

### 3. Instalar Dependencias
Abre una terminal (Símbolo del sistema o PowerShell) en la carpeta del proyecto y ejecuta:
```bash
pip install -r requirements.txt
```

### 4. Configurar la Clave de la API (Gemini)
El programa utiliza Google Gemini AI. Necesitas tu clave de API para que funcione.
1. Localiza el archivo `[API KEY].env.example` en la carpeta.
2. Cópialo y renombra la copia a `[API KEY].env`.
3. Ábrelo con el Bloc de notas y reemplaza `tu_clave_aqui` por tu verdadera API Key de Google:
   ```env
   GEMINI_API_KEY=AIzaSyTuClaveReal...
   ```
*(Nota: El archivo `[API KEY].env` nunca se debe subir a GitHub por seguridad, ya está ignorado en `.gitignore`).*

### 5. Preparar las Carpetas de Datos
La primera vez que ejecutes el programa (o creándolas tú mismo manualmente), asegúrate de que exista la carpeta donde pondrás las facturas:
1. Crea una carpeta llamada `BUZON_DE_FACTURAS_SOPORTADAS` en el mismo directorio del programa.
2. Coloca dentro los archivos PDF de tus facturas.

## Uso

Una vez instaladas las dependencias, configurado el `[API KEY].env`, y colocados los PDFs en `BUZON_DE_FACTURAS_SOPORTADAS`, hay dos maneras de ejecutar el programa:

- **Doble Clic:** Haz doble clic sobre `INICIAR_FACTURAS_SOPORTADAS_DBS.bat`.
- **Desde la Terminal:** Abre una terminal en la carpeta y escribe:
  ```bash
  python main.py
  ```

El programa leerá todos los PDFs, extraerá los importes y conceptos, y generará (o actualizará si ya existe) el archivo `facturas_soportadas.xlsx`. Los archivos procesados con éxito serán renombrados añadiendo el prefijo `[PROCESADA]_`.

## Compilar un Ejecutable (.exe)
Si deseas crear un archivo ejecutable que no requiera instalación de Python en otros ordenadores, puedes usar PyInstaller:
```bash
pip install pyinstaller
pyinstaller main.spec
```
*(El archivo `main.exe` se generará en la carpeta `dist/main/`). Recuerda que aunque uses el `.exe`, el archivo `[API KEY].env` o la variable de entorno debe seguir existiendo junto a él.*
