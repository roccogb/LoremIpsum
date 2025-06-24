from flask import jsonify, request
from . import favoritos_bp
from database.db import get_connection

# Este endpoint va a marcar o desmarcar un comercio
@favoritos_bp.route('/alternar', methods=['POST'])
def alternar_fav():
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
        favorito = False
    else: #agrega el favorito nuevo
        cursor.execute("INSERT INTO favoritos (id_usr, id_comercio) VALUES (%s, %s)", (id_usr, id_comercio))
        favorito = True

    conn.commit()
    cursor.close()
    conn.close()
   
    return jsonify({"marca": favorito}),200

# Este endpoint va a listar los favoritos de un usuario
@favoritos_bp.route('/detallado/<int:id_usr>', methods=['GET'])
def listar_favoritos_con_detalle(id_usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT c.id_comercio, c.nombre_comercio, c.ruta_imagen, c.ranking_ponderado
        FROM favoritos f
        LEFT JOIN comercios c ON f.id_comercio = c.id_comercio
        WHERE f.id_usr = %s 
    """
    cursor.execute(query, (id_usr,))
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(resultados),200