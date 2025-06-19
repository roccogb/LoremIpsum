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
                  
                  (1, 59, '/resources/uploads/comercios/don_cafe.jpg', 'Don Café', 'especialidad', 'autor', 22113344, -34.6037, -58.3816, '2025-06-15 09:00:00', 'https://doncafe.menu', 4.7, 20, 4.2, "['lunes','martes','miércoles','jueves','viernes']", "['7-11','16-18']", "['wifi','sin_gluten','apto_mascotas']"),
                  
                  (2, 60, '/resources/uploads/comercios/chimichurri_grill.jpg', 'Chimichurri Grill', 'familiar', 'clasica', 23004567, -34.6100, -58.4000, '2025-06-14 13:15:00', 'https://chimigrill.menu', 0.0, 0, 0.0, "['jueves','viernes','sábado','domingo']", "['12-15','19-23']", "['para_llevar','musica_vivo','zona_fumadores']"),
                  
                  (3, 61, '/resources/uploads/comercios/veggie_vida.jpg', 'Veggie Vida', 'tematico', 'clasica', 22119988, -34.5800, -58.3700, '2025-06-13 10:45:00', 'https://veggievida.menu', 4.9, 5, 4.2, "['lunes','miércoles','viernes']", "['12-15','19-23']", "['vegano','sin_gluten','accesible']"),
                  
                  (4, 62, '/resources/uploads/comercios/el_gourmet_oculto.jpg', 'El Gourmet Oculto', 'gourmet', 'alta_cocina', 23115678, -34.5933, -58.4100, '2025-06-12 20:00:00', 'https://gourmetoculto.link', 5.0, 1, 5.0, "['viernes','sábado']", "['19-23']", "['happy_hour','musica_vivo','wifi']"),
                  
                  (5, 63, '/resources/uploads/comercios/pollo_frito_king.jpg', 'Pollo Frito King', 'comida_rapida', 'vanguardia', 29998877, -34.5990, -58.3820, '2025-06-16 11:30:00', 'https://pollofrito.menu', 3.9, 80, 3.5, "['lunes','martes','miércoles','jueves','viernes','sábado']", "['12-15','19-23']", "['delivery','para_llevar','wifi']");
""")


############### REGUSTROS DE PRUEBA PARA LA TABLA 'reservas'
cursor.execute("""INSERT INTO reservas
                  (id_reserva,id_usr,id_comercio,nombre_bajo_reserva,email,telefono,cant_personas,fecha_reserva,solicitud_especial,estado_reserva, resenia_pendiente)
                  VALUES
                  (10, 6, 1, 'Carla Peterson','cpeterson@gmail.com',11554433, 2, '2025-06-08 21:30:50', 'Quiero poder comer todo el menu Sin Gluten', True, True),
                  (15, 10, 2, 'German Beder', 'gerchosports@gmail.com', 15000999,3, '2025-06-01 20:30:50', 'Mesa mas alejada de la gente con sillita para niños, por favor.', True, True),
                  (21, 9, 2, 'Ricardo Bochini', 'richard_el_diablo@gmail.com',11445566, 1, '2025-06-05 18:25:50', 'Una milanesa napolitana con el escudo de independiente', True, True),
                  (22, 8, 3, 'Lucia Freitas', 'lufree@hotmail.com', 15400112, 5, '2025-06-06 11:15:20', 'Una mesa bastante grande, voy con mis facuamigos!!!', True, True),                                                      
                  (34, 10, 2, 'German Beder','gerchosports@gmail.com',15000999, 5, '2025-06-12 20:15:00', 'Una mesa grande, se probarán las alas del rey.', True, True),
                  (35, 10, 2, 'German Beder','gerchosports@gmail.com',15000999, 5, '2025-06-12 20:15:00', 'Una mesa grande, se probarán las alas del rey.', True, True );
               """)

############## REGISTROS DE PRUEBA PARA LA TABLA 'resenias'
cursor.execute("""INSERT INTO resenias
                  (id_comercio,id_usr,comentario,calificacion,tiempo_de_creacion, id_reserva)
                  VALUES
                  (1, 6, 'Un lugar tranquilo y con una buena carta. Excelente para una merienda con tu pareja', 4, '2025-06-01 22:15:00', 10),
                  (5, 10, 'Espantoso el lugar, no me alcanzan los caracteres para describir mi experiencia. Una de las famosas alas del rey que le dieron a mi amigo lo tuvo en el baño 3 hs, con eso te digo todo.', 1, '2025-06-05 19:00:00', 34),
                  (3, 9, 'Las mejores milanesas que probe en mi vida', 5, '2025-06-08 22:15:00', 21),
                  (5, 10, 'Excelente. Mis felicitaciones al maestro de la parrilla', 5, '2025-06-06 13:00:00', 15),
                  (3,8,'Buen lugar, mis amigos la pasaron bien aunque la comida no es bastante buena.',3, '2025-05-20 16:30:00', 22);
                """)

conn.commit()                           # Guardo los cambios realizados en la BDD
cursor.close()
conn.close()

print("Datos de prueba insertados correctamente.")