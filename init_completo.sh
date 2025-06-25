#!/bin/bash

#  Detecta IP local
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    IP_LOCAL=$(hostname -I | awk '{print $1}')
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    IP_LOCAL=$(ipconfig | grep -a -oE "192\.168\.[0-9]+\.[0-9]+" | head -1)
else
    echo " Sistema no reconocido. Ingresá la IP manualmente:"
    read -p "IP local: " IP_LOCAL
fi

echo "  IP detectada: $IP_LOCAL"

if [ -z "$IP_LOCAL" ]; then
  echo " No se pudo detectar la IP local. Abortando."
  exit 1
fi

FRONT="frontend/app.py"
BACK="backend/app.py"

# Pedir contraseña de MySQL
read -s -p " Ingresá la nueva contraseña de MySQL: " CONTRA_MYSQL
echo ""
echo "  Reemplazando contraseña en archivos de base de datos..."

for FILE in backend/database/__init__.py backend/database/init_db.py; do
  if [ -f "$FILE" ]; then
    sed -i.bak "s/CONTRASQL/$CONTRA_MYSQL/g" "$FILE"
    echo " Contraseña actualizada en $FILE"
  fi
done

# Reemplazar IP en app.py
echo ""
echo " Reemplazando IP en archivos app.py..."
sed -i.bak "s/0.0.0.0/$IP_LOCAL/g" "$FRONT" && echo " IP reemplazada en $FRONT"
sed -i.bak "s/0.0.0.0/$IP_LOCAL/g" "$BACK" && echo " IP reemplazada en $BACK"

# Reemplazar IP en el link del QR
echo ""
echo "Reemplazando IP en el link del QR"
sed -i.bak "s/9.9.9.9/$IP_LOCAL/g" "backend/reservas/routes.py" && echo " IP reemplazada en el QR"

echo ""
echo " Instalando entorno virtual..."
pipenv install flask
pipenv run pip install -r requirements.txt


echo ""
echo " Inicializando base de datos..."
pipenv run python -m backend.database.init_db

echo " Cargando datos de prueba..."
pipenv run python -m tests.init_test_data

echo ""
echo " Iniciando servidores..."

echo " Backend (8100)..."
pipenv run python -m backend.app &
BACKEND_PID=$!
sleep 2

echo "  Frontend (8200)..."
pipenv run python -m frontend.app &
FRONTEND_PID=$!

echo ""
echo " ¡Proyecto iniciado correctamente!"
echo "    Backend PID: $BACKEND_PID"
echo "    Frontend PID: $FRONTEND_PID"
echo ""
