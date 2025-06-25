# Script para eliminar las tablas de la BDD. No tiene mucha utilidad, es para hacer pruebas mas que nada(se elimina)
from backend.database import get_connection

conn=get_connection()
cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS resenias;")
cursor.execute("DROP TABLE IF EXISTS reservas;")
cursor.execute("DROP TABLE IF EXISTS favoritos;")
cursor.execute("DROP TABLE IF EXISTS comercios;")
cursor.execute("DROP TABLE IF EXISTS usuario_comercio;")
cursor.execute("DROP TABLE IF EXISTS usuario_consumidor;")

conn.commit()
cursor.close()
conn.close()

print("Tablas eliminadas con éxito")