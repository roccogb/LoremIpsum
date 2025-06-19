# Modulo que va a contener el conjunto de servicios vinculados al blueprint 'Comercios'
# Este es un borrador, el endpoint 'agregar' con las funciones auxiliares que utilizan puede ser necesitadas en otro blueprint'
from flask import jsonify, request
from . import comercios_bp
from database.db import get_connection
from fextra import transform_dir_coords

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
@comercios_bp.route("/get")
def get_comercio():
    body_request=request.get_json()
        
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    sql="SELECT * FROM comercios WHERE id_comercio=%s OR nombre_comercio=%s;"      
    
    cursor.execute(sql,(body_request["id_comercio"],body_request["nombre_comercio"]))                      
    comercio_encontrado=cursor.fetchone()                   

    cursor.close()
    conn.close()
    if not comercio_encontrado:
        return jsonify({"ERROR":"Comercio no encontrado"}),404
    else:
        ruta_relativa=comercio_encontrado["ruta_imagen"]
        host=request.host_url.rstrip("/")
        comercio_encontrado["ruta_imagen"]=host+ruta_relativa
        return jsonify(comercio_encontrado),200

# De momento, se va a poder filtrar solamente por un parámetro. Implementación a futuro: que se pueda a filtrar por mas de un parámetro
# Endpoint que va a retornar información de la BDD de los comercios que cumplan con cierto patrón. Ej: 'retornar toda la información de los comercios con tipo de cocina china'
# Va a recibir un archivo JSON con la información necesaria para filtrar     
@comercios_bp.route("/filtrar")
def get_comercios_filter():
    body_request = request.get_json()

    condiciones_filtro = []
    ordenar_calificacion = False

    for clave, valor in body_request.items():
        if clave == "dias":
            if len(valor) > 0:
                for tag in valor:
                    condiciones_filtro.append(f"dias LIKE '%{tag}%'")
        elif clave == "etiquetas":
            if len(valor) > 0:
                for tag in valor:
                    condiciones_filtro.append(f"etiquetas LIKE '%{tag}%'")
        elif clave == "horarios":
            if len(valor) > 0:
                for tag in valor:
                    condiciones_filtro.append(f"horarios LIKE '%{tag}%'")
        elif clave == "calificacion":
            if valor != "null":
                ordenar_calificacion = True
        else:
            if valor != "null":
                condiciones_filtro.append(f"{clave}='{valor}'")

    qsql_filtrar_comercio = "SELECT * FROM comercios"

    if condiciones_filtro:
        qsql_filtrar_comercio += " WHERE " + " AND ".join(condiciones_filtro)

    if ordenar_calificacion:
        orden = body_request["calificacion"].upper() 
        qsql_filtrar_comercio += f" ORDER BY ranking_ponderado {orden}"

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(qsql_filtrar_comercio)
    comercios_filtrados = cursor.fetchall()
    cursor.close()
    conn.close()

    if not comercios_filtrados:
        return jsonify({"ERROR": "No se encontraron comercios que cumplan con esos filtros"}), 404
    return jsonify(comercios_filtrados), 200

# Este endpoint va a permitir editar la información de un comercio. El mismo va a recibir un archivo JSON con la nueva información ingresada
@comercios_bp.route("/editar", methods=["PUT"])
def edit_comercio():
    body_request=request.get_json()

    conn=get_connection()                       # Me conecto al servidor MySQL y a la BDD
    cursor=conn.cursor()
    
    claves_validas=["id_comercio","nombre_comercio","categoria","tipo_cocina",
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
    
    cursor.execute(qsl_actualizar_comercio,(body_request["nombre_comercio"],body_request["categoria"],body_request["tipo_cocina"],
                                            body_request["telefono"], body_request["pdf_menu_link"], body_request["dias"], 
                                            body_request["horarios"], body_request["etiquetas"], body_request["id_comercio"]))

    conn.commit()                       # Guardo los nuevos cambios
    cursor.close()
    conn.close()
    
    return jsonify({"msg":"Comercio actualizado"}),200