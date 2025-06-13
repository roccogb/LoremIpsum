# Modulo borrador
from backend.comercios.routes import verificar_data_comercio, transform_dir_coords
import unittest

class TestUnitarios(unittest.TestCase):
    def test_verificacion_datos_erroneo(self):
        # Se ingresa un nombre incorrecto
        resultado=verificar_data_comercio("hola4","Especialidad","Cocina de vanguardia",11112222,"Tero violado","2025-06-03 21:38:15","https://kwikemart4.mitiendanube.com/",5,"24h")
        self.assertFalse(resultado)
    def test_verificacion_datos_correcto(self):
        resultado=verificar_data_comercio("El Cuadrado de la cocina","Familiar","Cocina de autor",22223333, "Villa fiorito","2025-06-04 18:38:20", "https://www.instagram.com/cocina_al_cuadrado/?hl=es",3.2,"8:00 - 15:00")
        pass
    def test_trans_dir_coords_correcto(self):
        # Se verifica que la funcion 'transform_dir_coords' pase correctamente una direccion a coordenadas
        resultado=transform_dir_coords("UBA Facultad de Ingenieria")
        lat,lng=resultado                                               # Desempaqueto las coordenadas ya que [coordX,coordY]
        self.assertAlmostEqual(lat, -34.617610, places=3)               # Compruebo si la coordX es mas o menos igual a la indicada. Se tolera un margen de 3 decimales
        self.assertAlmostEqual(lng, -58.368436, places=3)               # Compruebo si la coordY es mas o menos igual a la indicada. Se tolera un margen de 3 decimales