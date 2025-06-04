from db import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""INSERT INTO usuario_comercio (nombre_usuario, email_usuario, contrasena) VALUES('Comerciante1','comercio1@gmail.com','1234');""")

cursor.execute("""INSERT INTO usuario_final (nombre_usuario, email_usuario, contrasena) VALUES('Usuario1','comercio1@gmail.com','1234');""")

conn.commit()
cursor.close()
conn.close()
print("Datos de prueba insertados correctamente.")
