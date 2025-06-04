from db import get_connection
try:
  conn = get_connection()
  cursor = conn.cursor()
  cursor.execute("SHOW TABLES;")
  tablas = cursor.fetchall()

  print("Tablas de la bd")
  for t in tablas:
    print("-",t[0])
except Exeption as e:
  print("Error al conectar o consultar",e)
finally:
  cursor.close()
  conn.close()
