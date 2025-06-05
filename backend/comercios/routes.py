# Modulo que va a contener el conjunto de servicios vinculados al blueprint 'Comercios'
# Este es un borrador, el endpoint 'agregar' con las funciones auxiliares que utilizan puede ser necesitadas en otro blueprint'
from flask import jsonify, request
from . import comercios_bp
from backend.database.db import get_connection
from geopy.geocoders import Nominatim
import re                                       # Libreria que me va a permitir trabajar con expresiones regulares

# Funcion auxiliar para verificar si la información ingresada es valida. Para que la información que se ingresa sea considerada válida se deben cumplir las siguientes condiciones:
#               - 'nombre_comercio' -> No debe contener digitos
#               - 'categoria_comercio' -> Se tiene que haber seleccionado una categoría
#               - 'tipo_cocina' -> Se tiene que haber seleccionado un tipo de cocina
#               - 'email_comercio' -> El email ingresado debe seguir un patrón
#               - 'nombre_responsable_comercio' -> El nombre del responsable no debe contener digitos
#               - 'dni_responsable_comercio' -> El DNI deben ser un total de 8 digitos
#               - 'cuit_responsable_comercio' -> El CUIT del responsable debe contener 11 digitos
def verificar_data_comercio(nombre_comercio, categoria_comercio, tipo_cocina, telefono_comercio, direccion_comercio, email_comercio, nombre_responsable_comercio,dni_responsable_comercio,cuit_responsable_comercio):
    # Verifico si el email ingresado es válido
    # La expresión regular representa al conjunto de cadenas que cumplan lo siguiente:
    #   '^[A-Za-z0-9._-]+'->Que la cadena empiece con un caracter existente, al menos una vez, en los siguientes conjuntos: [a-z],[A-Z],[0-9], . , _ , -  
    #   '@' -> Que contenga un arroba
    #   '[a-zA-Z._-]+' -> Que los caracteres continuos al arroba se encuentren, al menos una vez, en los siguientes conjuntos: [a-z],[A-Z], . , _ , -
    #   '\.[a-zA-Z]{2,}$' -> Que contenga un punto y que los caracteres finales de la cadena, sean mayores a 2 y se encuentren en los conjunto: [a-z], [A-Z]
    email_valido=re.search(r"^[A-Za-z0-9._-]+@[a-zA-Z._-]+\.[a-zA-Z]{2,}$", email_comercio)

    if nombre_comercio.isalpha() and categoria_comercio != "-" and tipo_cocina != "-" and len(str(telefono_comercio)) == 8 and direccion_comercio != None and email_valido and nombre_responsable_comercio.isalpha() and len(str(dni_responsable_comercio)) == 8 and len(str(cuit_responsable_comercio)):
        return True
    else:
        return False

# Funcion auxiliar que, mediante la librería geocoder, va a retornar una lista con las coordenadas en el siguiente formato [coordX,coordY]
def transform_dir_coords(str_dir):
    try:
        # Inicializo el geolocalizador Nomitanim de la API OpenStreetMap 
        # El parametro 'usr_agent' es obligatorio para asi poder identificar mi aplicación ante el servicio de geocodificacion
        geolocalizador=Nominatim(user_agent="geo-FoodyBA")    
        locacion=geolocalizador.geocode(str_dir)                # Realizo una petición a la API y busco la dirección. Si la ubicación es encontrada, la API envía una respuesta con la misma
        if locacion:
            # Si encontró la dirección
            return [locacion.latitude, locacion.longitude]
    except Exception as e:
        # Ver si devuelvo un mensaje de error o algo por el estilo
        print("Error: ",e)
    return None

# Endpoint que va a retornar TODA la información de los comercios. La misma será retornada en formato JSON
@comercios_bp.route("/")
def get_comercios():
    conn=get_connection()                               # Me conecto al servidor MySQL y a la BDD
    # Creo un cursor para así poder ejecutar sentencias SQL. El parametro dictionary hace que cada vez que haga una consulta a la BDD, me devuelva los datos como diccionarios facilitando asi la transformación de los mismos a JSON
    cursor=conn.cursor(dictionary=True)

    qsql_comercios="""SELECT * FROM comercios"""
    cursor.execute(qsql_comercios)                      # Ejecuto la consulta
    comercios=cursor.fetchall()                         # Almaceno todas las filas del resultado de la consulta en la variable 'comercios'.

    cursor.close()
    conn.close()
    return jsonify(comercios),200

# Endpoint que va a retornar TODA la información de un comercio. La misma será retornada en formato JSON
@comercios_bp.route("/<int:id_comercio>")
def get_comercio(id_comercio):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    #Parametrizo la consulta, esto va a mejorar la seguridad y la legibilidad del código
    sql="SELECT * FROM comercios WHERE id_comercio=%s"      # Sentencia SQL con un marcador que trabaja como parametro
    cursor.execute(sql,(id_comercio,))                      # Con el cursor ejecuto la sentencia y de segundo parametro le paso una tupla con los parametros a utilizar

    comercio_encontrado=cursor.fetchone()                   # El método fetchone va a retornar la primera fila del resultado de la consulta

    cursor.close()
    conn.close()
    if not comercio_encontrado:
        # Si no se encontró ningun comercio bajo ese ID, retorno un código 404
        return jsonify({"ERROR":"Comercio no encontrado"}),404
    else:
        # Si se encontró un comercio bajo ese ID
        return jsonify(comercio_encontrado),200
    
# Endpoint que va a retornar información de la BDD de los comercios que cumplan con cierto patrón. Ej: 'retornar toda la información de los comercios con tipo de cocina china'
# Implementar la funcionalidad de filtrar comercios según los tags vinculados a los mismos
@comercios_bp.route("/<filtro>/<valor>")
def get_comercios_filter(filtro,valor):
    # Verifico que el filtro pasado por la URI sea válido
    filtros_validos=["categoria","tipo_de_cocina","ubicacion","tiempo_de_creacion",
                    "calificacion","horarios"]      # Agregar las 'tags' vinculadas al comercio
    if filtro not in filtros_validos:
        return jsonify({"ERROR":"Filtro inválido"}),400
    
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    #Parametrizo la consulta, brindando asi mejor seguridad y legibilidad al código
    sql=f"""SELECT * FROM comercios WHERE {filtro}=%s;"""    
    cursor.execute(sql,(valor,))

    comercios_filtrados=cursor.fetchall()                   # El método fetchall va a retornar todas las filas del resultado de la consulta

    cursor.close()
    conn.close()
    if not comercios_filtrados:
        # Si no encontró comercios que cumplan con el filtro
        return jsonify({"ERROR":"No existen comercios que compartan esa caracteristica"}),404
    else:
        # Si se encontraron comercios que cumplan con el filtro
        return jsonify(comercios_filtrados),200

# MOMENTANEO. BORRADOR
@comercios_bp.route("/agregar")
def add_comercio():
    nombre_comercio=request.form["name_bss"]
    categoria_comercio=request.form["categoria"]
    tipo_cocina=request.form["tipo_cocina"]
    telefono_comercio=request.form["tel_bss"]
    direccion_comercio= transform_dir_coords(request.form["dir_bss"])
    email_comercio=request.form["email_bss"]
    nombre_responsable_comercio=request.form["nr_bss"]
    dni_responsable_comercio=request.form["dni_responsable_bss"]
    cuit_responsable_comercio=request.form["cuit_responsable_bss"]

    pass