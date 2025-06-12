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
                  (4, 'Kevin Lomonaco','SeñorDELanoche','guarachita@hotmail.com','1234', 20335555, 15);""")

################ REGISTROS DE PRUEBA PARA LA TABLA 'comercios'
cursor.execute("""INSERT INTO comercios
                  (id_comercio,id_usr_comercio, ruta_imagen,nombre_comercio, categoria, tipo_de_cocina, telefono, latitud, longitud, tiempo_de_creacion, pdf_menu_link, calificacion, dias, horarios, etiquetas)
                  VALUES 
                  (1, 4,'media/img/cafe_expressosc.jpg','Cafe Expresso', 'Especialidad', 'Cocina de autor', 99991111, 20.8501, -51.9987, '2015-05-22 10:50:10', 'https://www.cafemartinez.com/?srsltid=AfmBOooWV1qsi0jC_PbWjnW7bbE3NRQQnn7ZKZfjLTSypqMci67UFitx',4.8, 'Lunes-Viernes', '08:00-23:00', '[pet-friendly, wifi, terraza]'),
                  (99, 11,'media/img/la_parrilla_ddua.jpeg','La Parrilla de Dua', 'Familiar', 'Cócina clasica', 12123030, -34.88412, -58.35581, '2002-09-22 11:35:55', 'https://www.facebook.com/groups/580812462862561/posts/1657688688508261/', 5, 'Lunes-Viernes', '08:00-01:00', '[accesible,delivery,para_llevar,familiar]'),
                  (15,3,'media/img/kwik_e_mart.jpg','Kwik-E-Mart', 'Especialidad', 'Cocina de vanguardia', 11112222,-54.6333, 50.5050, '2025-06-03 21:38:15', 'https://kwikemart4.mitiendanube.com/', 5,'Lunes-Viernes', '24h', '[pet-friendly,vegano,accesible]'),
                  (7,5,'media/img/la_escuela_platense.jpg','Pasión Calamar', 'Familiar', 'Cocina técnico-conceptual', 14442011,-33.491974, -70.685941, '2025-06-10 9:37:00', 'superlinkmenu', 3.5, 'Miercoles-Domingo','10:00-00:00', '[wifi,pet-friendly,para_llevar, delivery]'),
                  (11,6,'media/img/teatro_glamour.jpg','Pasarella del Glamour', 'Gourmet', 'Alta cocina', 69691111,-34.60364165, -58.38587265, '2025-06-10 9:57:15', 'linkardodelmenu', 4.5, 'Miercoles-Domingo','20:00-02:00', '[vegano,vegetariano,wifi,sin_tacc]'),
                  (2,7,'media/img/la_cachetona.jpg','La Cachetona de Varela', 'Buffet', 'Cócina clasica', 22223131,-34.80108, -58.28662, '2025-06-10 10:00:58', 'linkiumleviosapdf', 2.8, 'Lunes-Viernes','11:00-23:00', '[vegano,vegetariano, accesible, para_llevar, sin_tacc]'),
                  (9,9,'media/img/la_familiar.jpg','Las Noches Familiares', 'Familiar', 'Cócina clasica', 99995555,-34.58015, -58.45086, '2025-06-10 10:10:15', 'menumenumenu', 4.5, 'Miercoles-Domingo','10:00-23:00', '[sin_tacc, accesible,terraza,wifi,delivery]'),
                  (44,10,'media/img/el_rojo_chileno.jpg','El Chileno Rojo', 'Gourmet', 'Alta cocina', 88441212, -34.6702227, -58.37103780889193, '2025-06-10 10:12:50', 'linkmenulinkeadorojo', 5.5, 'Lunes-Viernes','17:00-03:00', '[sin_tacc,wifi,terraza,accesible]'),
                  (3,8,'media/img/azul_resto.jpg','VistebocalaurnaE', 'Comida rapida', 'Cócina de vanguardia', 11115454,-34.63551715, -58.364916326853375, '2025-06-10 10:20:58', 'dameunmenu', 4.0, 'Lunes-Sabado','24h', '[para_llevar,delivery, accesible, wifi]'),  
                  (20,2,'media/img/supermekdo_chinardo.jpg','Super comercio', 'Gourmet', 'Chino', 20004444,20.555481, -35.43334, '2025-05-25 17:58:20', 'asasdadada', 2.5, 'Martes-Viernes','17:00-19:00', '[vegano,vegetariano,delivery]'),
                  (95, 12, 'media/img/pizzeria_roma.jpg', 'Pizzería Roma', 'Italiana', 'Pizza', 27123456, -34.603722, -58.381592, '2025-06-10 14:30:15', 'Auténtica pizza italiana', 4.2, 'Lunes-Domingo', '18:00-24:00', '[delivery,takeaway,gluten_free]'),
                  (32, 23, 'media/img/burger_house.jpg', 'Burger House', 'Americana', 'Hamburguesas', 33987654, -34.615852, -58.445122, '2025-06-08 20:45:30', 'Las mejores hamburguesas artesanales', 3.8, 'Miércoles-Lunes', '19:00-02:00', '[delivery,vegano,craft_beer]'),
                  (8, 35, 'media/img/sushi_tokyo.jpg', 'Sushi Tokyo', 'Japonesa', 'Sushi', 23456789, -34.588765, -58.372456, '2025-06-09 12:15:45', 'Sushi fresco y tradicional', 4.5, 'Martes-Sábado', '12:00-15:00,20:00-24:00', '[takeaway,sin_gluten,premium]'),
                  (41, 47, 'media/img/parrilla_argentina.jpg', 'La Parrilla Criolla', 'Argentina', 'Parrilla', 20567891, -34.592341, -58.395123, '2025-06-07 19:20:10', 'Carnes a la parrilla tradicional', 4.0, 'Jueves-Martes', '20:00-01:00', '[delivery,wine_pairing,asado]'),
                  (26, 58, 'media/img/cafe_literario.jpg', 'Café Literario', 'Cafetería', 'Café', 30445566, -34.580123, -58.390987, '2025-06-11 08:45:25', 'Café de especialidad y libros', 4.3, 'Lunes-Viernes', '07:00-22:00', '[wifi,vegetariano,quiet_space]');""")

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