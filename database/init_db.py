# Este modulo va a crear la BDD bajo el nombre de 'foodyba_dbb'
import mysql.connector                                                        # Libreria que me va a permitir acceder a BDD MySQL

# Abro el archivo que contiene todas las sentencias SQL para crear la BDD
with open("init_db.sql") as f:
  sql = f.read()

# Me conecto con el servidor MySQL.
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="contraSQL",
)

cursor = conn.cursor()                    # Creo un cursor. Este mismo me va a permitir ejecutar comando SQL

# Meto una sentencia 'try/except' acá para asi poder prevenir cualquier tipo de error en la ejecución del script
try:
  # Recorro cada sentencia SQL del archivo previamente abierto. A cada una se le va a aplicar un split en el caracter ';' para asi poder ejecutarlas.
  # Esto es necesario realizarlo ya que, el archivo abierto viene en el siguiente formato
  # CREATE TABLE tabla_A();CREATE TABLE tabla_B();......
  # Tras aplicar el split-> ["CREATE TABLE tabla_A()","CREATE TABLE tabla_B()",...]
  for statement in sql.split(";"):
    if statement.strip():
      cursor.execute(statement)             # Ejecuto la sentencia SQL
      conn.commit()                         # Guardo de forma permanente los cambios realizados en la sesión. Si no se ejecuta 'commit' los cambios que se hayan hecho no se guardaran
      print("Sentencia SQL ejecutada")      # Mensaje para confirmar que la sentencia se ejecutó con éxito     
except Exception as e:
  # Si ocurre algun error durante el 'try' se va a mostrar el siguiente msj
  print("Error al inicializar la base de datos: ", e)
finally:
  # Bloque que siempre se va a ejecutar.
  cursor.close()                            # Cierro el cursor
  conn.close()                              # Cierro la conexión con el servidor MySQL
