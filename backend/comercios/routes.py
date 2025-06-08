# Modulo que va a contener el conjunto de servicios vinculados al blueprint 'Comercios'
# Este es un borrador, el endpoint 'agregar' con las funciones auxiliares que utilizan puede ser necesitadas en otro blueprint'
from flask import jsonify, request
from . import comercios_bp
from database.db import get_connection
from geopy.geocoders import Nominatim
from ast import literal_eval                    # Libreria que estándar de Python para trabajr con cadenas

# Esta funcion va a convertir una dirección, pasada como string, en coordenadas geograficas.
# La misma puede ser utilizada por el blueprint 'Comercios' como tambien 'Autenticación'
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

# De momento, se va a poder filtrar solamente por un parámetro. Implementación a futuro: que se pueda a filtrar por mas de un parámetro
# Endpoint que va a retornar información de la BDD de los comercios que cumplan con cierto patrón. Ej: 'retornar toda la información de los comercios con tipo de cocina china'
# Va a recibir un archivo JSON con la información necesaria para filtrar
@comercios_bp.route("/filtrar")
def get_comercios_filter():
    body_request=request.get_json()

    # Verifico que el JSON contenga filtros válidos
    filtros_validos=["categoria","tipo_de_cocina","ubicacion",
                     "calificacion","dias","horarios","etiquetas"]
    
    if body_request["filtro"] not in filtros_validos:
        return jsonify({"ERROR":"Filtro inválido"}),400
    
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    qsql_filtrar_comercios=f""""""

    # Armo la consulta que me va a permitir filtrar los comercios segun el parámetro ingresado
    if body_request["filtro"] == "etiquetas":
        # Si el filtro seleccionado es mediante etiquetas
        # Convierto el string que representa una estructura de datos en el objeto que corresponde
        valores_filtro=literal_eval(body_request["valor"])
        # Creo una nueva lista aplicando una expresión, como 'etiquetas LIKE ....', a todos los elementos de un iterable. Esta tecnica se conoce como comprensión de listas
        # ["etiquetas LIKE '%etiquetaA%'", "etiquetas LIKE '%etiquetaB%'", ..... ]
        condiciones_filtro=[f"etiquetas LIKE '%{valor}%'" for valor in valores_filtro]
        # Uno todos los elementos de la lista 'condiciones_filtro' con el caracter ' OR ' generando la siguiente sentencia SQL para poder realizar una consulta a la BDD
        # "SELECT * FROM comercios WHERE etiquetas LIKE '%etiquetaA%' OR etiquetas LIKE '%etiquetaB%'"
        qsql_filtrar_comercios="SELECT * FROM comercios WHERE " + " OR ".join(condiciones_filtro)         
    else:
        # Si es cualquier otro tipo de filtro
        qsql_filtrar_comercios=f"SELECT * FROM comercios WHERE {body_request["filtro"]}='{body_request["valor"]}';"
    
    cursor.execute(qsql_filtrar_comercios)
    comercios_filtrados=cursor.fetchall()                           # Almaceno todos los registros resultantes de la consulta a la BDD en la variable 'comercios_filtrados'

    cursor.close()
    conn.close()
    if not comercios_filtrados:
        # Si no se encontrarón comercios que cumplan con los parámetros recibidos
        return jsonify({"ERROR":"No se encontraron comercios bajo esos parametros"}),404
    else:
        # Si se encontraron comercios
        return jsonify(comercios_filtrados),200

# Este endpoint va a permitir editar la información de un comercio. El mismo va a recibir un archivo JSON con la nueva información ingresada
@comercios_bp.route("/editar", methods=["PUT"])
def edit_comercio():
    body_request=request.get_json()

    conn=get_connection()                       # Me conecto al servidor MySQL y a la BDD
    cursor=conn.cursor()
    
    # Verifico que el JSON recibido contenga claves válidas. Estas mismas representan las columnas de la tabla
    claves_validas=["id_comercio","nombre_comercio","categoria","tipo_de_cocina",
                     "telefono","direccion", "pdf_menu_link", "dias",
                     "horarios","etiquetas"]

    for clave in claves_validas:
        if clave not in body_request:
            return jsonify({"ERROR":f"Falta el dato '{clave}' en la petición"}), 400
    
    lat,lng=transform_dir_coords(body_request["direccion"])            # Convierto la dirección ingresada por el usuario en coordenadas lat=coordX;long=coordY

    # Consulta de SQL que me va a permitir actualizar la información de un comercio
    qsl_actualizar_comercio=f"""UPDATE comercios 
                                SET 
                                {claves_validas[1]}=%s, 
                                {claves_validas[2]}=%s, 
                                {claves_validas[3]}=%s, 
                                {claves_validas[4]}=%s, 
                                latitud={lat}, 
                                longitud={lng},
                                {claves_validas[6]}=%s, 
                                {claves_validas[7]}=%s, 
                                {claves_validas[8]}=%s, 
                                {claves_validas[9]}=%s 
                                WHERE {claves_validas[0]}=%s;"""
    
    cursor.execute(qsl_actualizar_comercio,(body_request["nombre_comercio"],body_request["categoria"],body_request["tipo_de_cocina"],
                                            body_request["telefono"], body_request["pdf_menu_link"], body_request["dias"], 
                                            body_request["horarios"], body_request["etiquetas"], body_request["id_comercio"]))

    conn.commit()                       # Guardo los nuevos cambios
    cursor.close()
    conn.close()
    
    return jsonify({"msg":"Comercio actualizado"}),200