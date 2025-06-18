import mysql.connector               # Libreria que me va a permitir acceder a BDD MySQL

# Funcion que va a conectarse con el servidor MySQL, y en específico, con la BDD llamada 'foodyba_dbb'.
# El objeto que retorne esta funcion va a representar la conexión con el servidor y la BDD. Con el mismo se va a poder ejecutar consultas, crear cursores, gestionar transacciones de data con la BDD,etc
def get_connection():
  return mysql.connector.connect(
    host="localhost",
    user="root",
    password="contraSQL1",             # La contraseña de la base de datos varía según la configuración de cada uno. ¿Se puede hacer algo mas general?
    database="foodyba_dbb"
  )
