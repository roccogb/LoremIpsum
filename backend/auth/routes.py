from flask import request, jsonify, render_template, redirect, flash, url_for
from . import auth_bp
from database.db import get_connection

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

# Este endpoint va a recibir un archivo JSON con la información del usuario que desea iniciar sesión y va a verificar si el mismo se encuentra en el sistema, de ser así responderá con un codigo HTTP 200.
# Para poder realizar esto, primero hay que verificar que tipo de usuario es.
@auth_bp.route('/usr', methods=["GET","POST"])              
def verificar_usr():
    body_request=request.get_json()             # Información enviada por el usuario
    conn=get_connection()                       # Me conecto al servidor MySQL y a la BDD
    cursor=conn.cursor()                        # Creo un cursor para asi poder realizar consultas a la BDD

    # Escribo la consulta que me va a permitir verificar si la información ingresada es de un usuario registrado. Esta misma tendrá que ser para un usuario consumidor y tambien usuario comercio
    # Los caracteres '%s' se utilizan como marcadores de posición para pasar parametros a la consulta de forma segura.
    qsql_usr_comercio="SELECT * FROM usuario_comercio WHERE email_usuario=%s AND contrasena=%s"                       # Consulta que sirve para verificar en la tabla 'usuario_comercio'  si existe una cuenta que comparta las caracteristicas denominadas
    qsql_usr_consumidor="SELECT * FROM usuario_consumidor WHERE email_usuario=%s AND contrasena=%s"                   # Consulta que sirve para verificar en la tabla 'usuario_consumidor'  si existe una cuenta que comparta las caracteristicas denominadas

    # Ejecuto las consultas y le paso de parametros los datos recibidos del front
    cursor.execute(qsql_usr_consumidor,(body_request["usr"],body_request["pss"]))
    usuario_cosumidor_existente=cursor.fetchone()                                               # Almaceno la primera fila del resultado de la consulta en la variable 'usuario_consumidor'
    
    cursor.execute(qsql_usr_comercio,(body_request["usr"],body_request["pss"]))
    usuario_comercio_existente=cursor.fetchone()                                                # Almaceno la primera fila del resultado de la consulta en la variable 'usuario_comercio'

    cursor.close()
    conn.close()
    if usuario_comercio_existente or usuario_cosumidor_existente:
        # Si se encontró un usuario del tipo comercio o consumidor con esa información
        return jsonify({"msg":"Ingreso exitoso"}),200
    else:
        # Si no se encontró ningun tipo de usuario que cumpliera con esa información en ninguna de las tablas.
        return jsonify({"ERROR":"No se encontró ningun usuario con esa información"}),404
