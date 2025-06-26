import mysql.connector               # Libreria que me va a permitir acceder a BDD MySQL

def get_connection():
  return mysql.connector.connect(
    host="localhost",
    user="root",
    password="CONTRASQL",            
    database="foodyba_dbb"
  )
