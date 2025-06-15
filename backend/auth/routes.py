from flask import request, jsonify, render_template, redirect, flash, url_for
from . import auth_bp
from database.db import get_connection

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = request.form
        if form.get("title") == "consumidor":
            nombre = form.get("first_name")
            apellido = form.get("last_name")
            usuario = form.get("usr")
            email = form.get("email")
            password = form.get("password")
            print(f"[consumidor] {usuario} - {email}")
        else:
            nombre_comercio = form.get("name_bss")
            categoria = form.get("categoria")
            tipo_cocina = form.get("tipo_cocina")
            email_comercio = form.get("email_bss")
            print(f"[comercio] {nombre_comercio} - {email_comercio}")

        flash("usuario registrado correctamente")
        return redirect(url_for('auth_bp.login'))

    return render_template("register.html")

@auth_bp.route('/usr', methods=["GET", "POST"])
def verificar_usr():
    body_request = request.get_json()
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) # Devuelve las filas de la tabla como diccionario.

    qsql_usr_comercio = "SELECT * FROM usuario_comercio WHERE email_usuario=%s AND contrasena=%s"
    qsql_usr_consumidor = "SELECT * FROM usuario_consumidor WHERE email_usuario=%s AND contrasena=%s"


    cursor.execute(qsql_usr_comercio, (body_request["usr"], body_request["pss"])) # Ejecuto primero la busqueda dentro de la tabla comercio.
    usuario_comercio = cursor.fetchone()

    if usuario_comercio:
        cursor.close() # Si se encuentra en comercio, cierra el cursor en esta linea para liberar recursos.
        conn.close()
        return jsonify({
            "tipo": "comercio",
            "id_usr": usuario_comercio["id_usr_comercio"],
            "nombre_usuario": usuario_comercio["nombre_apellido"]
        }), 200

    cursor.execute(qsql_usr_consumidor, (body_request["usr"], body_request["pss"])) # Si no encuentra al usuario en comercio, busca en la tabla de consumudidor.
    usuario_consumidor = cursor.fetchone()

    cursor.close() # Cierra cursor si encuentra o no al usuario.
    conn.close()

    if usuario_consumidor: # Retorna 'tipo', 'ids_usr' y 'usuario' para guardarlo en session.
        
        return jsonify({
            "tipo": "consumidor",
            "id_usr": usuario_consumidor["id_usr"],
            "nombre_usuario": usuario_consumidor["usuario"]
        }),200


    return jsonify({"ERROR": "No se encontró ningún usuario con esa información"}), 404