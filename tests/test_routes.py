# Script que va a testear el funcionamiento de los endpoints del backend
from backend.faux import transform_dir_coords
from backend.app import app
import unittest

# Test unitarios de la funcion que transforma una direccion en coordenadas gracias a 'Geopy'
class TestDirCoord(unittest.TestCase):
    def setUp(self):
        print("=====TEST UNITARIOS=====")
    def test_transformacion_dir_coords_correcta(self):
        resultado=transform_dir_coords("Facultad de Ingenieria UBA")
        esperado=[-34.617610,-58.367966]
        for exp,res in zip(esperado,resultado):
            self.assertAlmostEqual(exp,res,places=3)
    def test_transform_dir_coords_incorrecta(self):
        resultado=transform_dir_coords("Pancheria FIUBA")
        esperado=[0,0]
        for exp,res in zip(esperado,resultado):
            self.assertEqual(exp,res)

#Test de integración de los endpoints del modulo autenticación
class TestROUTESAuth(unittest.TestCase):
    def setUp(self):
        self.client=app.test_client()
        print("=====Test ROUTES Auth=====")

    def test_log_consumidor_correcto(self):
        response=self.client.post("/auth/consumidor", json={"email":"gerchosports@gmail.com","pss":"oliviaquerida88"})
        self.assertEqual(200, response.status_code)

    def test_log_consumidor_incorrecto_inexistente(self):
        response=self.client.post("/auth/consumidor", json={"email":"test_cuenta_consumidor@gmail.com","pss":"prueba123"})
        self.assertEqual(404, response.status_code)

    def test_log_comercio_correcto(self):
        response=self.client.post("/auth/comercio", json={"email":"mfabbiani@canal.com","pss":"tvshow321"})
        self.assertEqual(200,response.status_code)
    
    def test_log_comercio_incorrecto_inexistente(self):
        response=self.client.post("/auth/comercio", json={"email":"test_cuenta_comerciante@gmail.com", "pss":"prueba123"})
        self.assertEqual(404, response.status_code)
    
    def test_reg_consumidor_correcto(self):
        response=self.client.post("/auth/register", json={"tipo_usuario":"consumidor",
                                                          "nombre_consumidor":"Matias","apellido_consumidor":"Sapienza",
                                                          "usuario_consumidor":"msspza","email_consumidor":"msapienza@fi.uba.ar",
                                                          "telefono_consumidor":"1131097368","password_consumidor":"contra123"})
        self.assertEqual(200, response.status_code)

    def test_reg_consumidor_incorrecto_data_incompleta(self):
        response=self.client.post("/auth/register", json={"tipo_usuario":"consumidor",
                                                          "nombre_consumidor":"","apellido_consumidor":"",
                                                          "usuario_consumidor":"","email_consumidor":"",
                                                          "telefono_consumidor":"","password_consumidor":""})
        self.assertEqual(400,response.status_code)
    
    def test_reg_consumidor_incorrecto_existente(self):
        response=self.client.post("/auth/register",json={"tipo_usuario":"consumidor",
                                                         "nombre_consumidor":"Ricardo","apellido_consumidor":"Bochini",
                                                         "usuario_consumidor":"maestro_rojo","email_consumidor":"richard_el_diablo@gmail.com",
                                                         "telefono_consumidor":"11445566","password_consumidor":"rojox100pre"})
        self.assertEqual(409, response.status_code)
    
    def test_reg_comercio_correcto(self):
        response=self.client.post("/auth/register",json={"tipo_usuario":"comercio",
                                                         "nombre_responsable":"Lucia Sanchez","dni_responsable":"41500311",
                                                         "cuit_responsable":"15415003118","email_responsable":"lsanchez@gmail.com",
                                                         "contrasena_usr_comercio":"l123","nombre_comercio":"La Parrilla Sanchez",
                                                         "tel_comercio":"54112020","dir_comercio":"Pancheria Fiuba",
                                                         "lkmenu_comercio":"https://pypi.org/project/geopy/","categoria":"Buffet",
                                                         "tipo_cocina":"alta_cocina","ruta_img":"/resources/uploads/comercios/img_resto_defecto.jpg",
                                                         "dias":['lunes','martes','miercoles'],"horarios":['7-10','12-15'], "etiquetas":['apto_mascotas','wifi']})
        self.assertEqual(200, response.status_code)
    
    def test_reg_comercio_incorrecto_existente(self):
        response=self.client.post("/auth/register",json={"tipo_usuario":"comercio",
                                                    "nombre_responsable":"Lucia Sanchez","dni_responsable":"41500311",
                                                    "cuit_responsable":"15415003118","email_responsable":"lsanchez@gmail.com",
                                                    "contrasena_usr_comercio":"l123","nombre_comercio":"La Parrilla Sanchez",
                                                    "tel_comercio":"54112020","dir_comercio":"Pancheria Fiuba",
                                                    "lkmenu_comercio":"https://pypi.org/project/geopy/","categoria":"Buffet",
                                                    "tipo_cocina":"alta_cocina","ruta_img":"/resources/uploads/comercios/img_resto_defecto.jpg",
                                                    "dias":['lunes','martes','miercoles'],"horarios":['7-10','12-15'], "etiquetas":['apto_mascotas','wifi']})
        self.assertEqual(409, response.status_code)
    
    def test_reg_comercio_incorrecto_data_incompleta(self):
        response=self.client.post("/auth/register",json={"tipo_usuario":"comercio",
                                                    "nombre_responsable":"","dni_responsable":"",
                                                    "cuit_responsable":"","email_responsable":"",
                                                    "contrasena_usr_comercio":"","nombre_comercio":"",
                                                    "tel_comercio":"","dir_comercio":"",
                                                    "lkmenu_comercio":"","categoria":"",
                                                    "tipo_cocina":"","ruta_img":"/resources/uploads/comercios/img_resto_defecto.jpg",
                                                    "dias":[],"horarios":[], "etiquetas":[]})
        self.assertEqual(400, response.status_code)
    
#Test de integración de los endpoints del modulo de comercios
class TestROUTESComercios(unittest.TestCase):
    def setUp(self):
        self.client=app.test_client()
        print("=====Test ROUTES Comercios=====")
    
    def test_get_comercios(self):
        response=self.client.get("/comercio/")
        self.assertEqual(200,response.status_code)
    
    def test_get_comercio_correcto(self):
        response=self.client.post("/comercio/get",json={"id_comercio":6,"nombre_comercio":""})
        self.assertEqual(200, response.status_code)
    
    def test_get_comercio_incorrecto_inexistente(self):
        response=self.client.post("/comercio/get",json={"id_comercio":0,"nombre_comercio":"Los Panchos de Mati"})
        self.assertEqual(404, response.status_code)
    
    def test_get_comercio_filtrado_correcto(self):
        response=self.client.post("/comercio/filtrar",json={"tipo_cocina":"alta_cocina"})
        self.assertEqual(200, response.status_code)
    
    def test_get_comercio_filtrado_incorrecto(self):
        response=self.client.post("/comercio/filtrar",json={"tipo_cocina":"coreana"})
        self.assertEqual(404, response.status_code)

#Test de integración de los endpoints del modulo de favoritos
class TestROUTESFavoritos(unittest.TestCase):
    def setUp(self):
        self.client=app.test_client()
        print("=====Test ROUTES Favoritos=====")

    def test_marcar_fav_correcto(self):
        response=self.client.post("/favs/alternar", json={"id_usr":6,"id_comercio":6})
        self.assertEqual(200, response.status_code)

    def test_fav_usr_correcto(self):
        response=self.client.get("/favs/detallado/6")
        self.assertEqual(200, response.status_code)

#Test de integración de los endpoints del modulo de reservas
class TestROUTESReservas(unittest.TestCase):
    def setUp(self):
        self.cliente=app.test_client()
        print("=====Test ROUTES Reservas=====")
    
    def test_agregar_reserva_correcto(self):
        response=self.cliente.post("/reserva/agregar",json={"id_usr":6,"id_comercio":6,
                                                            "nombre_bajo_reserva":"Carla Peterson", "email":"cpeterson@gmail.com",
                                                            "telefono":"11554433","cant_personas":3,"fecha_reserva":"2025-05-20 21:30:00",
                                                            "solicitud_especial":"La mejor mesa al frente del escenario"})
        self.assertEqual(201, response.status_code)
    
    def test_agregar_reserva_incorrecto_mala_peticion(self):
        response=self.cliente.post("/reserva/agregar",json={"id_usr":0,"id_comercio":0,
                                                            "nombre_bajo_reserva":"","email":"","telefono":"",
                                                            "cant_personas":0,"fecha_reserva":"","solicitud_especial":""})
        self.assertEqual(400,response.status_code)

    def test_get_reservas_usr_correcto(self):
        response=self.cliente.get("/reserva/usr/6")
        self.assertEqual(200,response.status_code)
    
    def test_get_reservas_usr_incorrecto_inexistente(self):
        response=self.cliente.get("/reserva/usr/999")
        self.assertEqual(404,response.status_code)
    
    def test_get_reservas_comercio_correcto(self):
        response=self.cliente.get("/reserva/comercio/6")
        self.assertEqual(200, response.status_code)
    
    def test_get_reservas_comercio_incorrecto_inexistente(self):
        response=self.cliente.get("/reserva/comercio/999")
        self.assertEqual(404, response.status_code)
    
    def test_get_reserva_correcto(self):
        response=self.cliente.get("/reserva/2")
        self.assertEqual(200, response.status_code)
    
    def test_get_reserva_incorrecto_inexistente(self):
        response=self.cliente.get("/reserva/99")
        self.assertEqual(404, response.status_code)

    def test_eliminar_reserva_correcto(self):
        response=self.cliente.put("/reserva/eliminar/2")
        self.assertEqual(200,response.status_code)
    
    def test_eliminar_reserva_incorrecto_inexistente(self):
        response=self.cliente.put("/reserva/eliminar/99")
        self.assertEqual(404,response.status_code)

# Test de integración de los endpoints del modulo de reservas. 
# Para realizar estos mismos es necesario tener una reserva previamente creada
class TestROUTESReview(unittest.TestCase):
    def setUp(self):
        self.client=app.test_client()
        print("=====Test ROUTES Review=====")
    
    def test_crear_review_correcto(self):
        response=self.client.post("/review/crear", json={"id_comercio":6,"calificacion":5,
                                                         "comentario":"Fascinante!!","id_reserva":1,
                                                         "id_usr":10})
        self.assertEqual(201,response.status_code)
    
    def test_crear_review_incorrecto_data_incompleta(self):
        response=self.client.post("/review/crear", json={"id_comercio":0,"calificacion":0,
                                                         "comentario":"","id_reserva":0,
                                                         "id_usr":0})
        self.assertEqual(400, response.status_code)
    
    def test_get_all_review_com_correcto(self):
        response=self.client.get("/review/com/6")
        self.assertEqual(200, response.status_code)
    
    def test_get_all_review_com_incorrecto_inexistente(self):
        response=self.client.get("/review/com/99")
        self.assertEqual(404, response.status_code)

    def test_get_all_review_cons_correcto(self):
        response=self.client.get("/review/usr/10")
        self.assertEqual(200, response.status_code)
    
    def test_get_all_review_cons_incorrecto_inexistente(self):
        response=self.client.get("/review/usr/99")
        self.assertEqual(404, response.status_code)

