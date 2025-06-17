from geopy.geocoders import Nominatim

# Esta funcion va a convertir una dirección, pasada como string, en coordenadas geograficas.
# La misma puede ser utilizada por el blueprint 'Comercios' como tambien 'Autenticación'
def transform_dir_coords(str_dir):
    try:
        geolocalizador=Nominatim(user_agent="geo-FoodyBA")    
        locacion=geolocalizador.geocode(str_dir)
        if locacion:
            return [locacion.latitude, locacion.longitude]
    except Exception as e:
        print("Error: ",e)
    return 