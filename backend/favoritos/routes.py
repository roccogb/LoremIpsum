from flask import jsonify, request
from . import favoritos_bp
from database.db import get_connection


@favoritos_bp.route('/agregar', methods=['POST'])
def agregar():
    data = request.get_json()
    id_usr = data.get('id_usr')
    id_comercio = data.get('id_comercio')
    if not id_usr or not id_comercio:
        return jsonify({"success": False, "msg": "Datos incompletos"}), 400

    conn = get_connection() #conecta con la bdd y el servidor
    cursor = conn.cursor(dictionary= True) #"cualquier resultado de las consultas pasa a diccionarios para trabajar con él".
    cursor.execute("SELECT * FROM favoritos WHERE id_usr=%s AND id_comercio=%s", (id_usr, id_comercio))
    existe = cursor.fetchone() #agarra el resultado de la consulta.
    if existe: #si el favorito ya existe, lo borra.
        cursor.execute("DELETE FROM favoritos WHERE id_usr=%s AND id_comercio=%s", (id_usr, id_comercio))
        conn.commit()
        favorito = False
    else: #agrega el favortito nuevo
        cursor.execute("INSERT INTO favoritos (id_usr, id_comercio) VALUES (%s, %s)", (id_usr, id_comercio))
        conn.commit()
        favorito = True
    cursor.close()
    conn.close()
    return jsonify({"success": True, "favorito": favorito})

@favoritos_bp.route('/<int:id_usr>', methods=['GET'])
def listar_favoritos(id_usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_comercio FROM favoritos WHERE id_usr=%s", (id_usr,))
    favs = [row['id_comercio'] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(favs)