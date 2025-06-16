# Script de prueba para insertar datos en la BDD

from backend.database.db import get_connection

conn = get_connection()                 
cursor = conn.cursor()                  

################# REGISTROS DE PRUEBA PARA LA TABLA 'usuario_comercio'
cursor.execute("""INSERT INTO usuario_comercio 
               (id_usr_comercio,nombre_apellido, DNI,CUIT,email_usuario, contrasena) 
               VALUES 
               (2,'Walter White', 12305555, 20123055553,'heisenberg@hotmail.com',1234),
               (3,'Apu Nahasapeemapetilon', 45202333, 20442013668,'dandydelosprecios@outlook.com',5678),
               (4,'Sabrina Carpenter', 43102113, 20431021135,'sc_gamer2001@outlook.com','ABC123'),
               (5,'OrsiGomez', 21444201, 15214442018,'platensequerido@gmail.com','EFG123'),
               (6,'Moria Casan', 15202311, 21152023115,'divatotal@live.com','lacontramiamor1'),
               (7,'Billie Eilish', 44641333, 20446413335,'bbgamer777@hotmail.com','Jk12la454'),
               (8,'Ricky Blanco', 28714555, 19287145553,'rblanco@live.com','EH?33'),
               (9,'Camila Fortunato', 35200121, 23352001218,'princesitacf@live.com','theprincessdestroyer233'),
               (10,'Felipe Loyola', 42011211, 20420112115,'pipeguaton@hotmail.com','pipediablito22'),
               (11,'Dua Lipa', 40444252, 15404442527,'dlgutierrez@gmail.com','ABC456'),
               (12,'Comerciante12', 44121002, 16441210028,'mailgenerico@gmail.com','ABC456'),
               (23, 'Comerciante23', 33245789, 20332457891, 'usuario23@hotmail.com', 'DEF789'),
               (35, 'Comerciante35', 28967543, 27289675432, 'negocio35@outlook.com', 'GHI123'),
               (47, 'Comerciante47', 41582096, 20415820963, 'empresa47@yahoo.com', 'JKL456'),
               (58, 'Comerciante58', 36749821, 23367498214, 'comercio58@gmail.com', 'MNO789');""")

################ REGISTROS DE PRUEBA PARA LA TABLA 'usuario_consumidor'
cursor.execute("""INSERT INTO usuario_consumidor 
                  (id_usr,nombre_apellido, usuario, email_usuario, contrasena, numero_telefono, cant_reservas_canceladas) 
                  VALUES
                  (1, 'Matias Sapienza', 'msspza', 'matikpo2002@live.com','contraseña', 22113030, 0),
                  (2, 'Angela Leiva', 'AL777', 'negritacuartetera@gmail.com', 'ABC333', 11033030, 5),
                  (3, 'Sasha Ferro', 'ruggeri_chupapija', 'sashamiau@outlook.com', 'DEF888', 15150233, 20),
                  (4, 'Kevin Lomonaco','SeñorDELanoche','guarachita@hotmail.com','1234', 20335555, 15),
                  (5, 'Andrés Ducatenzeiler','Duka','rojitocorazon@live.com','1234', 69697777, 0),
                  (6, 'German Beder','gbeder','gercho-sports@gmail.com','oli299', 11223434, 2),
                  (7, 'Claudia Ianoco','cia22','claudita_iacono@live.com','1234', 33335455, 3),
                  (8, 'Laura Mendez','mistres_destroyer','lau_m@hotmail.com','5678', 11135555, 7),
                  (9, 'Tom Cruise','toti','themastercruise@live.com','la122', 66412020, 20),
                  (10, 'Esteban Quito','equito33','quitorepezl@hotmail.com','1334', 64423333, 0);""")

################ REGISTROS DE PRUEBA PARA LA TABLA 'comercios'
cursor.execute("""INSERT INTO comercios
                  (id_comercio,id_usr_comercio, ruta_imagen,nombre_comercio, categoria, tipo_cocina, telefono, latitud, longitud, tiempo_de_creacion, pdf_menu_link, calificacion, dias, horarios, etiquetas)
                  VALUES 
                  (1, 4,'media/img/cafe_expressosc.jpg','Cafe Expresso', 'especialidad', 'autor', 99991111, 20.8501, -51.9987, '2015-05-22 10:50:10', 'https://www.cafemartinez.com/?srsltid=AfmBOooWV1qsi0jC_PbWjnW7bbE3NRQQnn7ZKZfjLTSypqMci67UFitx',4.8, "['lunes','martes','miercoles','viernes','sabado','domingo']", "['7-11','16-18']", "['apto_mascotas', 'wifi','sin_gluten', 'musica_vivo']"),
                  (99, 11,'media/img/la_parrilla_ddua.jpeg','La Parrilla de Dua', 'familiar', 'autor', 12123030, -34.88412, -58.35581, '2002-09-22 11:35:55', 'https://www.facebook.com/groups/580812462862561/posts/1657688688508261/', 5, "['jueves','viernes','sabado','domingo']", "['12-15','19-23']", "['accesible','delivery','para_llevar', 'zona_fumadores', 'musica_vivo']"),
                  (15,3,'media/img/kwik_e_mart.jpg','Kwik-E-Mart', 'especialidad', 'vanguardia', 11112222,-54.6333, 50.5050, '2025-06-03 21:38:15', 'https://kwikemart4.mitiendanube.com/', 5,"['lunes','martes','miercoles','jueves','viernes','sabado','domingo']", "['0-24']", "['apto_mascotas','vegano', 'vegetariano','zona_fumadores','sin_gluten', 'para_llevar', 'accesible']"),
                  (7,5,'media/img/la_escuela_platense.jpg','Pasión Calamar', 'familiar', 'tecnico_conceptual', 14442011,-33.491974, -70.685941, '2025-06-10 9:37:00', 'superlinkmenu', 3.5, "['jueves','viernes','sabado','domingo']","['12-15','19-23']", "['wifi','apto_mascotas','para_llevar', 'delivery']"),
                  (11,6,'media/img/teatro_glamour.jpg','Pasarella del Glamour', 'gourmet', 'alta_cocina', 69691111,-34.60364165, -58.38587265, '2025-06-10 9:57:15', 'linkardodelmenu', 4.5, "['jueves','viernes','sabado','domingo']","['19-23','23-5']", "['vegano','vegetariano','wifi','sin_gluten', 'musica_vivo', 'happy_hour']"),
                  (2,7,'media/img/la_cachetona.jpg','La Cachetona de Varela', 'buffet', 'tecnico_conceptual', 22223131,-34.80108, -58.28662, '2025-06-10 10:00:58', 'linkiumleviosapdf', 2.8, "['lunes','martes','miercoles','jueves','viernes']","['7-11','12-15']", "['vegano','vegetariano', 'accesible', 'para_llevar', 'sin_gluten']"),
                  (9,9,'media/img/la_familiar.jpg','Las Noches Familiares', 'familiar', 'clasica', 99995555,-34.58015, -58.45086, '2025-06-10 10:10:15', 'menumenumenu', 4.5, "['jueves','viernes','sabado','domingo']","['19-23']", "['sin_gluten', 'accesible','zona_fumadores','wifi','delivery']"),
                  (44,10,'media/img/el_rojo_chileno.jpg','El Chileno Rojo', 'gourmet', 'alta_cocina', 88441212, -34.6702227, -58.37103780889193, '2025-06-10 10:12:50', 'linkmenulinkeadorojo', 5.5, "['jueves','viernes','sabado','domingo']","['19-23','23-5']", "['sin_gluten','wifi','accesible', 'musica_vivo', 'happy_hour']"),
                  (3,8,'media/img/azul_resto.jpg','VistebocalaurnaE', 'comida_rapida', 'vanguardia', 11115454,-34.63551715, -58.364916326853375, '2025-06-10 10:20:58', 'dameunmenu', 4.0, "['lunes','martes','miercoles','jueves','viernes','sabado','domingo']","['19-23','23-5']", "['para_llevar','delivery', 'accesible', 'wifi', 'zona_fumadores']"),  
                  (20,2,'media/img/supermekdo_chinardo.jpg','Super comercio', 'tematico', 'clasica', 20004444,20.555481, -35.43334, '2025-05-25 17:58:20', 'asasdadada', 2.5, "['lunes','martes','miercoles','jueves','viernes','sabado','domingo']","['0-24']", "['vegano','vegetariano','delivery', 'para_llevar', 'zona_fumadores']"),
                  (95, 12, 'media/img/pizzeria_roma.jpg', 'Pizzería Roma', 'tematico', 'clasica', 27123456, -34.603722, -58.381592, '2025-06-10 14:30:15', 'supermenuitaliano', 4.2, "['jueves','viernes','sabado','domingo']", "['12-15','19-23']", "['delivery','para_llevar','sin_gluten', 'musica_vivo']"),
                  (32, 23, 'media/img/burger_house.jpg', 'Burger House', 'comida_rapida', 'clasica', 33987654, -34.615852, -58.445122, '2025-06-08 20:45:30', 'mirateestasburgas', 3.8, "['miercoles','jueves','viernes','sabado','domingo']", "['7-11','12-15','16-18','19-23']", "['delivery','happy_hour','musica_vivo','para_llevar']"),
                  (8, 35, 'media/img/sushi_tokyo.jpg', 'Sushi Tokyo', 'tematico', 'autor', 23456789, -34.588765, -58.372456, '2025-06-09 12:15:45', 'aligoto', 4.5, "['lunes','jueves','viernes','sabado','domingo']", "['12-15','19-23']", "['sin_gluten','happy_hour','zona_fumadores']"),
                  (41, 47, 'media/img/parrilla_argentina.jpg', 'La Parrilla Criolla', 'familiar', 'vanguardia', 20567891, -34.592341, -58.395123, '2025-06-07 19:20:10', 'miratecomoaulla', 4.0, "['lunes','martes','sabado','domingo']", "['12-15','19-23']", "['wifi','zona_fumadores','happy_hour','musica_vivo']"),
                  (26, 58, 'media/img/cafe_literario.jpg', 'Café Literario', 'especialidad', 'autor', 30445566, -34.580123, -58.390987, '2025-06-11 08:45:25', 'shhh', 4.3, "['lunes','martes','miercoles','jueves']", "['7-11','16-18']", "['wifi','sin_gluten','apto_mascotas','vegetariano','vegano']");""")

############### REGUSTROS DE PRUEBA PARA LA TABLA 'reservas'
cursor.execute("""INSERT INTO reservas
                  (id_reserva,id_usr,id_comercio,nombre_bajo_reserva,email,telefono,cant_personas,fecha_reserva,solicitud_especial,estado_reserva)
                  VALUES
                  (10, 4, 15, 'Kevin Lomonaco','guarachita@hotmail.com',20335555, 2, '2025-06-08 21:30:50', 'Buena musica...', False),
                  (15, 1, 99, 'Matias Sapienza', 'matikpo2002@live.com', 22113030,4, '2025-06-01 20:30:50', 'Punto de coccion:La carne tiene que decir mu', True),
                  (21, 3, 1, 'Sasha Ferro', 'sashamiau@outlook.com',15150233, 1, '2025-06-05 18:25:50', 'El mejor cafe con leche posible', False),
                  (22, 1, 99, 'Matias Sapienza', 'matikpo2002@live.com', 22113030, 1, '2025-06-06 11:15:20', 'El mejor chinchulin disponible', True),                  
                  (30, 6, 11, 'German Beder','gercho-sports@gmail.com',11223434, 3, '2025-06-10 21:30:00', 'Mesa cerca del escenario por favor', True),
                  (31, 9, 3, 'Tom Cruise','themastercruise@live.com',66412020, 5, '2025-06-11 20:00:00', 'Mesa alejada del bullicio', False),
                  (32, 10, 2, 'Esteban Quito','quitorepezl@hotmail.com',64423333, 2, '2025-06-12 12:00:00', 'Sin mayonesa en la comida', True),
                  (33, 6, 11, 'German Beder','gercho-sports@gmail.com',11223434, 2, '2025-06-10 23:00:00', 'Sin sal', True),
                  (34, 2, 95, 'Angela Leiva','negritacuartetera@gmail.com',11033030, 4, '2025-06-12 20:15:00', 'Con velitas románticas', True);
               """)

############## REGISTROS DE PRUEBA PARA LA TABLA 'resenias'
cursor.execute("""INSERT INTO resenias
                  (id_comercio,id_usr,comentario,calificacion,tiempo_de_creacion, id_reserva)
                  VALUES
                  (99, 1, 'La mejor parrilla que probé en mi vida. El mozo sabía mi nombre antes de que llegara, un 10.', 5, '2025-06-01 22:15:00', 15),
                  (1, 3, 'El café estaba bien, pero la atención fue muy lenta. Volvería solo si mejoran eso.', 3, '2025-06-05 19:00:00', 21),
                  (15, 4, 'Lugar limpio y ordenado, pero la comida demoró demasiado.', 3, '2025-06-08 22:15:00', 10),
                  (99, 1, 'El chinchulín estaba espectacular. Vuelvo seguro.', 4, '2025-06-06 13:00:00', 22),
                  (11, 6, 'Música en vivo genial, pero la comida algo salada.', 4, '2025-06-10 23:00:00', 33);
                """)

conn.commit()                           # Guardo los cambios realizados en la BDD
cursor.close()
conn.close()

print("Datos de prueba insertados correctamente.")