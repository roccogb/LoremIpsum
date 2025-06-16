
#!/bin/bash

echo "Configurando proyecto Flask..."

#crear entorno virtual
echo "Creando entorno virtual..."
python3 -m venv venv

#ctivar entorno virtual
echo "Activando entorno virtual..."
source venv/bin/activate

# Instalar Flask
echo " Instalando Flask..."
pip install flask

# Instalar dependencias
echo "Instalando dependencias del requirements.txt..."
pip install -r requirements.txt

# ejecutar init_db.py
echo "Inicializando base de datos..."
python3 backend/database/init_db.py

# ejecutar init_test_data
echo "Cargando datos de prueba..."
python3 -m tests.init_test_data

echo "Configuración completada!"
echo "Iniciando aplicaciones..."
echo "Backend corriendo en segundo plano..."
echo "Frontend se iniciará en una nueva ventana..."

# ejecutar backend en segundo plano
python3 backend/app.py &
BACKEND_PID=$!
