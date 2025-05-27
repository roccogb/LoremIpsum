#!/bin/bash

# Script de instalacion de dependecias para RestauranteReviews

echo " Creando entorno virtual"
python3 -m venv venv

echo " Entorno virtual creado"

echo " Activando entorno virtual"
source venv/bin/activate

echo " Instalando dependencias desde requirements.txt"
pip install -r requirements.txt

echo " Dependencias instaladas correctamente"
