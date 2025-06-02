# Este modulo va a crear la BDD bajo el nombre de 'foodyba_dbb'
import mysql.connector

# Abro el archivo que contiene todas las sentencias SQL para crear la BDD
with open("init_db.sql") as f:
  sql = f.read()

# Me conecto con el servidor MySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="contraSQL",
)

cursor = conn.cursor()                    # Creo un cursor. Este mismo me va a permitir ejecutar comando SQL

# Recorro cada sentencia SQL del archivo previamente abierto. A cada una se le va a aplicar un split en el caracter ';'
for statement in sql.split(";"):
  if statement.strip():
    cursor.execute(statement)             # Ejecuto la sentencia SQL
    conn.commit()                         # Guardo de forma permanente los cambios realizados en la sesión. Si no se ejecuta 'commit' los cambios que se hayan hecho no se guardaran
    print("Statement executed")

cursor.close()                            # Cierro el cursor
conn.close()                              # Cierro la conexión con el servidor MySQL
