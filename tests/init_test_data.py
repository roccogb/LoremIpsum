# Script de prueba para insertar datos en la BDD
from backend.database.db import get_connection

conn = get_connection()                 # Me conecto con el servidor MySQL y a la base de datos 'foodyba_dbb'
cursor = conn.cursor()                  # Creo un cursor el cual me va a permitir ejecutar comandos

################# REGISTROS DE PRUEBA PARA LA TABLA 'usuario_comercio'
cursor.execute("""INSERT INTO usuario_comercio 
               (id_usr_comercio,nombre_apellido, DNI,CUIT,email_usuario, contrasena) 
               VALUES 
               (2,'Walter White', 12305555, 20123055553,'heisenberg@hotmail.com',1234),
               (3,'Apu Nahasapeemapetilon', 45202333, 20442013668,'dandydelosprecios@outlook.com',5678),
               (4,'Sabrina Carpenter', 43102113, 20431021135,'sc_gamer2001@outlook.com','ABC123'),
               (5,'Dua Lipa', 40444252, 15404442527,'dlgutierrez@gmail.com','ABC456');""")

################ REGISTROS DE PRUEBA PARA LA TABLA 'usuario_consumidor'
cursor.execute("""INSERT INTO usuario_consumidor 
                  (id_usr,nombre_apellido, usuario, email_usuario, contrasena, numero_telefono, cant_reservas_canceladas) 
                  VALUES
                  (1, 'Matias Sapienza', 'msspza', 'matikpo2002@live.com','contraseña', 22113030, 0),
                  (2, 'Angela Leiva', 'AL777', 'negritacuartetera@gmail.com', 'ABC333', 11033030, 5),
                  (3, 'Sasha Ferro', 'ruggeri_chupapija', 'sashamiau@outlook.com', 'DEF888', 15150233, 20),
                  (4, 'Kevin Lomonaco','SeñorDELanoche','guarachita@hotmail.com','1234', 20335555, 15);""")

################ REGISTROS DE PRUEBA PARA LA TABLA 'comercios'
cursor.execute("""INSERT INTO comercios
                  (id_comercio,id_usr_comercio, nombre_comercio, categoria, tipo_de_cocina, telefono, latitud, longitud, tiempo_de_creacion, pdf_menu_link, calificacion, dias, horarios, etiquetas)
                  VALUES 
                  (1, 4, 'Cafe Expresso', 'Especialidad', 'Cocina de autor', 99991111, 20.8501, -51.9987, '2015-05-22 10:50:10', 'https://www.cafemartinez.com/?srsltid=AfmBOooWV1qsi0jC_PbWjnW7bbE3NRQQnn7ZKZfjLTSypqMci67UFitx',4.8, 'Lunes-Viernes', '08:00-23:00', '[pet-friendly, wifi, terraza]'),
                  (99, 5, 'La Parrilla de Dua', 'Familiar', 'Cócina clasica', 12123030, -34.88412, -58.35581, '2002-09-22 11:35:55', 'https://www.facebook.com/groups/580812462862561/posts/1657688688508261/', 5, 'Lunes-Viernes', '08:00-01:00', '[accesible,delivery,para_llevar,familiar]'),
                  (15,3,'Kwik-E-Mart', 'Especialidad', 'Cocina de vanguardia', 11112222,-54.6333, 50.5050, '2025-06-03 21:38:15', 'https://kwikemart4.mitiendanube.com/', 5,'Lunes-Viernes', '24h', '[pet-friendly,vegano,accesible]'),
                  (20,2,'Super comercio', 'Gourmet', 'Chino', 20004444,20.555481, -35.43334, '2025-05-25 17:58:20', 'asasdadada', 5.5, 'Martes-Viernes','17:00-19:00', '[vegano,vegetariano,delivery]');""")

############### REGUSTROS DE PRUEBA PARA LA TABLA 'reservas'
cursor.execute("""INSERT INTO reservas
                  (id_reserva,id_usr,id_comercio,nombre_bajo_reserva,email,telefono,cant_personas,fecha_reserva,solicitud_especial,estado_reserva)
                  VALUES
                  (10, 4, 15, 'Kevin Lomonaco','guarachita@hotmail.com',20335555, 2, '2025-06-08 21:30:50', 'Buena musica...', False),
                  (15, 1, 99, 'Matias Sapienza', 'matikpo2002@live.com', 22113030,4, '2025-06-01 20:30:50', 'Punto de coccion:La carne tiene que decir mu', True),
                  (21, 3, 1, 'Sasha Ferro', 'sashamiau@outlook.com',15150233, 1, '2025-06-05 18:25:50', 'El mejor cafe con leche posible', False),
                  (22, 1, 99, 'Matias Sapienza', 'matikpo2002@live.com', 22113030, 1, '2025-06-06 11:15:20', 'El mejor chinchulin disponible', True);""")

conn.commit()                           # Guardo los cambios realizados en la BDD
cursor.close()
conn.close()

print("Datos de prueba insertados correctamente.")
