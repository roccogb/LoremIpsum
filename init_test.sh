#!/bin/bash

# Detectar IP local de forma robusta
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    IP_LOCAL=$(hostname -I | awk '{print $1}')
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    IP_LOCAL=$(ipconfig | grep -oE "IPv4.*192\.168\.[0-9]+\.[0-9]+" | grep -oE "192\.168\.[0-9]+\.[0-9]+" | head -1)
else
    echo "Sistema no reconocido. Ingresá la IP manualmente:"
    read -p "IP local: " IP_LOCAL
fi

# Fallback manual si no se detectó nada
if [ -z "$IP_LOCAL" ]; then
  echo "No se pudo detectar la IP local automáticamente."
  read -p "Ingresala manualmente (ej: 192.168.0.105): " IP_LOCAL
fi

echo "IP detectada: $IP_LOCAL"

FRONT="frontend/app.py"
BACK="backend/app.py"

# Guardar IP para generación de QR
echo "IP_LOCAL=$IP_LOCAL" > backend/ip_config.env
echo "IP guardada en backend/ip_config.env"

# Pedir contraseña MySQL
read -s -p "Ingresá la nueva contraseña de MySQL: " CONTRA_MYSQL
echo ""
echo "Reemplazando contraseña en archivos de base de datos..."

for FILE in backend/database/db.py backend/database/init_db.py; do
  if [ -f "$FILE" ]; then
    sed -i.bak "s/DB_PASSWORD = \".*\"/DB_PASSWORD = \"$CONTRA_MYSQL\"/" "$FILE"
    echo "Contraseña actualizada en $FILE"
  fi
done

# Reemplazar IP en app.py
echo ""
echo "Reemplazando IP en archivos app.py..."
sed -i.bak "s/0.0.0.0/$IP_LOCAL/g" "$FRONT" && echo "IP reemplazada en $FRONT"
sed -i.bak "s/0.0.0.0/$IP_LOCAL/g" "$BACK" && echo "IP reemplazada en $BACK"

# Instalar entorno y dependencias
echo ""
echo "Instalando entorno virtual y dependencias..."
export PIPENV_IGNORE_VIRTUALENVS=1
pipenv install flask
pipenv run pip install -r requirements.txt

# Inicializar base de datos
echo ""
echo "Inicializando base de datos..."
pipenv run python -m backend.database.init_db

# Cargar datos de prueba
echo "Cargando datos de prueba..."
pipenv run python -m tests.init_test_data

# Iniciar servidores
echo ""
echo "Iniciando servidores..."

echo "Backend (8100)..."
pipenv run python -m backend.app &
BACKEND_PID=$!
sleep 2

echo "Frontend (8200)..."
pipenv run python -m frontend.app &
FRONTEND_PID=$!

echo ""
echo "Proyecto iniciado correctamente"
echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
