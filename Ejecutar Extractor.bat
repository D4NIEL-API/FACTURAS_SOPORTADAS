@echo off
REM Script sencillo para ejecutar la aplicacion de extraccion de facturas

echo Inicializando Extractor de Facturas...
echo.

REM Comprueba si existe el ejecutable compilado
if exist "dist\main\main.exe" (
    echo Ejecutando version precompilada...
    "dist\main\main.exe"
) else (
    REM Si no existe el ejecutable, intenta usar Python directamente
    echo Ejecutando codigo fuente con Python...
    python main.py
)

echo.
pause
