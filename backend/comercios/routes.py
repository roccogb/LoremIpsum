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
        geolocalizador=Nominatim(user_agent="geo-FoodyBA")    
        locacion=geolocalizador.geocode(str_dir)
        if locacion:
            return [locacion.latitude, locacion.longitude]
    except Exception as e:
        print("Error: ",e)
    return None

# Endpoint que va a retornar TODA la información de los comercios. La misma será retornada en formato JSON
@comercios_bp.route("/")
def get_comercios():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    qsql_comercios="""SELECT * FROM comercios"""
    cursor.execute(qsql_comercios)                      
    comercios=cursor.fetchall()                       

    cursor.close()
    conn.close()
    return jsonify(comercios),200

# Endpoint que va a retornar TODA la información de un comercio. La misma será retornada en formato JSON
@comercios_bp.route("/<int:id_comercio>")
def get_comercio(id_comercio):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    sql="SELECT * FROM comercios WHERE id_comercio=%s"      
    cursor.execute(sql,(id_comercio,))                      

    comercio_encontrado=cursor.fetchone()                   

    cursor.close()
    conn.close()
    if not comercio_encontrado:
        return jsonify({"ERROR":"Comercio no encontrado"}),404
    else:
        return jsonify(comercio_encontrado),200

# De momento, se va a poder filtrar solamente por un parámetro. Implementación a futuro: que se pueda a filtrar por mas de un parámetro
# Endpoint que va a retornar información de la BDD de los comercios que cumplan con cierto patrón. Ej: 'retornar toda la información de los comercios con tipo de cocina china'
# Va a recibir un archivo JSON con la información necesaria para filtrar
@comercios_bp.route("/filtrar")
def get_comercios_filter():
    body_request=request.get_json()

    filtros_validos=["categoria","tipo_de_cocina","ubicacion",
                     "calificacion","dias","horarios","etiquetas"]
    
    if body_request["filtro"] not in filtros_validos:
        return jsonify({"ERROR":"Filtro inválido"}),400
    
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    qsql_filtrar_comercios=f""""""

    if body_request["filtro"] == "etiquetas":
        valores_filtro=literal_eval(body_request["valor"])
        condiciones_filtro=[f"etiquetas LIKE '%{valor}%'" for valor in valores_filtro]
        qsql_filtrar_comercios="SELECT * FROM comercios WHERE " + " OR ".join(condiciones_filtro)         
    else:
        qsql_filtrar_comercios=f"SELECT * FROM comercios WHERE {body_request["filtro"]}='{body_request["valor"]}';"
    
    cursor.execute(qsql_filtrar_comercios)
    comercios_filtrados=cursor.fetchall()                           # Almaceno todos los registros resultantes de la consulta a la BDD en la variable 'comercios_filtrados'

    cursor.close()
    conn.close()
    if not comercios_filtrados:
        return jsonify({"ERROR":"No se encontraron comercios bajo esos parametros"}),404
    else:
        return jsonify(comercios_filtrados),200

# Este endpoint va a permitir editar la información de un comercio. El mismo va a recibir un archivo JSON con la nueva información ingresada
@comercios_bp.route("/editar", methods=["PUT"])
def edit_comercio():
    body_request=request.get_json()

    conn=get_connection()                       # Me conecto al servidor MySQL y a la BDD
    cursor=conn.cursor()
    
    claves_validas=["id_comercio","nombre_comercio","categoria","tipo_de_cocina",
                     "telefono","direccion", "pdf_menu_link", "dias",
                     "horarios","etiquetas"]

    for clave in claves_validas:
        if clave not in body_request:
            return jsonify({"ERROR":f"Falta el dato '{clave}' en la petición"}), 400
    
    lat,lng=transform_dir_coords(body_request["direccion"])

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