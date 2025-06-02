import mysql.connector               # Libreria utilizada para controlar la base de datos 

# Funcion que va a conectarse con el servidor MySQL, y en específico, con la BDD llamada 'foodyba_dbb'
def get_connection():
  return mysql.connector.connect(
    host="localhost",
    user="root",
    password="contraSQL",             # La contraseña de la base de datos varía según la configuración de cada uno. ¿Se puede hacer algo mas general?
    database="foodyba_dbb"
  )
