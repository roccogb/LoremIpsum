from database.db import get_connection

conn = get_connection()                 # Me conecto con el servidor MySQL y a la base de datos 'foodyba_dbb'
cursor = conn.cursor()                  # Creo un cursor el cual me va a permitir ejecutar comandos

cursor.execute("""INSERT INTO usuario_comercio (nombre_usuario, email_usuario, contrasena) VALUES('Comerciante1','comercio1@gmail.com','1234');""")

cursor.execute("""INSERT INTO usuario_consumidor (nombre_usuario, email_usuario, contrasena) VALUES('Usuario1','comercio1@gmail.com','1234');""")

conn.commit()                           # Guardo los cambios realizados en la BDD
cursor.close()
conn.close()
print("Datos de prueba insertados correctamente.")
