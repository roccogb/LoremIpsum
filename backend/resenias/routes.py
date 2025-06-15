from flask import request, jsonify, session
from . import resenias_bp
from database.db import get_connection

@resenias_bp.route("/crear", methods=["POST"])
def crear_resenia():
    if "id_usr" not in session:      # Corrobora que el usuario este logueado. 
        return jsonify({"msg": "Debe loguearse"}), 401
    
    data = request.get_json()
    id_comercio = data.get("id_comercio")
    calificacion = data.get("puntuacion")
    comentario = data.get("comentario")
    id_reserva = data.get("id_reserva")
    id_usr = session["id_usr"]

    if not all([id_comercio, calificacion, comentario, id_reserva]):  # Corrobora que los campos se llenen.
        return jsonify({"msg": "Debe  completar todos los datos"}), 400
    
    if not (1 <= int(calificacion) <= 5):
        return jsonify ({"msg": "Debe enviar una calificación"}), 400
    
    conn = get_connection
    cursor = conn.cursor(dictionary=True)

    try:
        # Verificar reserva válida y confirmada por asistencia.
        cursor.execute (""" 
            SELECT * FROM reservas WHERE id_reservas = %s 
            AND id_usr = %s AND id_comercio = %s AND estado_reserva = TRUE 
            """,(id_reserva, id_usr, id_comercio))
        reserva_valida = cursor.fetchone()

        if not reserva_valida:
            return jsonify({"error": "Reserva no confirmada por asistencia"}), 403
        
        """
        # Verificar que no exista otra reseña con la misma reserva
        cursor.execute (" SELECT * FROM resenias WHERE id_reserva = %s ", (id_reserva))
        if cursor.fetchone():
            return jsonify({"error": "Ya existe una resenia para esta reseña."}), 409
        """
        # Insertar reseña

        cursor.execute ("""
            INSERT INTO resenias (id_comercio, id_usr, comentario, calificacion, tiempo_de_creacion, id_reserva)
            VALUES (%s, %s, %s, %s, NOW(), %s)
            """, (id_comercio, id_usr, comentario, calificacion, id_reserva))
        conn.commit()

        return jsonify({"msg": "Reseña creada con éxito."}), 201
    
    except Exception as e:
        print("Error al crear reseña:", e)
        return jsonify({"error": "Error interno del servidor."}), 500
    
    finally:
        cursor.close()
        conn.close()