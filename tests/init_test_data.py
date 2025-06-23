# Script de prueba para insertar datos en la BDD
from backend.database.db import get_connection

conn = get_connection()                 
cursor = conn.cursor()                  

################# REGISTROS DE PRUEBA PARA LA TABLA 'usuario_comercio'
cursor.execute("""INSERT INTO usuario_comercio 
                 (id_usr_comercio, nombre_apellido, DNI, CUIT, email_usuario, contrasena, fecha_creacion)
                 VALUES
                 (64, 'Mariana Fabbiani', 32111222, 27321112221, 'mfabbiani@canal.com', 'tvshow321', '2025-06-16'),
                 (65, 'Diego Torres', 34123123, 27341231234, 'dtorres@musica.com', 'coloresperanza', '2025-06-16'),
                 (66, 'Natalie Portman', 32199900, 27321999001, 'n.portman@cine.org', 'blackSwan22', '2025-06-17'),
                 (67, 'Juan Román Riquelme', 28777222, 20287772223, 'jrr10@futbol.ar', 'enganche10', '2025-06-17'),
                 (68, 'Emma Watson', 31311311, 27313113112, 'emma.w@hogwarts.uk', 'hermione22', '2025-06-17'),                    
                 (69, 'Carlos Tévez', 30010101, 20300101012, 'carlitos@boca.ar', 'apache123', '2025-06-18'),
                 (70, 'Lionel Messi', 31123321, 20311233211, 'lmessi@inter.miami', 'goat10', '2025-06-18'),
                 (71, 'Frida Kahlo', 29992211, 27299922112, 'frida@arte.mx', 'cejaunic4', '2025-06-18'),
                 (72, 'Sofía Vergara', 32211333, 27322113334, 'svergara@modern.com', 'gloria2025', '2025-06-19'),
                 (73, 'Keanu Reeves', 31444444, 27314444445, 'neo@matrix.net', 'whoa123', '2025-06-19'),
                 (74, 'Gustavo Cerati', 30303030, 27303030301, 'cerati@rock.com', 'mequedo', '2025-06-19'),
                 (75, 'Amy Winehouse', 31999988, 27319999881, 'amy@jazz.uk', 'back2black', '2025-06-20'),
                 (76, 'Mafalda Quino', 31122334, 27311223345, 'mafiquino@revista.com', 'nopolitics', '2025-06-20'),
                 (77, 'Stephen Hawking', 27778888, 27277788889, 'hawking@cosmos.uk', 'time4space', '2025-06-20'),
                 (78, 'Dua Lipa', 32987654, 27329876541, 'dualipa@pop.com', 'futureNostalgia', '2025-06-20'),
                 (79, 'Michael Bublé', 32887766, 27328877662, 'mbuble@crooner.ca', 'canada123', '2025-06-20'),
                 (80, 'Jorge Drexler', 32775511, 27327755113, 'jdrexler@musica.uy', 'guitarra2025', '2025-06-20'),
                 (81, 'Penélope Cruz', 32445566, 27324455667, 'pcruz@cine.es', 'alma2025', '2025-06-20'),
                 (82, 'Elon Musk', 30101010, 20301010101, 'elon@tesla.space', 'marsbound', '2025-06-20'),
                 (83, 'Shakira Mebarak', 30012345, 27300123456, 'shakira@music.co', 'hipsdontlie', '2025-06-20');""")   

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
                    (6, 64, '/resources/uploads/comercios/pizza_roma.jpg', 'Pizza Roma', 'familiar', 'alta_cocina', 22334455, -34.769865, -58.396290, '2025-06-16 13:00:00', 'https://www.instagram.com/pizzaromaoficial/?hl=es', 4.3, 15, 4.1, "['lunes','martes','miércoles']", "['12-15','20-23']", "['delivery','wifi']"),
                    (7, 65, '/resources/uploads/comercios/tango_bistro.jpg', 'Tango Bistro', 'tematico', 'tecnico_conceptual', 22334456, -34.611767, -58.374664, '2025-06-16 18:00:00', 'https://querandi.com.ar/restaurante-tango/', 4.0, 22, 3.9, "['jueves','viernes','sábado']", "['20-23']", "['musica_vivo','zona_fumadores']"),
                    (8, 66, '/resources/uploads/comercios/luna_sushi.jpeg', 'Luna Sushi', 'gourmet', 'vanguardia', 22334457, -35.537004, -71.486251, '2025-06-17 12:00:00', 'https://www.instagram.com/luna.sushi/?hl=es', 4.8, 10, 4.5, "['lunes','miércoles','viernes']", "['12-15']", "['wifi','sin_gluten']"),
                    (9, 67, '/resources/uploads/comercios/moliere_cafe.jpg', 'Molieré Café', 'especialidad', 'autor', 22334458, -34.597224, -58.378321, '2025-06-17 09:00:00', 'https://www.instagram.com/moliereesmeralda/', 4.1, 18, 3.8, "['lunes','martes','jueves']", "['7-10','16-18']", "['apto_mascotas','wifi']"),
                    (10, 68, '/resources/uploads/comercios/casa_madre.jpg', 'Casa Madre', 'familiar', 'clasica', 22334459, -34.614266, -68.335428, '2025-06-17 20:00:00', 'https://www.instagram.com/casamadre2024/', 3.7, 8, 3.4, "['miércoles','viernes','domingo']", "['12-15','20-23']", "['para_llevar']"),
                    (11, 69, '/resources/uploads/comercios/burger_heaven.jpg', 'Burger Heaven', 'comida_rapida', 'alta_cocina', 22334460, 40.623391, -73.730198, '2025-06-18 13:45:00', 'https://burgerheaven.com/lander', 4.6, 30, 4.4, "['todos']", "['12-15','20-23']", "['delivery','wifi','zona_fumadores']"),
                    (12, 70, '/resources/uploads/comercios/parrilla_don_julio.jpg', 'Parrilla Don Julio', 'gourmet', 'tecnico_conceptual', 22334461, -34.586292, -58.424277, '2025-06-18 20:30:00', 'https://www.parrilladonjulio.com/', 5.0, 50, 4.9, "['viernes','sábado','domingo']", "['20-23']", "['musica_vivo','happy_hour']"),
                    (13, 71, '/resources/uploads/comercios/green_garden.jpg', 'Green Garden', 'tematico', 'vanguardia', 22334462, -34.918360, -57.954699, '2025-06-18 10:15:00', 'https://www.instagram.com/greengardenlaplata?igsh=cm40Zm91YWtqMWxw', 4.4, 12, 4.0, "['lunes','martes','jueves']", "['12-15']", "['sin_gluten','vegano','apto_mascotas']"),
                    (14, 72, '/resources/uploads/comercios/arepa_land.jpeg', 'Arepa Club', 'familiar', 'autor', 22334463, -34.602450, -58.442283, '2025-06-19 12:00:00', 'https://www.instagram.com/arepasclub.ar?igsh=ODBmbnRtNzJ6M2Fk', 3.9, 5, 3.6, "['lunes','miércoles','sábado']", "['12-15','20-23']", "['para_llevar']"),
                    (15, 73, '/resources/uploads/comercios/food_truck_bay.jpeg', 'Food Truck Bay', 'comida_rapida', 'clasica', 22334464, -34.6022, -58.3801, '2025-06-19 11:30:00', 'https://www.instagram.com/foodtruckargentina/?hl=es', 4.2, 20, 3.9, "['jueves','viernes','sábado']", "['12-15','20-23']", "['delivery','wifi']"),
                    (16, 74, '/resources/uploads/comercios/rabieta.jpg', 'Cervecería Rabieta', 'tematico', 'alta_cocina', 22334465, -34.569793, -58.424390, '2025-06-19 19:00:00', 'https://www.rabieta.com.ar/', 4.7, 28, 4.4, "['jueves','viernes','sábado']", "['20-23']", "['happy_hour','musica_vivo']"),
                    (17, 75, '/resources/uploads/comercios/bistro_luz.jpg', 'Bistró Luz', 'especialidad', 'tecnico_conceptual', 22334466, -34.598355, -58.393281, '2025-06-20 18:45:00', 'https://www.melia.com/es/hoteles/argentina/buenos-aires/melia-recoleta-plaza/restaurantes', 4.5, 13, 4.3, "['miércoles','jueves','viernes']", "['16-18','20-23']", "['wifi','sin_gluten']"),
                    (18, 76, '/resources/uploads/comercios/casa_andina.jpg', 'Casa Andina', 'tematico', 'vanguardia', 22334467, -34.605014, -58.393823, '2025-06-20 13:30:00', 'https://www.instagram.com/casaandina.bs/', 4.0, 7, 3.7, "['lunes','jueves','sábado']", "['12-15','20-23']", "['delivery','apto_mascotas']"),
                    (19, 77, '/resources/uploads/comercios/mila_house.jpg', 'Mila House', 'familiar', 'autor', 22334468, -26.821289, -65.196905, '2025-06-20 14:00:00', 'https://www.instagram.com/milahousetucson/', 4.1, 10, 3.9, "['martes','viernes','domingo']", "['12-15']", "['para_llevar','wifi']"),
                    (20, 78, '/resources/uploads/comercios/sintesis-tapas-asiaticas.jpeg', 'Sintesis Tapas Asiaticas', 'especialidad', 'clasica', 22334469, -34.583813, -58.399702, '2025-06-20 20:15:00', 'https://www.facebook.com/sintesis.tapas.asiaticas', 4.6, 16, 4.2, "['miércoles','sábado']", "['12-15','20-23']", "['wifi','sin_gluten']"),
                    (21, 79, '/resources/uploads/comercios/parrilla_dona_rosa.jpg', 'Doña Rosa', 'familiar', 'alta_cocina', 22334470, -35.021799, -58.096594, '2025-06-20 19:30:00', 'https://www.facebook.com/rosakm57/?locale=es_LA', 3.8, 6, 3.4, "['martes','jueves','domingo']", "['12-15','20-23']", "['delivery']"),
                    (22, 80, '/resources/uploads/comercios/heladeria_polar.jpg', 'Helados Polar', 'especialidad', 'tecnico_conceptual', 22334471, -38.045068, -57.570899, '2025-06-20 16:00:00', 'https://www.instagram.com/heladospolar_/?hl=es', 4.2, 25, 4.0, "['lunes','viernes','sábado']", "['16-18','20-23']", "['apto_mascotas','wifi']"),
                    (23, 81, '/resources/uploads/comercios/tapas_y_vino.jpg', 'Tapas y Vino', 'gourmet', 'vanguardia', 22334472, -34.585185, -58.428887, '2025-06-20 21:00:00', 'https://www.instagram.com/calderatapas/', 4.9, 35, 4.8, "['viernes','sábado']", "['20-23']", "['musica_vivo','happy_hour']"),
                    (24, 82, '/resources/uploads/comercios/bio_natur.jpg', 'Bio Natur', 'tematico', 'autor', 22334473, -34.580982, -58.431215, '2025-06-20 11:00:00', 'https://biorestaurant.com.ar/', 4.5, 18, 4.1, "['lunes','miércoles','viernes']", "['12-15','20-23']", "['vegano','sin_gluten']"),
                    (25, 83, '/resources/uploads/comercios/taco_box.jpg', 'Taco Box', 'comida_rapida', 'clasica', 22334474, -34.573807, -58.455156, '2025-06-20 13:00:00', 'http://www.tacobox.com.ar/', 4.0, 12, 3.7, "['jueves','viernes','sábado']", "['12-15','20-23']", "['para_llevar','zona_fumadores']");""")


conn.commit()                           # Guardo los cambios realizados en la BDD
cursor.close()
conn.close()

print("Datos de prueba insertados correctamente.")