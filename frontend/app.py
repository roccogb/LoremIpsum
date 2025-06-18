from flask import Flask, request, render_template, redirect, session, url_for, flash, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from fextra import transformar_dias_comercio, transformar_horarios_comercio, transformar_tags_comercio, transformar_tp_comercio, transform_coords_dir
import requests
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"]="../backend/resources/uploads/comercios/"
app.secret_key = "contra_ids"  # Necesario para usar session y flash

API_BACK = "http://0.0.0.0:8100"                                        # Dirección local del backend


# Este endpoint va a retornar va a retornar una imagen almacenada en el backend.
@app.route("/resources/uploads/comercios/<imagen>")
def cargar_imagen(imagen):
    nombre_imagen_seguro=secure_filename(imagen)
    if os.path.exists( os.path.join(app.config["UPLOAD_FOLDER"], nombre_imagen_seguro)):
        return send_from_directory(app.config["UPLOAD_FOLDER"],nombre_imagen_seguro)
    else:
        return send_from_directory("frontend/static/img", "img_resto_defecto.jpg")

# Este endpoint va a guardar una imagen subida por el usuario
@app.route("/upload/<nombre_archivo>", methods=["POST"])
def subir_imagen():
    pass

# Pagina de inicio
@app.route("/")
def home():
    response=requests.get(f"{API_BACK}/comercio/filtrar",json={"tipo_cocina":"null","categoria":"null","calificacion":"desc",
                                                                         "horarios":[],"etiquetas":[],"dias":[]})
    
    # Obtener favoritos del usuario si está logueado
    id_favoritos = []
    if "datos_usuario" in session and session["tipo_usuario"] == "consumidor":
        id_usr = session.get("datos_usuario")["id_usr"]
        try:
            fav_response = requests.get(f"{API_BACK}/favs/detallado/{id_usr}")
            if fav_response.status_code == 200:
                favoritos_data = fav_response.json()
                # Extraer solo los IDs de comercios favoritos
                id_favoritos = [fav['id_comercio'] for fav in favoritos_data]
        except requests.RequestException:
            # Si hay error al obtener favoritos, continuar sin ellos
            id_favoritos = []
    
    if response.status_code == 200:
        comercios_rank_bdd=list(response.json())
        top_comercios=[]
        comercios_destacados=[]
        if len(comercios_rank_bdd) >= 3:
            top_comercios=comercios_rank_bdd[:3]
            
            if len(comercios_rank_bdd) >= 9:
                comercios_destacados=comercios_rank_bdd[3:9]
            else:
                comercios_destacados=comercios_rank_bdd[3:]

        return render_template("home.html", comercios_destacados=comercios_destacados, rank_comercios=top_comercios, id_favoritos=id_favoritos)
    else:
        return "Error al obtener los comercios desde el backend", 500

# Endpoint que va a permitir realizar una busqueda individual de un comercio
@app.route("/buscar", methods=["POST"])
def buscar_comercio():
    nombre_comercio=request.form.get("buscador")
    response = requests.get(f"{API_BACK}/comercio/get", json={"id_comercio":"null","nombre_comercio":nombre_comercio.title()})
    if response.status_code == 200:
        comercio_encontrado=response.json()
        return redirect(url_for("resto", id_comercio=comercio_encontrado["id_comercio"]))
    return redirect(url_for("home"))

# Este endpoint va a renderizar la página de descubre. En la misma se presentarán todos los comercios registrados y las herramientas necesarias para navegar en estos mismos, como; filtros,paginación,etc.
# El párametro dinamico recibido será el indice de la pagina actual renderizada
@app.route("/descubre/<int:indice_pag>", methods=["GET","POST"])
def descubre(indice_pag):
    inicio = indice_pag * 9
    if request.method == "POST":
        tipo_cocina=request.form.get("tipo_cocina","null")
        categoria=request.form.get("categoria","null")
        calificacion=request.form.get("orden_calificacion","null")
        horarios=request.form.getlist("horarios[]")
        etiquetas=request.form.getlist("etiquetas[]")            
        dias=request.form.getlist("dias[]")

        response=requests.get(f"{API_BACK}/comercio/filtrar", 
                               json={"tipo_cocina":tipo_cocina,"categoria":categoria,"horarios":horarios,
                                     "calificacion":calificacion,"etiquetas":etiquetas, "dias":dias})
    elif request.method == "GET":
        response=requests.get(f"{API_BACK}/comercio/")

    if response.status_code == 200:
        comercios_bdd = list(response.json())
        total_comercios = len(comercios_bdd)
        fin = min(inicio + 9, total_comercios)
    
        total_paginas = (total_comercios - 1) // 9
        
        # Si el índice pedido es mayor que las páginas disponibles
        if indice_pag > total_paginas:
            return redirect(url_for("descubre", indice_pag=total_paginas))
            
        return render_template("descubre.html", 
                            comercios=comercios_bdd[inicio:fin],
                            total_comercios=total_comercios,
                            pagina_actual=indice_pag,
                            total_paginas=total_paginas)
    else:
        return render_template("descubre.html",comercios=[])

# Página del restaurante seleccionado
@app.route("/restaurante/<int:id_comercio>")
def resto(id_comercio):
    #Petición al backend para obtener los detalles del comercio.
    if id_comercio <= 0:
        return redirect(url_for("home"))
    
    # Obtener favoritos del usuario si está logueado
    id_favoritos = []
    if "datos_usuario" in session and session["tipo_usuario"] == "consumidor":
        id_usr = session.get("datos_usuario")["id_usr"]
        try:
            fav_response = requests.get(f"{API_BACK}/favs/detallado/{id_usr}")
            if fav_response.status_code == 200:
                favoritos_data = fav_response.json()
                # Extraer solo los IDs de comercios favoritos
                id_favoritos = [fav['id_comercio'] for fav in favoritos_data]
        except requests.RequestException:
            # Si hay error al obtener favoritos, continuar sin ellos
            id_favoritos = []

    response = requests.get(f"{API_BACK}/comercio/get", json={"id_comercio":id_comercio,"nombre_comercio":""})
    if response.status_code == 200:
        comercio_bdd = response.json()

        dias_abiertos=transformar_dias_comercio(comercio_bdd["dias"])
        etiquetas_comercio=transformar_tags_comercio(comercio_bdd["etiquetas"])
        categoria_comercio=comercio_bdd["categoria"].capitalize()
        tipo_cocina_comercio=transformar_tp_comercio(comercio_bdd["tipo_cocina"])
        horarios_disponible=transformar_horarios_comercio(comercio_bdd["horarios"])

        # Sacar
        if type(comercio_bdd["calificacion"]) == float:
            comercio_bdd["calificacion"]=round(comercio_bdd["calificacion"])

        response_resenias=requests.get(f"{API_BACK}/review/com/{id_comercio}")

        resenias_data=[]
        if response_resenias.status_code == 200:
            resenias_data=response_resenias.json()

        return render_template("resto.html", comercio=comercio_bdd, resenias=resenias_data, id_favoritos=id_favoritos,
                                             dias=dias_abiertos, etiquetas=etiquetas_comercio,categoria=categoria_comercio,
                                             tipo_cocina=tipo_cocina_comercio, horarios=horarios_disponible)
    else:
        # Redirigir al home. 
        flash("Comercio no encontrado")
        return redirect(url_for("home"))

# Este endpoint le va a permitir al usuario, de tipo consumidor, realizar una reserva
@app.route("/realizar_reserva", methods=["POST"])
def reservar():
    if "datos_usuario" not in session or session.get("tipo_usuario") != "consumidor":
        flash("Solo los usuarios registrados que sean consumidores pueden realizar reservas.")
        return redirect(url_for("login"))
    else:
        # Recibe los datos del formulario de reserva.
        id_comercio = request.form.get("id_comercio")
        nombre_bajo_reserva = request.form.get("nombre_bajo_reserva")
        email = request.form.get("email")
        telefono = request.form.get("telefono")
        cant_personas = request.form.get("cant_personas")
        fecha_reserva = request.form.get("fecha_reserva")
        hora_reserva = request.form.get("hora_reserva")
        solicitud_especial = request.form.get("solicitud_especial", "")

        # Envía los datos al backend para crear la reserva.
        response = requests.post(f"{API_BACK}/reserva/crear", json={
            "id_usr": session.get("id_usr"),
            "id_comercio": id_comercio,
            "nombre_bajo_reserva": nombre_bajo_reserva,
            "email": email,
            "telefono": telefono,
            "cant_personas": cant_personas,
            "fecha_reserva": fecha_reserva,
            "solicitud_especial": solicitud_especial,
            "estado_reserva": False
        })

        if response.status_code == 200:
            flash("Reserva creada exitosamente", "success")

# Pagina de ayuda
@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")

# Este endpoint va a manejar la carga de perfiles si el usuario esta logeado
@app.route("/perfil")
def manag_perfiles():
    if "datos_usuario" not in session:
        return redirect(url_for("login"))
    else:
        if session.get("tipo_usuario") == "consumidor":

            response_reservas=requests.get(f"{API_BACK}/reserva/usr/{session.get("datos_usuario")["id_usr"]}")
            response_resenias=requests.get(f"{API_BACK}/review/usr/{session.get("datos_usuario")["id_usr"]}")
            response_favs=requests.get(f"{API_BACK}/favs/detallado/{session.get("datos_usuario")["id_usr"]}")

            data_reservas=[]
            data_resenias=[]
            data_fav=[]

            if response_reservas.status_code == 200:
                data_reservas=list(response_reservas.json())
            
            if response_resenias.status_code == 200:
                data_resenias=list(response_resenias.json())

            if response_favs.status_code == 200:
                data_fav=list(response_favs.json())

            return render_template("perfil_consumidor.html",
                                    usuario=session.get("datos_usuario"),
                                    reservas=data_reservas,
                                    resenias=data_resenias,
                                    favoritos=data_fav)
        elif session.get("tipo_usuario") == "comercio":
            response_reservas=requests.get(f"{API_BACK}/reserva/comercio/{session.get("datos_comercio")["id_comercio"]}")
            response_resenias=requests.get(f"{API_BACK}/review/com/{session.get("datos_comercio")["id_comercio"]}")

            data_reservas=[]
            data_resenias=[]
            direccion=transform_coords_dir([session.get("datos_comercio")["latitud"], session.get("datos_comercio")["longitud"]])

            if response_reservas.status_code == 200:
                data_reservas=list(response_reservas.json())
            
            if response_resenias.status_code == 200:
                data_resenias=list(response_resenias.json())

            return render_template("perfil_comerciante.html",
                                   usuario=session.get("datos_usuario"),
                                   datos_comercio=session.get("datos_comercio"),
                                   resenias=data_resenias,
                                   reservas=data_reservas, 
                                   ubicacion=direccion)

# Login de usuario
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        pswd = request.form["password"]

        try:
            # Primero intentamos autenticar como usuario consumidor
            response_consumidor = requests.post(f"{API_BACK}/auth/consumidor", 
                                              json={"email": email, "pss": pswd})
            
            if response_consumidor.status_code == 200:
                data_consumidor = response_consumidor.json()

                session["tipo_usuario"] = "consumidor"
                session["datos_usuario"] = {
                    "id_usr": data_consumidor.get("id_usr"),
                    "nombre_apellido": data_consumidor.get("nombre_apellido"),
                    "usuario": data_consumidor.get("usuario"),
                    "email_usuario":data_consumidor.get("email_usuario"),
                    "numero_telefono": data_consumidor.get("numero_telefono"),
                    "fecha_creacion":data_consumidor.get("fecha_creacion"),
                    "cant_reservas_canceladas": data_consumidor.get("cant_reservas_canceladas", 0)
                }
                return redirect(url_for("home"))
            
            # Si no es consumidor, intentamos autenticar como comerciante
            response_comercio = requests.post(f"{API_BACK}/auth/comercio", 
                                            json={"email": email, "pss": pswd})
            
            if response_comercio.status_code == 200:
                data_comercio = response_comercio.json()

                session["tipo_usuario"] = "comercio"
                session["datos_usuario"] = {
                        "id_usr_comercio": data_comercio.get("id_usr_comercio"),
                        "nombre_apellido": data_comercio.get("nombre_apellido"),
                        "DNI": data_comercio.get("DNI"),
                        "CUIT": data_comercio.get("CUIT"),
                        "email_usuario": data_comercio.get("email_usuario"),
                        "fecha_creacion": data_comercio.get("fecha_creacion")
                    }
                session["datos_comercio"] = {
                        "id_comercio": data_comercio.get("id_comercio"),
                        "nombre_comercio": data_comercio.get("nombre_comercio"),
                        "categoria": data_comercio.get("categoria"),
                        "tipo_cocina": data_comercio.get("tipo_cocina"),
                        "telefono": data_comercio.get("telefono"),
                        "latitud": data_comercio.get("latitud"),
                        "longitud": data_comercio.get("longitud"),
                        "calificacion": data_comercio.get("calificacion", 0.0),
                        "dias": transformar_dias_comercio(data_comercio.get("dias")),
                        "horarios": transformar_horarios_comercio(data_comercio.get("horarios")),
                        "etiquetas": transformar_tags_comercio(data_comercio.get("etiquetas")),
                        "ruta_imagen": data_comercio.get("ruta_imagen"),
                        "pdf_menu_link": data_comercio.get("pdf_menu_link")
                    }
                return redirect(url_for("home"))
            
            flash("Credenciales inválidas", "error")
            return redirect(url_for("login"))
            
        except Exception as e:
            flash("Error de conexión con el servidor", "error")
            return redirect(url_for("login"))     
    return render_template("login.html")


# FALTA SOLUCIONAR COMO SUBIR LA IMAGEN QUE SELECCIONA EL USUARIO
# Cuando el usuario pulse el boton 'Subir imagen' envie una peticion a otro endpoint diferente que va a guardar la imagen y que en este solamente se grabe la ruta de la imagen
# Registrar usuario
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Endpoint para renderizar la página de registro"""
    if request.method == 'POST':
        form = request.form
        if form.get("tipo_usuario") == "consumidor":
            nombre_consumidor = form.get("nombre_consumidor")
            apellido_consumidor = form.get("apellido_consumidor")
            usuario_consumidor = form.get("usuario_consumidor")
            email_consumidor = form.get("email_consumidor")
            telefono_consumidor = form.get("telefono_consumidor")
            password_consumidor = form.get("password_consumidor")
            response = requests.post(f"{API_BACK}/auth/register", 
                                            json={
                                                "tipo_usuario":form.get("tipo_usuario"),
                                                "nombre_consumidor" : nombre_consumidor,
                                                "apellido_consumidor" : apellido_consumidor,
                                                "usuario_consumidor" : usuario_consumidor,
                                                "email_consumidor": email_consumidor,
                                                "telefono_consumidor" : telefono_consumidor,
                                                "password_consumidor": password_consumidor
                                                  })
        else:
            nombre_comercio = form.get("name_bss")
            tel_comercio = form.get("tel_bss")
            dir_comercio = form.get("dir_bss")
            lkmenu_comercio = form.get("lkm_bss")
            categoria = form.get("categoria")
            tipo_cocina = form.get("tipo_cocina")
            email_responsable = form.get("email_bss")
            dias = form.getlist("dias[]")
            horarios = form.getlist("horarios[]")
            etiquetas = form.getlist("etiquetas[]")
            dni_responsable = form.get("dni_responsable_bss")
            cuit_responsable = form.get("cuit_responsable_bss")
            nombre_responsable = form.get("nr_bss")
            contrasena_usr_comercio = form.get("p_r_bss")

            # Falta agregar la implementacion de subir la imagen

            if "0-24" in horarios:
                horarios=["0-24"]

            response = requests.post(f"{API_BACK}/auth/register", 
                                            json={
                                                "tipo_usuario":form.get("tipo_usuario"),
                                                "nombre_comercio" : nombre_comercio,
                                                "tel_comercio" : tel_comercio,
                                                "dir_comercio" : dir_comercio,
                                                "lkmenu_comercio" : lkmenu_comercio,
                                                "categoria" : categoria,
                                                "tipo_cocina" : tipo_cocina,
                                                "email_responsable" : email_responsable,
                                                "dias" : dias,
                                                "horarios" : horarios,
                                                "etiquetas" : etiquetas,
                                                "dni_responsable" : dni_responsable,
                                                "cuit_responsable" : cuit_responsable,
                                                "nombre_responsable" : nombre_responsable,
                                                "contrasena_usr_comercio" : contrasena_usr_comercio
                                                  })
        if response.status_code == 200:
            flash("Se registro el usuario correctamente","message")
            return redirect('/login')
        flash(f"{response.json()["error"]}","warning")
    else:
        return render_template("register.html")

# Marcar un comercio como favorito.
@app.route("/click_fav/<int:id_comercio>", methods=["POST"])
def click_fav(id_comercio):
    if "datos_usuario" not in session or session["tipo_usuario"] != "consumidor":
        return jsonify({"success": False, "error": "No autorizado"}), 401

    id_usr = session.get("datos_usuario")["id_usr"]
    
    try:
        response = requests.post(f"{API_BACK}/favs/alternar", json={"id_comercio": id_comercio, "id_usr": id_usr})
        
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                "success": True, 
                "favorito": data.get("marca", False),
                "message": "Favorito actualizado correctamente"
            })
        else:
            return jsonify({"success": False, "error": "Error del servidor backend"}), 500
            
    except requests.RequestException as e:
        return jsonify({"success": False, "error": "Error de conexión con el backend"}), 500
 
# Logout
@app.route("/logout")
def logout():
    if "datos_usuario" in session:
        session.clear()
        return redirect(url_for("home"))
    else:
        flash("Primero debe iniciar sesión","message")
        return redirect(url_for("home"))

# Este endpoint va a implementar las funcionalidades respectivas a dejar una reseña en un comercio
@app.route("/realizar_review/<int:id_comercio>/<int:id_reserva>", methods=["GET","POST"])
def realizar_review(id_comercio, id_reserva):
    if "datos_usuario" in session and session.get("tipo_usuario") == "consumidor":
        response_comercio=requests.get(f"{API_BACK}/comercio/get", json={"id_comercio":id_comercio,"nombre_comercio":""})
        response_reserva=requests.get(f"{API_BACK}/reserva/{id_reserva}")
        if response_comercio.status_code == 200 and response_reserva.status_code == 200:
            data_comercio=response_comercio.json()
            data_reserva=response_reserva.json()
            if data_reserva["estado_reserva"]:
                if request.method == "GET":
                    return render_template("review.html", comercio=data_comercio, identificador_reserva=id_reserva)
                else:
                    text_comentario=request.form.get("comentario")
                    calificacion_resto=request.form.get("calificacion")

                    response=requests.post(f"{API_BACK}/review/crear", json={"id_usr":session.get("id_usr"),"id_reserva":id_reserva,
                                                                            "id_comercio":data_comercio["id_comercio"], 
                                                                            "calificacion":calificacion_resto, "comentario":text_comentario})
                    if response.status_code == 200:
                        flash("Reseña realizada con éxito","message")
                        return redirect(url_for("resto", id_comercio=data_comercio["id_comercio"]))
            else:
                flash("No se puede realizar una reseña, estado de la reserva pendiente")
                return redirect(url_for("manag_perfiles"))
        else:
            return jsonify({"ERROR":"Reserva o comercio inexistente"}),404

if __name__ == "__main__":
    app.run(host="localhost", port=8200, debug=True)
