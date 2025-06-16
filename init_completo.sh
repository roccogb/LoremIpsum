#!/bin/bash

echo "configurando proyecto Flask..."

# Crear entorno virtual
echo " Creando entorno virtual..."
python3 -m venv venv

# Activar entorno virtual
echo " Activando entorno virtual..."
source venv/bin/activate

# Instalar Flask
echo " instalando Flask..."
pip install flask

# Instalar dependencias
echo " Instalando dependencias del requirements.txt..."
pip install -r requirements.txt

# Ejecutar init_db.py
echo " Inicializando base de datos..."
python3 backend/database/init_db.py

# Ejecutar init_test_data
echo " Cargando datos de prueba..."
python3 -m tests.init_test_data

echo "Configuración completada!"
echo ""
echo "🚀 Iniciando aplicaciones..."
echo "Backend corriendo en segundo plano..."
echo "Frontend se iniciará en una nueva ventana..."

# Ejecutar backend en segundo plano
python3 backend/app.py &
BACKEND_PID=$!

# Esperar un momento para que el backend inicie
sleep 2

# Ejecutar frontend
python3 frontend/app.py &
FRONTEND_PID=$!

echo ""
echo "✅ ¡Proyecto iniciado!"
echo "📍 Backend PID: $BACKEND_PID"
echo "📍 Frontend PID: $FRONTEND_PID"
echo ""
