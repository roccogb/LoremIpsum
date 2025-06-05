# Script para insertar datos en las BDD
from backend.database.db import get_connection

conn = get_connection()                 # Me conecto con el servidor MySQL y a la base de datos 'foodyba_dbb'
cursor = conn.cursor()                  # Creo un cursor el cual me va a permitir ejecutar comandos

# Agrego un usuario del tipo comercio
cursor.execute("""INSERT INTO usuario_comercio (id_usr_comercio,nombre_usuario,DNI,CUIT,email_usuario, contrasena) VALUES(2,'Comerciante1', 12305555, 20113456883,'comercio1@gmail.com','1234');""")
cursor.execute("""INSERT INTO usuario_comercio (id_usr_comercio,nombre_usuario,DNI,CUIT,email_usuario, contrasena) VALUES(3,'Apu Nahasapeemapetilon', 45202333, 20442013668,'dandydelosprecios@outlook.com','5678');""")
# Agrego un usuario del tipo consumidor
cursor.execute("""INSERT INTO usuario_consumidor (id_usr,nombre_apellido,usuario, email_usuario, contrasena, numero_telefono, cant_reservas_canceladas) VALUES(4, 'Juansito Lopez','Usuario1','comercio1@gmail.com','1234', 20331122, 15);""")
# Agrego comercios
cursor.execute("""INSERT INTO comercios (id_comercio,id_usr_comercio, nombre_comercio, categoria, tipo_de_cocina, telefono, latitud, longitud, tiempo_de_creacion, pdf_menu_link, calificacion, dias, horarios, etiquetas) VALUES (20,2,'Super comercio', 'Gourmet', 'Chino', '2000-4444',20.555481, -35.43334, '2025-05-25 17:58:20', 'asasdadada', 5.5, 'Martes-Viernes','17:00-19:00', '[vegano,vegetariano,delivery]')""")
cursor.execute("""INSERT INTO comercios (id_comercio,id_usr_comercio, nombre_comercio, categoria, tipo_de_cocina, telefono, latitud, longitud, tiempo_de_creacion, pdf_menu_link, calificacion, dias, horarios, etiquetas) VALUES (15,3,'Kwik-E-Mart', 'Especialidad', 'Cocina de vanguardia', '1111-2222',-54.6333, 50.5050, '2025-06-03 21:38:15', 'https://kwikemart4.mitiendanube.com/', 5,'Lunes-Viernes', '24h', '[pet-friendly,vegano,accesible]')""")

conn.commit()                           # Guardo los cambios realizados en la BDD
cursor.close()
conn.close()
print("Datos de prueba insertados correctamente.")
