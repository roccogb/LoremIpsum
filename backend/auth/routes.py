from flask import request, jsonify
from . import auth_bp
from database.db import get_connection
from fextra import transform_dir_coords
import datetime

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
        return jsonify({"msg": "Error interno del servidor auth consumidor"}), 500

# Este endpoint va a autenticar usuarios comerciantes
@auth_bp.route("/comercio", methods=["POST"])
def auth_comercio():
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
        return jsonify({"msg": "Error interno del servidor auth_comercio"}), 500

# Este endpoint va a registrar un usuario nuevo. Dependiendo el tipo del usuario va a realizar diferentes acciones
@auth_bp.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        
        tipo_usuario = data.get('tipo_usuario')
        
        conn = get_connection()
        if not conn:
            return jsonify({"error": "Error de conexión a la base de datos"}), 500
        
        cursor = conn.cursor()
        
        if tipo_usuario == "consumidor":
                return register_consumidor(data, cursor, conn)
        elif tipo_usuario == "comercio":
                return register_comercio(data, cursor, conn)
                
        cursor.close()
        conn.close()
            
    except Exception as e:
        print(f"Error general: {str(e)}")
        return jsonify({"error": "Error interno del servidor register user"}), 500

def register_consumidor(data, cursor, conn):
    """Registra un usuario consumidor"""
    
    nombre = data.get('nombre_consumidor', '').strip()
    apellido = data.get('apellido_consumidor', '').strip()
    usuario = data.get('usuario_consumidor', '').strip()
    email = data.get('email_consumidor', '').strip()
    telefono = data.get('telefono_consumidor', '').strip()
    password = data.get('password_consumidor', '').strip()
    
    # Validaciones básicas
    if not all([nombre, apellido, usuario, email, telefono, password]):
        return jsonify({"error": "Ocurrió un error al ingresar los datos, verifique que todos los campos esten completos"}), 400
    
    nombre_completo = f"{nombre} {apellido}" 
    telefono_int = int(telefono)
    
    # Verificar si el usuario ya existe
    cursor.execute("""
        SELECT * FROM usuario_consumidor 
        WHERE usuario = %s AND email_usuario = %s AND numero_telefono = %s
    """, (usuario, email, telefono_int))
    
    if cursor.fetchone():
        return jsonify({"error": "Usuario, email o teléfono ya registrado"}), 409
    
    else :  
        # Insertar nuevo consumidor
        insert_query = """
            INSERT INTO usuario_consumidor 
            (nombre_apellido, usuario, email_usuario, contrasena, numero_telefono) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (nombre_completo, usuario, email, password, telefono_int))
        conn.commit()
    
    return jsonify({
        "message": "Consumidor registrado exitosamente",
    }), 200

def register_comercio(data, cursor, conn):
    """Registra un usuario comercio y su comercio asociado"""

    nombre_responsable = data.get('nombre_responsable', '').strip()
    dni_responsable = data.get('dni_responsable', '0').strip()
    cuit_responsable = data.get('cuit_responsable', '0').strip()
    email_responsable = data.get('email_responsable', '').strip()
    contrasena = data.get('contrasena_usr_comercio', '').strip()
    
    # Extraer datos del comercio
    nombre_comercio = data.get('nombre_comercio', '').strip()
    tel_comercio = data.get('tel_comercio', '0').strip()
    lat,lng = transform_dir_coords(data.get('dir_comercio', '').strip())
    lkmenu_comercio = data.get('lkmenu_comercio', '').strip()
    categoria = data.get('categoria', '').strip()
    tipo_cocina = data.get('tipo_cocina', '').strip()
    ruta_img = data.get('ruta_img')
    
    # Arrays que vienen del frontend
    dias = data.get('dias', [])
    horarios = data.get('horarios', [])
    etiquetas = data.get('etiquetas', [])
    
    if not all([nombre_responsable, dni_responsable, cuit_responsable, 
                email_responsable, contrasena, nombre_comercio,
                tel_comercio,lat,lng,lkmenu_comercio,
                categoria,tipo_cocina,dias,horarios]):
        return jsonify({"error": "Ocurrió un error al ingresar los datos, verifique que todos los campos esten completos"}), 400

    dni_int = int(dni_responsable)
    cuit_int = int(cuit_responsable)
    telefono_int = int(tel_comercio)
    
    # Convertir arrays a strings para almacenar en la BD
    dias_str = str(dias) if dias else str([])
    horarios_str= str(horarios) if horarios else str([])
    etiquetas_str = str(etiquetas) if etiquetas else str([])
    
    # Metodo para hacer mas de 2 consultas post sql que esten conectadas x id
    conn.start_transaction()
    
    #  Verificar si el usuario comercio ya existe en la tabla comercio
    cursor.execute("""
        SELECT * FROM usuario_comercio 
        WHERE DNI = %s AND CUIT = %s AND email_usuario = %s
    """, (dni_int, cuit_int, email_responsable))
    
    if cursor.fetchone():
        return jsonify({"error": "DNI, CUIT o email ya registrado"}), 409
    
    # Insertar usuario comercio a la tabla comercio
    insert_user_query = """
        INSERT INTO usuario_comercio 
        (nombre_apellido, DNI, CUIT, email_usuario, contrasena) 
        VALUES (%s, %s, %s, %s, %s)
    """
    
    cursor.execute(insert_user_query, (
        nombre_responsable, dni_int, cuit_int, email_responsable, contrasena
    ))
    
    id_usr_comercio = cursor.lastrowid
    
    #  Verificar si el id_usr_comercio del comercio ya existe en la tabla
    cursor.execute("SELECT * FROM comercios WHERE id_usr_comercio = %s", (id_usr_comercio,))
    if cursor.fetchone():
        return jsonify({"error": "id_usr_comercio del comercio ya registrado"}), 409
    
    #  Insertar comercio a tabla comercio
    insert_comercio_query = """
        INSERT INTO comercios 
        (id_usr_comercio, ruta_imagen, nombre_comercio, categoria, tipo_cocina,telefono, latitud, longitud, tiempo_de_creacion,pdf_menu_link, calificacion, dias, horarios, etiquetas) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    cursor.execute(insert_comercio_query, (
        id_usr_comercio, ruta_img, nombre_comercio, categoria, tipo_cocina,
        telefono_int,lat,lng,datetime.datetime.now(),lkmenu_comercio,0,dias_str, horarios_str, etiquetas_str
    ))
    
    conn.commit()
    return jsonify({
        "message": "Comercio registrado exitosamente",
    }), 200
    