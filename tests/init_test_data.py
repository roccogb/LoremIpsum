from backend.database.db import get_connection

conn = get_connection()                 # Me conecto con el servidor MySQL y a la base de datos 'foodyba_dbb'
cursor = conn.cursor()                  # Creo un cursor el cual me va a permitir ejecutar comandos

cursor.execute("""INSERT INTO usuario_comercio (id_usr_comercio,nombre_usuario, email_usuario, contrasena) VALUES(2,'Comerciante1','comercio1@gmail.com','1234');""")
cursor.execute("""INSERT INTO usuario_consumidor (id_usr,nombre_usuario, email_usuario, contrasena) VALUES(4,'Usuario1','comercio1@gmail.com','1234');""")
cursor.execute("""INSERT INTO comercios (id_comercio,id_usr_comercio, nombre_comercio, categoria, tipo_de_cocina, telefono, ubicacion, tiempo_de_creacion, pdf_menu_link, calificacion, horarios) VALUES (20,2,'Super comercio', 'Gourmet', 'Chino', '2000-4444','Avenida Siempreviva', '2025-05-25 17:58:20', 'asasdadada', 5.5, '17:00-19:00' )""")

conn.commit()                           # Guardo los cambios realizados en la BDD
cursor.close()
conn.close()
print("Datos de prueba insertados correctamente.")

#20 id_comercio
#2 id_usr_comercio

