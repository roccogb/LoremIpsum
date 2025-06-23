# Script de prueba para insertar datos en la BDD
from backend.database.db import get_connection

conn = get_connection()                 
cursor = conn.cursor()                  

################# REGISTROS DE PRUEBA PARA LA TABLA 'usuario_comercio'
cursor.execute("""INSERT INTO usuario_comercio 
               (id_usr_comercio, nombre_apellido, DNI, CUIT, email_usuario, contrasena, fecha_creacion) 
               VALUES 
               (59, 'Andrés Iniesta', 30111222, 20301112223, 'ainiesta@gmail.com', 'golazo123', '2025-06-12'),
               (60, 'Lisa Simpson', 22334455, 27223344556, 'lisamusica@springfield.com', 'saxolove4', '2025-06-13'),
               (61, 'Pedro Pascal', 35998221, 20359982213, 'mandolorian@hotmail.com', 'babyY0da!', '2025-06-14'),
               (62, 'Sandra Bullock', 40112333, 23401123334, 'sandra.b@cine.com', 'speed1994', '2025-06-15'),
               (63, 'Joaquín Sabina', 30011211, 25300112112, 'jsabina@poesia.net', 'y17picon', '2025-06-16');""")

################ REGISTROS DE PRUEBA PARA LA TABLA 'usuario_consumidor'
cursor.execute("""INSERT INTO usuario_consumidor 
                  (id_usr, nombre_apellido, usuario, email_usuario, contrasena, fecha_creacion, numero_telefono, cant_reservas_canceladas) 
                  VALUES
                  (6, 'Carla Peterson', 'CarlaP', 'cpeterson@gmail.com', 'telenovela123', '2025-06-17', 11554433, 2),
                  (7, 'Tobías Merlo', 'tobix', 'tobimerlo@outlook.com', 'pass456', '2025-06-18', 11223344, 1),
                  (8, 'Lucía Freitas', 'LuFree', 'lufree@hotmail.com', 'freedom!', '2025-06-15', 15400112, 0),
                  (9, 'Ricardo Bochini', 'maestro_rojo', 'richard_el_diablo@gmail.com', 'rojox100pre', '2025-06-13', 11445566, 8),
                  (10, 'German Beder', 'gbeder', 'gerchosports@gmail.com', 'oliviaquerida88', '2025-06-14', 15000999, 0);""")


################ REGISTROS DE PRUEBA PARA LA TABLA 'comercios'
cursor.execute("""INSERT INTO comercios
                  (id_comercio,id_usr_comercio, ruta_imagen,nombre_comercio, categoria, tipo_cocina, telefono, latitud, longitud, tiempo_de_creacion, pdf_menu_link, promedio_calificacion, cantidad_resenias, ranking_ponderado, dias, horarios, etiquetas)
                  VALUES 
                  (1, 59, '/resources/uploads/comercios/don_cafe.jpg', 'Don Café', 'especialidad', 'autor', 22113344, -34.6037, -58.3816, '2025-06-15 09:00:00', 'https://doncafe.menu', 4.7, 20, 4.2, "['lunes','martes','miércoles','jueves','viernes']", "['7-10','16-18']", "['wifi','sin_gluten','apto_mascotas']"),
                  (2, 60, '/resources/uploads/comercios/chimichurri_grill.jpg', 'Chimichurri Grill', 'familiar', 'clasica', 23004567, -34.6100, -58.4000, '2025-06-14 13:15:00', 'https://chimigrill.menu', 0.0, 0, 0.0, "['jueves','viernes','sábado','domingo']", "['12-15','20-23']", "['para_llevar','musica_vivo','zona_fumadores']"),                  
                  (3, 61, '/resources/uploads/comercios/veggie_vida.jpg', 'Veggie Vida', 'tematico', 'clasica', 22119988, -34.5800, -58.3700, '2025-06-13 10:45:00', 'https://veggievida.menu', 4.9, 5, 4.2, "['lunes','miércoles','viernes']", "['12-15','20-23']", "['vegano','sin_gluten','accesible']"),
                  (4, 62, '/resources/uploads/comercios/el_gourmet_oculto.jpg', 'El Gourmet Oculto', 'gourmet', 'alta_cocina', 23115678, -34.5933, -58.4100, '2025-06-12 20:00:00', 'https://gourmetoculto.link', 5.0, 1, 5.0, "['viernes','sábado']", "['20-23']", "['happy_hour','musica_vivo','wifi']"),
                  (5, 63, '/resources/uploads/comercios/pollo_frito_king.jpg', 'Pollo Frito King', 'comida_rapida', 'vanguardia', 29998877, 36.72995945020064, -4.547759190890471, '2025-06-16 11:30:00', 'https://gaskins-fried-chicken.es/#men%C3%BA', 3.9, 80, 3.5, "['lunes','martes','miércoles','jueves','viernes','sábado']", "['12-15','20-23']", "['delivery','para_llevar','wifi']");
""")


conn.commit()                           # Guardo los cambios realizados en la BDD
cursor.close()
conn.close()

print("Datos de prueba insertados correctamente.")