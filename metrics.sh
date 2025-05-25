#!/bin/bash
echo "Ejecutando pruebas y cobertura..."
coverage run manage.py test
coverage report
coverage html

echo "Analizando complejidad ciclomática..."
radon cc . -s -a > radon_report.txt

echo "Chequeando calidad de código..."
flake8 . > flake8_report.txt

echo "Chequeando seguridad de dependencias..."
safety check > safety_report.txt

echo "Contando líneas de código..."
cloc . > cloc_report.txt

echo "¡Listo! Revisa los archivos generados para los resultados."
