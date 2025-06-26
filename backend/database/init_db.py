# Este modulo va a crear la BDD bajo el nombre de 'foodyba_dbb'
import mysql.connector                                                      
import os

# Ruta al archivo SQL desde la misma carpeta que este script
sql_path = os.path.join(os.path.dirname(__file__), "init_db.sql")

# Abro el archivo que contiene todas las sentencias SQL para crear la BDD
with open(sql_path) as f:
    sql = f.read()
  
# Me conecto con el servidor MySQL.
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="CONTRASQL"
)

cursor = conn.cursor()                    

# Meto una sentencia 'try/except' acá para asi poder prevenir cualquier tipo de error en la ejecución del script
try:
  for statement in sql.split(";"):
    if statement.strip():
      cursor.execute(statement)             
      conn.commit()                         
      print("Sentencia SQL ejecutada")      
except Exception as e:
  print("Error al inicializar la base de datos: ", e)
finally:
  cursor.close()                           
  conn.close()                              
