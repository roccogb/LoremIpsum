from flask import jsonify, request
from database.db import get_connection
from . import reservas_bp
import qrcode
import os

# Este endpoint mostrará todas las reservas vinculadas a un usuario.
# Se recibirá, a traves de la URI, un 'id' el cual servirá para identificar las reservas relacionadas al usuario
@reservas_bp.route("/usr/<int:id_usr>")
def get_reservas_usr(id_usr):
    conn=get_connection()                                               # Me conecto al servidor MySQL y a la BDD
    # Creo un cursor que me va a permitir ejecutar sentencias SQL. El parametro 'dictionary' hace que cada vez que realice una consulta a la BDD los resultados sean devueltos como diccionarios
    cursor=conn.cursor(dictionary=True)                                                

    # Sentencia que me va a permitir ver todos los datos de la tabla 'reservas donde la columna 'id_usr' es igual al parametro pasado.
    qsql_reservas_usr="""SELECT * FROM reservas WHERE id_usr=%s"""
    cursor.execute(qsql_reservas_usr,(id_usr,))
    reservas_usuario=cursor.fetchall()                      # Almaceno todas las filas del resultado de la consulta en 'reservas_usuario'

    cursor.close()
    conn.close()
    if not reservas_usuario:
        # Si no se encontró ninguna reserva relacionada al 'id' pasado como parametro
        return jsonify({"ERROR":f"No se encontró ningun registro relacionado al ID USUARIO:{id_usr}"}),404
    else:
        # Si se encontró reservas relacionadas al 'id' pasado como parametro
        return jsonify(reservas_usuario),200

# Este endpoint mostrará todas las reservas vinculadas a un comercio
# Se recibirá, a traves de la URI, un 'id' el cual servirá para identificar las reservas relacionadas al comercio
@reservas_bp.route("/comercio/<int:id_comercio>")
def get_reservas_comercio(id_comercio):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    qsql_reservas_comercio="""SELECT * FROM reservas WHERE id_comercio=%s"""
    cursor.execute(qsql_reservas_comercio,(id_comercio,))

    # Almaceno todos los registros resultantes de la consulta a la BDD en la variable 'reservas_comercio'
    reservas_comercio=cursor.fetchall()

    cursor.close()
    conn.close()
    if not reservas_comercio:
        # Si no se encontró ninguna reserva relacionada al id del comercio pasado como parámetro
        return jsonify({"ERROR":f"No se encontró ningun registro relacionado al ID COMERCIO:{id_comercio}"}),404
    else:
        # Si se encontró alguna reserva relacionada al id pasado como parámetor
        return jsonify(reservas_comercio),200
    
# Este endpoint mostrará toda la información relacionada a una reserva almacenada en la BDD
# Se recibirá, a traves de la URI, un 'id' el cual servirá para identificar la reserva en cuestión
@reservas_bp.route("/<int:id_reserva>")
def get_reserva(id_reserva):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    # Consulta que me va a retornar aquella fila vinculada al 'id' pasado como parámetro
    qsql_reserva_info="""SELECT * FROM reservas WHERE id_reserva=%s"""
    cursor.execute(qsql_reserva_info,(id_reserva,))

    reserva_encontrada=cursor.fetchone()                    # Almaceno la fila resultante de la consulta a la BDD en la variable 'reserva_encontrada'

    cursor.close()
    conn.close()

    if not reserva_encontrada:
        # Si no se encontró ninguna reserva vinculada a ese id
        return jsonify({"ERROR":f"No se encontró ningun registro vinculado al ID RESERVA:{id_reserva}"}), 404
    else:
        # Si se encontró una reserva vinculada a ese id
        return jsonify(reserva_encontrada),200

# Este endpoint va a agregar una nueva reserva a la BDD. El mismo va a recibir un archivo JSON con toda la informacion requerida para realizar la operación
@reservas_bp.route("/agregar", methods=["POST"])
def agregar_reserva():
    body_request=request.get_json()

    # Verifico que el archivo JSON contenga claves válidas. Estas mismas representan las columnas de la tabla
    claves_validas=["id_usr","id_comercio","nombre_bajo_reserva",
                      "email","telefono","cant_personas",
                      "fecha_reserva","solicitud_especial"]
    for clave in claves_validas:
        if clave not in body_request:
            return jsonify({"ERROR":f"Falta la clave '{clave}' en la petición"}),400

    conn=get_connection()
    cursor=conn.cursor()

    # Esta consulta va a insertar los datos recibidos en la tabla 'reservas' como un nuevo registro
    qsql_nueva_reserva=f""" INSERT INTO reservas 
                            (id_reserva,id_usr,id_comercio,nombre_bajo_reserva,email,telefono,cant_personas,fecha_reserva,solicitud_especial,estado_reserva) 
                            VALUES 
                            (default,%s,%s,%s,%s,%s,%s,%s,%s,default);"""
    
    cursor.execute(qsql_nueva_reserva,(body_request["id_usr"],body_request["id_comercio"],body_request["nombre_bajo_reserva"],
                                       body_request["email"],body_request["telefono"],body_request["cant_personas"],
                                       body_request["fecha_reserva"],body_request["solicitud_especial"]))

    conn.commit()                                           # Guardo los nuevos cambios realizados

    # Creo un código QR vinculado a la reserva en cuestión
    # El metodo 'lastrowid' va a retornar el ID de la ultima reserva agregada
    # Es necesario que en la URL este la IP local asi cualquier dispositivo de la misma red puede acceder al servidor Flask utilizando esa dirección. Permitiendo asi, a un telefono conectado a la misma red, escanear el QR para confirmar la reserva
    qr_reserva=qrcode.make(f"http://192.168.0.8:8100/reserva/estado/{cursor.lastrowid}")
    qr_reserva.save(f"../frontend/static/media/img/qr_reserva{cursor.lastrowid}.png")

    cursor.close()
    conn.close()
    return jsonify({"msg":"Reserva realizada con éxito"}),201

# Este endpoint eliminará de la BDD una reserva
# Se recibirá, a traves de la URI, un 'id' el cual permitirá identificar cual será el registro a eliminar
@reservas_bp.route("/eliminar/<int:id_reserva>", methods=["DELETE"])
def eliminar_reserva(id_reserva):
    conn=get_connection()
    cursor=conn.cursor()

    # Sentencia SQL que borrará un registro de la tabla 'reservas' donde la columna id_reserva sea igual al parametro recibido a traves de la URI
    qsql_eliminar_reserva="""DELETE FROM reservas WHERE id_reserva=%s"""
    cursor.execute(qsql_eliminar_reserva,(id_reserva,))

    conn.commit()                           # Guardo los cambios realizados

    # Elimino la imagen QR relacionada a esa reserva
    ruta_img_qr=f"../frontend/static/media/img/qr_reserva{id_reserva}.png"
    # Me aseguro de que la imagen se encuentre en la ruta determinada
    if os.path.exists(ruta_img_qr):
        # Si es asi, la elimino
        os.remove(ruta_img_qr)

    cursor.close()
    conn.close()
    return jsonify({"msg":"Reserva eliminada con éxito"}),200

# Este endpoit editará la información de una reserva almacenada en la BDD
# Recibirá un archivo JSON el cual contedrá toda la información a editar
@reservas_bp.route("/editar", methods=["PUT"])
def editar_reserva():
    body_request=request.get_json()

    # Verifico que el archivo JSON contenga claves válidas. Estas mismas representarán las columnas de la tabla
    claves_validas=["id_reserva","id_usr","id_comercio","nombre_bajo_reserva","email",
                    "telefono","cant_personas","fecha_reserva","solicitud_especial","estado_reserva"]
    for clave in claves_validas:
        if clave not in body_request:
            return jsonify({"ERROR":f"Falta la clave {clave} en la petición"}),400
    
    conn=get_connection()
    cursor=conn.cursor()

    # Esta sentencia va a actualizar los datos del registro referido a traves del ID
    qsql_editar_reserva=f"""UPDATE reservas
                            SET 
                            {claves_validas[1]}=%s,
                            {claves_validas[2]}=%s,
                            {claves_validas[3]}=%s,
                            {claves_validas[4]}=%s,
                            {claves_validas[5]}=%s,
                            {claves_validas[6]}=%s,
                            {claves_validas[7]}=%s,
                            {claves_validas[8]}=%s,
                            {claves_validas[9]}=%s 
                            WHERE {claves_validas[0]}=%s;"""
    
    cursor.execute(qsql_editar_reserva,(body_request["id_usr"],body_request["id_comercio"],body_request["nombre_bajo_reserva"],
                                        body_request["email"], body_request["telefono"], body_request["cant_personas"], 
                                        body_request["fecha_reserva"], body_request["solicitud_especial"], body_request["estado_reserva"], 
                                        body_request["id_reserva"]))

    conn.commit()                           # Guardo los cambios realizados
    cursor.close()
    conn.close()
    return jsonify({"msg":"Reserva actualizada"}),200
    
# Este endpoint modificará el estado de una reserva para asi poder confirmarla. Se recibirá a traves de un parametro dinamico de la URI el ID de la misma
# Implementación a futuro.
#   Luego de pasado un determinado tiempo, el estado de la reserva será 'False'
#   Realizar algun tipo de animación con el front o algo por el estilo para mostrar que la reserva se confirmo
@reservas_bp.route("/estado/<int:id_reserva>")
def modificar_estado(id_reserva):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    # Actualizo el estado de la reserva
    qsql_nuevo_estado="""UPDATE reservas
                         SET
                            estado_reserva=True
                         WHERE id_reserva=%s;"""
    cursor.execute(qsql_nuevo_estado,(id_reserva,))

    conn.commit()                           # Guardo los cambios realizados
    cursor.close()
    conn.close()
    return jsonify({"msg":"Estado de reserva actualizado"}),200
