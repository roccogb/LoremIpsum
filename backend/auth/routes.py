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
    cursor = conn.cursor()

    qsql_usr_comercio = "SELECT * FROM usuario_comercio WHERE email_usuario=%s AND contrasena=%s"
    qsql_usr_consumidor = "SELECT * FROM usuario_consumidor WHERE email_usuario=%s AND contrasena=%s"

    cursor.execute(qsql_usr_consumidor, (body_request["usr"], body_request["pss"]))
    usuario_consumidor_existente = cursor.fetchone()

    cursor.execute(qsql_usr_comercio, (body_request["usr"], body_request["pss"]))
    usuario_comercio_existente = cursor.fetchone()

    cursor.close()
    conn.close()

    if usuario_comercio_existente or usuario_consumidor_existente:
        return jsonify({"msg": "Ingreso exitoso"}), 200
    else:
        return jsonify({"ERROR": "No se encontró ningún usuario con esa información"}), 404
