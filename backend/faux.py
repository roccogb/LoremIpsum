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
    return [0,0]

# Esta funcion va a transformar unas coordenadas en una direccion. Util mas que nada para la visibilidad de la direccion de un comercio
def transform_coords_dir(coords):
    try:
        geolocalizador = Nominatim(user_agent="geo-FoodyBA")
        locacion = geolocalizador.reverse(coords, exactly_one=True)
        if locacion:
            return locacion.address
    except Exception as e:
        print("Error:", e)
    return "No disponible"

# Esta funcion va a validar el archivo subido por el usuario
def archivo_permitido(imagen):
    extensiones_permitidas=["jpg","jpeg","png"]
    valido=True
    if not imagen:
        return False
    
    nombre_archivo=imagen.filename
    
    if nombre_archivo=="":
        valido=False

    if not '.' in nombre_archivo or nombre_archivo.rsplit('.',1)[1].lower() not in extensiones_permitidas:
        valido=False

    return valido