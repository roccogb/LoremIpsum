from flask import Flask, request, render_template, redirect, session, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from fextra import transformar_dias_comercio, transformar_horarios_comercio, transformar_tags_comercio, transformar_tp_comercio
import requests
import os

app = Flask(__name__)
app.secret_key = "contra_ids"  # Necesario para usar session y flash

API_BACK = "http://0.0.0.0:8100"                                        # Dirección local del backend
UPLOAD_FOLDER = os.path.join(os.getcwd(),'static','media', 'img')       # Carpeta donde van a ir todas las imagenes

# Pagina de inicio
@app.route("/")
def home():
    response=requests.get(f"{API_BACK}/comercio/filtrar",json={"tipo_cocina":"null","categoria":"null","calificacion":"desc",
                                                                         "horarios":[],"etiquetas":[],"dias":[]})
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

        return render_template("home.html", comercios_destacados=comercios_destacados, rank_comercios=top_comercios)
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
    
    response = requests.get(f"{API_BACK}/comercio/get", json={"id_comercio":id_comercio,"nombre_comercio":""})
    if response.status_code == 200:
        comercio_bdd = response.json()

        comercio_bdd["dias"]=transformar_dias_comercio(comercio_bdd["dias"])
        comercio_bdd["etiquetas"]=transformar_tags_comercio(comercio_bdd["etiquetas"])
        comercio_bdd["categoria"]=comercio_bdd["categoria"].capitalize()
        comercio_bdd["tipo_cocina"]=transformar_tp_comercio(comercio_bdd["tipo_cocina"])
        comercio_bdd["horarios"]=transformar_horarios_comercio(comercio_bdd["horarios"])

        if type(comercio_bdd["calificacion"]) == float:
            comercio_bdd["calificacion"]=round(comercio_bdd["calificacion"])

        return render_template("resto.html", comercios=comercio_bdd)
    else:
        # Redirigir al home. 
        flash("Comercio no encontrado")
        return redirect(url_for("home"))

# Este endpoint le va a permitir al usuario, de tipo consumidor, realizar una reserva
@app.route("/reservar", methods=["POST"])
def reservar():
    if "email" not in session:
        flash("Debes iniciar sesión para reservar")
        return redirect(url_for("login"))
    else:
        # Recibe los datos del formulario de reserva.
        id_comercio = request.form.get("id_comercio")
        nombre_bajo_reserva = request.form.get("nombre_bajo_reserva")
        email = request.form.get("email")
        telefono = request.form.get("telefono")
        cant_personas = request.form.get("cant_personas")
        fecha_reserva = request.form.get("fecha_reserva")
        #hora_reserva = request.form.get("hora_reserva")
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

# Este endpoint le va a permitir al usuario, de tipo consumidor, realizar una reseña sobre un comercio al cual el mismo haya ido
@app.route("/reseñar", methods=["POST"])
def agregar_resena():
    pass

# Pagina de ayuda
@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")

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
                session["email"] = email
                session["tipo_usuario"] = "consumidor"
                session["datos_usuario"] = {
                    "id_usr": data_consumidor.get("id_usr"),
                    "nombre_apellido": data_consumidor.get("nombre_apellido"),
                    "email_usuario": data_consumidor.get("email_usuario"),
                    "numero_telefono": data_consumidor.get("numero_telefono"),
                    "cant_reservas_canceladas": data_consumidor.get("cant_reservas_canceladas", 0)
                }
                return redirect(url_for("home"))
            
            # Si no es consumidor, intentamos autenticar como comerciante
            response_comercio = requests.post(f"{API_BACK}/auth/comercio", 
                                            json={"email": email, "pss": pswd})
            
            if response_comercio.status_code == 200:
                data_comercio = response_comercio.json()
                session["email"] = email
                session["tipo_usuario"] = "comercio"
                session["datos_usuario"] = {
                        "id_usr_comercio": data_comercio.get("id_usr_comercio"),
                        "nombre_apellido": data_comercio.get("nombre_apellido"),
                        "DNI": data_comercio.get("DNI"),
                        "CUIT": data_comercio.get("CUIT"),
                        "email_usuario": data_comercio.get("email_usuario")
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
                        "dias": data_comercio.get("dias"),
                        "horarios": data_comercio.get("horarios"),
                        "etiquetas": data_comercio.get("etiquetas"),
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


# Register usuario
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Endpoint para renderizar la página de registro"""
    if request.method == 'POST':
        form = request.form
        if form.get("tipo_usuario") == "consumidor":
            nombre_consumidor = form.get("first_name")
            apellido_consumidor = form.get("last_name")
            usuario_consumidor = form.get("usr")
            email_consumidor = form.get("email")
            telefono_consumidor = form.get("mobile")
            password_consumidor = form.get("password")
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

            imagen=request.files.get("img_local")
            if not imagen or imagen.filename == "":
                ruta_img="media/img/img_resto_defecto.jpg"
            else:            
                nombre_archivo_seguro=secure_filename(imagen.filename)
                imagen.save( os.path.join(UPLOAD_FOLDER,nombre_archivo_seguro) )
                ruta_img=f"media/img/{nombre_archivo_seguro}"

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
                                                "contrasena_usr_comercio" : contrasena_usr_comercio,
                                                "ruta_img" : ruta_img
                                                  })
        if response.status_code == 200:
            flash("Se registro el usuario correctamente","message")
            return redirect('/login')
        flash(f"{response.json()["error"]}","warning")
    else:
        return render_template("register.html")

# Logout
@app.route("/logout")
def logout():
    session.pop("email", None)
    session.pop("tipo_usuario", None)
    session.pop("datos_usuario", None)
    return redirect(url_for("home"))

# Este endpoint va a implementar las funcionalidades respectivas a dejar una reseña en un comercio
@app.route("/realizar_review/<int:id_comercio>/<int:id_reserva>", methods=["GET","POST"])
def realizar_review(id_comercio, id_reserva):
    # if "email" in session and session.get("tipo_usuario") == "consumidor":
        response_comercio=requests.get(f"{API_BACK}/comercio/{id_comercio}")
        if response_comercio.status_code == 200:
            data_comercio=response_comercio.json()
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
                    return redirect(url_for("home"))
        else:
            return jsonify({"ERROR":"No se cargó la informacion del comercio"}),500

if __name__ == "__main__":
    app.run(host="localhost", port=8200, debug=True)
