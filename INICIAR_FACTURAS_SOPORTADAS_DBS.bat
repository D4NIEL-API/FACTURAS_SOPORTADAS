@echo off
REM Script sencillo para ejecutar Facturas Soportadas DBS

echo Inicializando Facturas Soportadas DBS...
echo.

REM Comprueba si existe el ejecutable compilado
if exist "[NO BORRAR] Archivos funcionamiento\dist\main\main.exe" (
    echo Ejecutando version precompilada...
    cd "[NO BORRAR] Archivos funcionamiento"
    "dist\main\main.exe"
) else (
    REM Si no existe el ejecutable, intenta usar Python directamente
    echo Ejecutando codigo fuente con Python...
    cd "[NO BORRAR] Archivos funcionamiento"
    python main.py
)

echo.
pause
