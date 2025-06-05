from flask import render_template, request, redirect, url_for, flash
from . import auth_bp

# ruta para registrar usuarios
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # aca se procesan los datos del formulario
        form = request.form

        if form.get("title") == "consumidor":
            # logica para registrar usuario final
            nombre = form.get("first_name")
            apellido = form.get("last_name")
            usuario = form.get("usr")
            email = form.get("email")
            password = form.get("password")
            print(f"[consumidor] {usuario} - {email}")
        else:
            # logica para registrar usuario comercio
            nombre_comercio = form.get("name_bss")
            categoria = form.get("categoria")
            tipo_cocina = form.get("tipo_cocina")
            email_comercio = form.get("email_bss")
            print(f"[comercio] {nombre_comercio} - {email_comercio}")

        flash("usuario registrado correctamente")
        return redirect(url_for('auth_bp.login'))

    return render_template("register.html")

# ruta para iniciar sesion
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get("username")
        password = request.form.get("password")
        print(f"intento de login: {usuario} / {password}")
        flash("login exitoso")
        return redirect(url_for("auth_bp.login"))

    return render_template("login.html")

