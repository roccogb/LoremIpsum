#!/bin/bash


# Extraer la IP de la línea "Dirección IPv4" que contiene "192.168"
IP_LOCAL=$(ipconfig | grep -a -oE "192\.168\.[0-9]+\.[0-9]+" | head -1)

# Mostrar IP
echo "🖥️  IP detectada: $IP_LOCAL"

# Validar que se obtuvo algo
if [ -z "$IP_LOCAL" ]; then
  echo "❌ No se pudo detectar la IP local. Abortando."
  exit 1
fi

# Ruta a los archivos
FRONT="frontend/app.py"
BACK="backend/app.py"

# Reemplazo con sed compatible con Git Bash (agregar backup .bak)
sed -i.bak "s/0.0.0.0/$IP_LOCAL/g" "$FRONT" && echo "✅ IP $IP_LOCAL reemplazada en $FRONT"
sed -i.bak "s/0.0.0.0/$IP_LOCAL/g" "$BACK" && echo "✅ IP $IP_LOCAL reemplazada en $BACK"




echo "🔧 Configurando proyecto Flask con Pipenv..."

# Crear entorno virtual con Pipenv e instalar Flask
echo "📦 Instalando entorno con Flask..."
pipenv install flask

# Instalar dependencias desde requirements.txt
echo "📦 Instalando dependencias adicionales del requirements.txt..."
pipenv run pip install -r requirements.txt

# Ejecutar init_db.py
echo "🛠️  Inicializando base de datos..."
pipenv run python backend/database/init_db.py

# Ejecutar init_test_data
echo "🧪 Cargando datos de prueba..."
pipenv run python -m tests.init_test_data

echo ""
echo "✅ Configuración completada!"
echo "🚀 Iniciando aplicaciones..."
echo ""

# Ejecutar backend en segundo plano
echo "🔙 Iniciando Backend (puerto 8100)..."
pipenv run python backend/app.py --port=8100 &
BACKEND_PID=$!

# Esperar un momento a que arranque el backend
sleep 2

# Ejecutar frontend en segundo plano
echo "🖥️  Iniciando Frontend (puerto 5000)..."
pipenv run python frontend/app.py --port=5000 &
FRONTEND_PID=$!

echo ""
echo "🎉 ¡Proyecto iniciado!"
echo "   🧠 Backend PID: $BACKEND_PID   (Num de proceso)"
echo "   🖼️  Frontend PID: $FRONTEND_PID (Num de proceso)"
echo ""

