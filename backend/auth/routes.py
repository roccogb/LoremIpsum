from flask import request, jsonify, render_template, redirect, flash, url_for, session
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

@auth_bp.route("/consumidor", methods=["POST"])
def auth_consumidor():
    """Endpoint para autenticar usuarios consumidores"""
    try:
        data = request.get_json()
        email = data.get("email")
        pswd = data.get("pss")
        
        conn = get_connection()
        if not conn:
            return jsonify({"msg": "Error de conexión a la base de datos"}), 500
        
        cursor = conn.cursor(dictionary=True)
        
        # Buscar usuario por nombre de usuario o email
        query = """
        SELECT *
        FROM usuario_consumidor 
        WHERE email_usuario = %s AND contrasena = %s
        """
        cursor.execute(query, (email, pswd))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if not user_data:
            return jsonify({"msg": "Usuario no encontrado"}), 404         
        else:
            
            return jsonify(user_data), 200
           
    except Exception as e:
        print(f"Error en auth_consumidor: {e}")
        return jsonify({"msg": "Error interno del servidor"}), 500


@auth_bp.route("/comercio", methods=["POST"])
def auth_comercio():
    """Endpoint para autenticar usuarios comerciantes"""
    try:
        data = request.get_json()
        email = data.get("email")  # Puede ser email o DNI
        pswd = data.get("pss")
       
        conn = get_connection()
        if not conn:
            return jsonify({"msg": "Error de conexión a la base de datos"}), 500
        
        cursor = conn.cursor(dictionary=True)
        
        # Buscar usuario comercio por email o DNI, y hacer JOIN con comercios
        query = """
        SELECT 
            uc.id_usr_comercio, uc.nombre_apellido, uc.DNI, uc.CUIT, 
            uc.email_usuario, uc.contrasena,
            c.id_comercio, c.ruta_imagen, c.nombre_comercio, c.categoria,
            c.tipo_cocina, c.telefono, c.latitud, c.longitud, 
            c.tiempo_de_creacion, c.pdf_menu_link, c.calificacion,
            c.dias, c.horarios, c.etiquetas
        FROM usuario_comercio uc
        LEFT JOIN comercios c ON uc.id_usr_comercio = c.id_usr_comercio
        WHERE uc.email_usuario = %s AND uc.contrasena = %s
        """
        cursor.execute(query, (email, pswd))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if not user_data:
            return jsonify({"msg": "Usuario no encontrado"}), 404
        else:
            return jsonify(user_data), 200
                    
    except Exception as e:
        print(f"Error en auth_comercio: {e}")
        return jsonify({"msg": "Error interno del servidor"}), 500

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('email')
    password = request.form.get('password')
    rol = request.form.get('rol')  # viene del form: consumidor o comercio

    conn = get_connection()
    if not conn:
        flash("Error de conexión con la base de datos")
        return redirect(url_for('auth_bp.login'))

    cursor = conn.cursor(dictionary=True)

    if rol == 'consumidor':
        query = """
        SELECT * FROM usuario_consumidor 
        WHERE email_usuario = %s AND contrasena = %s
        """
        cursor.execute(query, (email, password))
    else:
        query = """
        SELECT uc.*, c.nombre_comercio
        FROM usuario_comercio uc
        LEFT JOIN comercios c ON uc.id_usr_comercio = c.id_usr_comercio
        WHERE uc.email_usuario = %s AND uc.contrasena = %s
        """
        cursor.execute(query, (email, password))

    user_data = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user_data:
        flash("Credenciales incorrectas")
        return redirect(url_for('auth_bp.login'))

    # Guardar datos en la session
    session['rol'] = rol
    session['usuario'] = user_data.get('nombre_apellido') or user_data.get('nombre_usuario')
    session['email'] = user_data.get('email_usuario')

    # Redireccion segun rol
    if rol == 'consumidor':
        return redirect('/perfil/consumidor')
    else:
        return redirect('/perfil/comercio')
