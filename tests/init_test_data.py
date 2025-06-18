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
                  (id_comercio, id_usr_comercio, ruta_imagen, nombre_comercio, categoria, tipo_cocina, telefono, latitud, longitud, tiempo_de_creacion, pdf_menu_link, calificacion, dias, horarios, etiquetas)
                  VALUES 
                  (1, 4,'media/img/cafe_expressosc.jpg','Cafe Expresso', 'especialidad', 'autor', 99991111, 20.8501, -51.9987, '2015-05-22 10:50:10', 'https://www.cafemartinez.com/?srsltid=AfmBOooWV1qsi0jC_PbWjnW7bbE3NRQQnn7ZKZfjLTSypqMci67UFitx', 0, 0, 0, "['lunes','martes','miercoles','viernes','sabado','domingo']", "['7-11','16-18']", "['apto_mascotas', 'wifi','sin_gluten', 'musica_vivo']"),
                  (99, 11,'media/img/la_parrilla_ddua.jpeg','La Parrilla de Dua', 'familiar', 'autor', 12123030, -34.88412, -58.35581, '2002-09-22 11:35:55', 'https://www.facebook.com/groups/580812462862561/posts/1657688688508261/', 0, 0, 0, "['jueves','viernes','sabado','domingo']", "['12-15','19-23']", "['accesible','delivery','para_llevar', 'zona_fumadores', 'musica_vivo']"),
                  (15,3,'media/img/kwik_e_mart.jpg','Kwik-E-Mart', 'especialidad', 'vanguardia', 11112222,-54.6333, 50.5050, '2025-06-03 21:38:15', 'https://kwikemart4.mitiendanube.com/', 0, 0, 0, "['lunes','martes','miercoles','jueves','viernes','sabado','domingo']", "['0-24']", "['apto_mascotas','vegano', 'vegetariano','zona_fumadores','sin_gluten', 'para_llevar', 'accesible']"),
                  (7,5,'media/img/la_escuela_platense.jpg','Pasión Calamar', 'familiar', 'tecnico_conceptual', 14442011,-33.491974, -70.685941, '2025-06-10 9:37:00', 'superlinkmenu', 0, 0, 0, "['jueves','viernes','sabado','domingo']","['12-15','19-23']", "['wifi','apto_mascotas','para_llevar', 'delivery']"),
                  (11,6,'media/img/teatro_glamour.jpg','Pasarella del Glamour', 'gourmet', 'alta_cocina', 69691111,-34.60364165, -58.38587265, '2025-06-10 9:57:15', 'linkardodelmenu', 0, 0, 0, "['jueves','viernes','sabado','domingo']","['19-23','23-5']", "['vegano','vegetariano','wifi','sin_gluten', 'musica_vivo', 'happy_hour']"),
                  (2,7,'media/img/la_cachetona.jpg','La Cachetona de Varela', 'buffet', 'tecnico_conceptual', 22223131,-34.80108, -58.28662, '2025-06-10 10:00:58', 'linkiumleviosapdf', 0, 0, 0, "['lunes','martes','miercoles','jueves','viernes']","['7-11','12-15']", "['vegano','vegetariano', 'accesible', 'para_llevar', 'sin_gluten']"),
                  (9,9,'media/img/la_familiar.jpg','Las Noches Familiares', 'familiar', 'clasica', 99995555,-34.58015, -58.45086, '2025-06-10 10:10:15', 'menumenumenu', 0, 0, 0, "['jueves','viernes','sabado','domingo']","['19-23']", "['sin_gluten', 'accesible','zona_fumadores','wifi','delivery']"),
                  (44,10,'media/img/el_rojo_chileno.jpg','El Chileno Rojo', 'gourmet', 'alta_cocina', 88441212, -34.6702227, -58.37103780889193, '2025-06-10 10:12:50', 'linkmenulinkeadorojo', 0, 0, 0, "['jueves','viernes','sabado','domingo']","['19-23','23-5']", "['sin_gluten','wifi','accesible', 'musica_vivo', 'happy_hour']"),
                  (3,8,'media/img/azul_resto.jpg','VistebocalaurnaE', 'comida_rapida', 'vanguardia', 11115454,-34.63551715, -58.364916326853375, '2025-06-10 10:20:58', 'dameunmenu', 0, 0, 0, "['lunes','martes','miercoles','jueves','viernes','sabado','domingo']","['19-23','23-5']", "['para_llevar','delivery', 'accesible', 'wifi', 'zona_fumadores']"),  
                  (20,2,'media/img/supermekdo_chinardo.jpg','Super comercio', 'tematico', 'clasica', 20004444,20.555481, -35.43334, '2025-05-25 17:58:20', 'asasdadada', 0, 0, 0, "['lunes','martes','miercoles','jueves','viernes','sabado','domingo']","['0-24']", "['vegano','vegetariano','delivery', 'para_llevar', 'zona_fumadores']"),
                  (95, 12, 'media/img/pizzeria_roma.jpg', 'Pizzería Roma', 'tematico', 'clasica', 27123456, -34.603722, -58.381592, '2025-06-10 14:30:15', 'supermenuitaliano', 0, 0, 0,  "['jueves','viernes','sabado','domingo']", "['12-15','19-23']", "['delivery','para_llevar','sin_gluten', 'musica_vivo']"),
                  (32, 23, 'media/img/burger_house.jpg', 'Burger House', 'comida_rapida', 'clasica', 33987654, -34.615852, -58.445122, '2025-06-08 20:45:30', 'mirateestasburgas', 0, 0, 0, "['miercoles','jueves','viernes','sabado','domingo']", "['7-11','12-15','16-18','19-23']", "['delivery','happy_hour','musica_vivo','para_llevar']"),
                  (8, 35, 'media/img/sushi_tokyo.jpg', 'Sushi Tokyo', 'tematico', 'autor', 23456789, -34.588765, -58.372456, '2025-06-09 12:15:45', 'aligoto', 0, 0, 0, "['lunes','jueves','viernes','sabado','domingo']", "['12-15','19-23']", "['sin_gluten','happy_hour','zona_fumadores']"),
                  (41, 47, 'media/img/parrilla_argentina.jpg', 'La Parrilla Criolla', 'familiar', 'vanguardia', 20567891, -34.592341, -58.395123, '2025-06-07 19:20:10', 'miratecomoaulla', 0, 0, 0, "['lunes','martes','sabado','domingo']", "['12-15','19-23']", "['wifi','zona_fumadores','happy_hour','musica_vivo']"),
                  (26, 58, 'media/img/cafe_literario.jpg', 'Café Literario', 'especialidad', 'autor', 30445566, -34.580123, -58.390987, '2025-06-11 08:45:25', 'shhh', 0, 0, 0, "['lunes','martes','miercoles','jueves']", "['7-11','16-18']", "['wifi','sin_gluten','apto_mascotas','vegetariano','vegano']");""")
                  (1, 59, '/resources/uploads/comercios/don_cafe.jpg', 'Don Café', 'especialidad', 'autor', 22113344, -34.6037, -58.3816, '2025-06-15 09:00:00', 'https://doncafe.menu', 4.7, "['lunes','martes','miércoles','jueves','viernes']", "['7-11','16-19']", "['wifi','sin_gluten','apto_mascotas']"),
                  
                  (2, 60, '/resources/uploads/comercios/chimichurri_grill.jpg', 'Chimichurri Grill', 'familiar', 'clasica', 23004567, -34.6100, -58.4000, '2025-06-14 13:15:00', 'https://chimigrill.menu', 4.3, "['jueves','viernes','sábado','domingo']", "['12-15','19-23']", "['para_llevar','musica_vivo','zona_fumadores']"),
                  
                  (3, 61, '/resources/uploads/comercios/veggie_vida.jpg', 'Veggie Vida', 'tematico', 'vegano', 22119988, -34.5800, -58.3700, '2025-06-13 10:45:00', 'https://veggievida.menu', 4.9, "['lunes','miércoles','viernes']", "['12-15','18-21']", "['vegano','sin_gluten','accesible']"),
                  
                  (4, 62, '/resources/uploads/comercios/el_gourmet_oculto.jpg', 'El Gourmet Oculto', 'gourmet', 'alta_cocina', 23115678, -34.5933, -58.4100, '2025-06-12 20:00:00', 'https://gourmetoculto.link', 5.0, "['viernes','sábado']", "['20-00']", "['happy_hour','musica_vivo','wifi']"),
                  
                  (5, 63, '/resources/uploads/comercios/pollo_frito_king.jpg', 'Pollo Frito King', 'comida_rapida', 'vanguardia', 29998877, -34.5990, -58.3820, '2025-06-16 11:30:00', 'https://pollofrito.menu', 3.9, "['lunes','martes','miércoles','jueves','viernes','sábado']", "['11-15','18-22']", "['delivery','para_llevar','wifi']");
""")


############### REGUSTROS DE PRUEBA PARA LA TABLA 'reservas'
cursor.execute("""INSERT INTO reservas
                  (id_reserva,id_usr,id_comercio,nombre_bajo_reserva,email,telefono,cant_personas,fecha_reserva,solicitud_especial,estado_reserva)
                  VALUES
                  (10, 6, 1, 'Carla Peterson','cpeterson@gmail.com',11554433, 2, '2025-06-08 21:30:50', 'Quiero poder comer todo el menu Sin Gluten', True),
                  (15, 10, 2, 'German Beder', 'gerchosports@gmail.com', 15000999,3, '2025-06-01 20:30:50', 'Mesa mas alejada de la gente con sillita para niños, por favor.', True),
                  (21, 9, 2, 'Ricardo Bochini', 'richard_el_diablo@gmail.com',11445566, 1, '2025-06-05 18:25:50', 'Una milanesa napolitana con el escudo de independiente', True),
                  (22, 8, 3, 'Lucia Freitas', 'lufree@hotmail.com', 15400112, 5, '2025-06-06 11:15:20', 'Una mesa bastante grande, voy con mis facuamigos!!!', True),                                                      
                  (34, 10, 5, 'German Beder','gerchosports@gmail.com',15000999, 5, '2025-06-12 20:15:00', 'Una mesa grande, se probarán las alas del rey.', True);
               """)

############## REGISTROS DE PRUEBA PARA LA TABLA 'resenias'
cursor.execute("""INSERT INTO resenias
                  (id_comercio,id_usr,comentario,calificacion,tiempo_de_creacion, id_reserva)
                  VALUES
                  (1, 6, 'Un lugar tranquilo y con una buena carta. Excelente para una merienda con tu pareja', 4, '2025-06-01 22:15:00', 10),
                  (5, 10, 'Espantoso el lugar, no me alcanzan los caracteres para describir mi experiencia. Una de las famosas alas del rey que le dieron a mi amigo lo tuvo en el baño 3 hs, con eso te digo todo.', 1, '2025-06-05 19:00:00', 34),
                  (2, 9, 'Las mejores milanesas que probe en mi vida', 5, '2025-06-08 22:15:00', 21),
                  (2, 10, 'Excelente. Mis felicitaciones al maestro de la parrilla', 5, '2025-06-06 13:00:00', 15),
                  (3,8,'Buen lugar, mis amigos la pasaron bien aunque la comida no es bastante buena.',3, '2025-05-20 16:30:00', 22);
                """)

conn.commit()                           # Guardo los cambios realizados en la BDD
cursor.close()
conn.close()

print("Datos de prueba insertados correctamente.")