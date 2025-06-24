#!/bin/bash

# 🎛️ Script de inicialización automática - FoodyBA

# 1. Detectar IP local
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    IP_LOCAL=$(hostname -I | awk '{print $1}')
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    IP_LOCAL=$(ipconfig | grep -a -oE "192\.168\.[0-9]+\.[0-9]+" | head -1)
else
    echo "⚠️ Sistema no reconocido. Ingresá la IP manualmente:"
    read -p "IP local: " IP_LOCAL
fi

echo "🖥️  IP detectada: $IP_LOCAL"

if [ -z "$IP_LOCAL" ]; then
  echo "❌ No se pudo detectar la IP local. Abortando."
  exit 1
fi

FRONT="frontend/app.py"
BACK="backend/app.py"

# 2. Pedir contraseña de MySQL
read -s -p "🔐 Ingresá la nueva contraseña de MySQL: " CONTRA_MYSQL
echo ""
echo "🛠️  Reemplazando contraseña en archivos de base de datos..."

for FILE in backend/database/db.py backend/database/init_db.py; do
  if [ -f "$FILE" ]; then
    sed -i.bak "s/DB_PASSWORD = \".*\"/DB_PASSWORD = \"$CONTRA_MYSQL\"/" "$FILE"
    echo "✅ Contraseña actualizada en $FILE"
  fi
done

# 3. Reemplazar IP en app.py
echo ""
echo "🌐 Reemplazando IP en archivos app.py..."
sed -i.bak "s/0.0.0.0/$IP_LOCAL/g" "$FRONT" && echo "✅ IP reemplazada en $FRONT"
sed -i.bak "s/0.0.0.0/$IP_LOCAL/g" "$BACK" && echo "✅ IP reemplazada en $BACK"

# 4. Instalar entorno y dependencias
echo ""
echo "📦 Instalando entorno virtual..."
pipenv install flask
pipenv run pip install -r requirements.txt

# 5. Inicializar base de datos
echo ""
echo "🧱 Inicializando base de datos..."
pipenv run python backend/database/init_db.py

echo "🧪 Cargando datos de prueba..."
pipenv run python -m tests.init_test_data

# 6. Levantar servidores
echo ""
echo "🚀 Iniciando servidores..."

echo "🔙 Backend (8100)..."
pipenv run python backend/app.py &
BACKEND_PID=$!
sleep 2

echo "🖥️  Frontend (8200)..."
pipenv run python frontend/app.py &
FRONTEND_PID=$!

echo ""
echo "🎉 ¡Proyecto iniciado correctamente!"
echo "   🧠 Backend PID: $BACKEND_PID"
echo "   🖼️  Frontend PID: $FRONTEND_PID"
echo ""
