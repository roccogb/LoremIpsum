from flask import request, jsonify
from backend.resenias import review_bp
from backend.database import get_connection

@review_bp.route("/crear", methods=["POST"])
def create_review():    
    data = request.get_json()
    id_comercio = data.get("id_comercio")
    calificacion = data.get("calificacion")
    comentario = data.get("comentario")
    id_reserva = data.get("id_reserva")
    id_usr = data.get("id_usr")

    if not all([id_comercio, calificacion, comentario, id_reserva, id_usr]):
        return jsonify({"msg": "Debe  completar todos los datos"}), 400
    
    if not (1 <= int(calificacion) <= 5):
        return jsonify ({"msg": "Debe enviar una calificación"}), 400
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute ("""
            INSERT INTO resenias 
            (id_comercio, id_usr, comentario, calificacion, tiempo_de_creacion, id_reserva)
            VALUES 
            (%s, %s, %s, %s, NOW(), %s);
            """, (id_comercio, id_usr, comentario, calificacion, id_reserva))
        
        cursor.execute("""
                UPDATE reservas
                SET resenia_pendiente = %s
                WHERE id_reserva = %s;""",
                (False, id_reserva))
        
        
        # Actualizar promedio
        cursor.execute("""
            SELECT AVG(calificacion) AS promedio, COUNT(*) AS cantidad
            FROM resenias
            WHERE id_comercio = %s;""",
            (id_comercio,))
        resultado = cursor.fetchone()
        nuevo_promedio = resultado["promedio"]
        nueva_cantidad = resultado["cantidad"]

        # Obtener promedio general
        cursor.execute("""SELECT AVG(calificacion) AS promedio_general FROM resenias;""")
        promedio_general = cursor.fetchone()["promedio_general"]

        m = 20  # Mínimo de reseñas para que se considere confiable la calificación
        v = nueva_cantidad
        r = float(nuevo_promedio)
        c = float(promedio_general)
        
        # Calcular el ranking ponderado
        ranking_ponderado = (v / (v + m)) * r + (m / (v + m)) * c

        cursor.execute("""
            UPDATE comercios
            SET promedio_calificacion = %s,
                cantidad_resenias = %s,
                ranking_ponderado = %s
            WHERE id_comercio = %s;""",
            (nuevo_promedio, nueva_cantidad, ranking_ponderado, id_comercio))
        conn.commit()
    except Exception as e:
        print("Error al crear reseña:", e)
        return jsonify({"error": "Error interno del servidor."}), 500
    
    finally:
        cursor.close()
        conn.close()
        return jsonify({"msg": "Reseña creada con éxito."}), 201

@review_bp.route("/com/<int:id_comercio>", methods=["GET"])
def get_all_review_com(id_comercio):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                r.comentario,
                r.calificacion,
                r.tiempo_de_creacion,
                u.usuario
            FROM resenias r
            JOIN usuario_consumidor u ON r.id_usr = u.id_usr
            WHERE id_comercio = %s;
        """, (id_comercio,))
        all_reviews = cursor.fetchall()

        cursor.close()
        conn.close()

        if not all_reviews:
            return jsonify({"msg":"No hay reseñas para este comercio"}),404

        return jsonify(all_reviews),200
    
    except Exception as e:

        cursor.close()
        conn.close()
        return jsonify({"ERROR":f"{str(e)}"}),500

@review_bp.route("/usr/<int:id_usr>", methods=["GET"])
def get_all_review_cons(id_usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                r.id_comercio,
                r.comentario,
                r.calificacion,
                r.tiempo_de_creacion,
                c.nombre_comercio
            FROM resenias r
            JOIN comercios c ON r.id_comercio = c.id_comercio
            WHERE r.id_usr = %s;"""
            , (id_usr,))
        all_reviews = cursor.fetchall()

        cursor.close()
        conn.close()

        if not all_reviews:
            return jsonify({"msg":"No hay reseñas para este usuario"}),404

        return jsonify(all_reviews)
    
    except Exception as e:
        cursor.close()
        conn.close()
        return jsonify({"ERROR":f"{str(e)}"}),500
