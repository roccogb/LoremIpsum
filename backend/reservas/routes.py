from flask import jsonify, request
from backend.database import get_connection
from backend.reservas import reservas_bp
import qrcode
import os

# Este endpoint mostrará todas las reservas vinculadas a un usuario.
# Se recibirá, a traves de la URI, un 'id' el cual servirá para identificar las reservas relacionadas al usuario
@reservas_bp.route("/usr/<int:id_usr>")
def get_reservas_usr(id_usr):
    conn=get_connection()                                              
    cursor=conn.cursor(dictionary=True)                                                

    qsql_reservas_usr="""SELECT 
                            r.id_reserva,
                            r.id_usr,
                            r.id_comercio,
                            r.nombre_bajo_reserva,
                            r.email,
                            r.telefono,
                            r.cant_personas, 
                            r.fecha_reserva, 
                            r.solicitud_especial,
                            r.estado_reserva,
                            r.resenia_pendiente,
                            c.nombre_comercio 
                            FROM reservas r 
                            JOIN comercios c ON c.id_comercio=r.id_comercio
                            WHERE id_usr=%s"""
    
    cursor.execute(qsql_reservas_usr,(id_usr,))
    reservas_usuario=cursor.fetchall()

    cursor.close()
    conn.close()
    if not reservas_usuario:
        return jsonify({"ERROR":f"No se encontró ningun registro relacionado al ID USUARIO:{id_usr}"}),404
    else:
        return jsonify(reservas_usuario),200

# Este endpoint mostrará todas las reservas vinculadas a un comercio
# Se recibirá, a traves de la URI, un 'id' el cual servirá para identificar las reservas relacionadas al comercio
@reservas_bp.route("/comercio/<int:id_comercio>")
def get_reservas_comercio(id_comercio):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    qsql_reservas_comercio="""SELECT * FROM reservas WHERE id_comercio=%s"""
    cursor.execute(qsql_reservas_comercio,(id_comercio,))
    reservas_comercio=cursor.fetchall()

    cursor.close()
    conn.close()
    if not reservas_comercio:
        return jsonify({"ERROR":f"No se encontró ningun registro relacionado al ID COMERCIO:{id_comercio}"}),404
    else:
        return jsonify(reservas_comercio),200
    
# Este endpoint mostrará toda la información relacionada a una reserva almacenada en la BDD
# Se recibirá, a traves de la URI, un 'id' el cual servirá para identificar la reserva en cuestión
@reservas_bp.route("/<int:id_reserva>")
def get_reserva(id_reserva):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    qsql_reserva_info="""SELECT * FROM reservas WHERE id_reserva=%s"""
    cursor.execute(qsql_reserva_info,(id_reserva,))

    reserva_encontrada=cursor.fetchone()

    cursor.close()
    conn.close()

    if not reserva_encontrada:
        return jsonify({"ERROR":f"No se encontró ningun registro vinculado al ID RESERVA:{id_reserva}"}), 404
    else:
        return jsonify(reserva_encontrada),200

# Este endpoint va a agregar una nueva reserva bajo el ID de un usuario
@reservas_bp.route("/agregar", methods=["POST"])
def agregar_reserva():
    body_request = request.get_json()

    id_usr=body_request["id_usr"]
    id_comercio=body_request["id_comercio"]
    nombre_bajo_reserva=body_request["nombre_bajo_reserva"]
    email=body_request["email"]
    telefono=body_request["telefono"]
    cant_personas=body_request["cant_personas"]
    fecha_reserva=body_request["fecha_reserva"]
    solicitud_especial=body_request["solicitud_especial"]

    
    if not all([id_usr, id_comercio, nombre_bajo_reserva, email, 
                telefono, cant_personas,fecha_reserva,solicitud_especial]):
        return jsonify({"ERROR": "Debe completar todos los datos"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    qsql_nueva_reserva = """
        INSERT INTO reservas 
        (id_reserva,id_usr, id_comercio, nombre_bajo_reserva, email, telefono, cant_personas, fecha_reserva, solicitud_especial, estado_reserva) 
        VALUES (default,%s,%s,%s,%s,%s,%s,%s,%s, default);
    """

    cursor.execute(qsql_nueva_reserva, (
        id_usr, id_comercio, nombre_bajo_reserva,
        email, telefono, cant_personas,
        fecha_reserva, solicitud_especial
    ))

    ruta_absoluta_qr=os.path.join(os.path.abspath("backend/resources/uploads/temp"),f"qr{cursor.lastrowid}.png")

    ruta_relativa_qr = f"/resources/uploads/temp/qr{cursor.lastrowid}.png"

    qr_url = f"http://9.9.9.9:8200/qrproxy/{cursor.lastrowid}"         # Acá coloquen la segunda ip del front.
    qr_img = qrcode.make(qr_url)
    qr_img.save(ruta_absoluta_qr)
    

    qsql_update_qr = "UPDATE reservas SET ruta_qr = %s WHERE id_reserva = %s"
    cursor.execute(qsql_update_qr, (ruta_relativa_qr, cursor.lastrowid))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"msg": "Reserva realizada con éxito", "ruta_qr": ruta_relativa_qr}), 201

# Este endpoint actualizará el estado de una reserva a 'Eliminada'
# Se recibirá, a traves de la URI, un 'id' el cual permitirá identificar cual será el registro a eliminar
@reservas_bp.route("/eliminar/<int:id_reserva>", methods=["PUT"])
def eliminar_reserva(id_reserva):
    conn=get_connection()
    cursor=conn.cursor()

    qsql_reserva_existente="""SELECT * FROM reservas WHERE id_reserva=%s;"""
    cursor.execute(qsql_reserva_existente,(id_reserva,))
    reserva_existente=cursor.fetchone()
    
    if not reserva_existente:
        return jsonify({"ERROR":"No existe ninguna reserva bajo ese ID"}),404
    
    qsql_eliminar_reserva="""UPDATE reservas
                             SET
                                estado_reserva='Eliminada'
                             WHERE id_reserva=%s"""
    cursor.execute(qsql_eliminar_reserva,(id_reserva,))

    conn.commit()                           # Guardo los cambios realizados

    ruta_img_qr=f"{os.path.abspath("backend/resources/uploads/temp")}/qr{id_reserva}.png"
    if os.path.exists(ruta_img_qr):
        os.remove(ruta_img_qr)

    cursor.close()
    conn.close()
    return jsonify({"msg":"Reserva eliminada con éxito"}),200

# Este endpoint modificará el estado de una reserva para asi poder confirmarla. Se recibirá a traves de un parametro dinamico de la URI el ID de la misma
# Implementación a futuro.
#   Luego de pasado un determinado tiempo, el estado de la reserva será 'False'
#   Realizar algun tipo de animación con el front o algo por el estilo para mostrar que la reserva se confirmo
@reservas_bp.route("/estado/<int:id_reserva>", methods=["PUT"])
def modificar_estado(id_reserva):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    # Actualizo el estado de la reserva
    qsql_nuevo_estado="""UPDATE reservas
                         SET
                            estado_reserva='Confirmada'
                         WHERE id_reserva=%s;"""
    cursor.execute(qsql_nuevo_estado,(id_reserva,))

    
    conn.commit()                           # Guardo los cambios realizados

    ruta_absoluta_qr=f"{os.path.abspath("backend/resources/uploads/temp")}/qr{id_reserva}.png"
    os.remove(ruta_absoluta_qr)

    cursor.close()
    conn.close()
    return jsonify({"msg":"Estado de reserva actualizado"}),200
