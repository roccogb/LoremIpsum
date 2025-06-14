from flask import Flask, request, render_template, redirect, session, url_for, flash, jsonify
import requests

app = Flask(__name__)
app.secret_key = "contra_ids"  # Necesario para usar session y flash

API_BACK = "http://192.168.1.6:8100"  # Dirección local del backend

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
        #Implementar template de error
        pass

# Este endpoint va a renderizar la página de descubre. En la misma se presentarán todos los comercios registrados y las herramientas necesarias para navegar en estos mismos, como; filtros,paginación,etc.
# El párametro dinamico recibido será el indice de la pagina actual renderizada
# Dividir el endpoint en dos partes donde la principal diferencia se va a encontrar en a que endpoint del back le realiza la peticion para conseguir la data
# POST -> Descubre con filtros aplicados.
# GET -> Descubre sin filtros.
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
@app.route("/restaurante")
def resto():
    return render_template("resto.html")
    
# Pagina de ayuda
@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")

# Login de usuario
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form["email"]
        pswd = request.form["password"]

        try:
            # Primero intentamos autenticar como usuario consumidor
            response_consumidor = requests.post(f"{API_BACK}/auth/consumidor", 
                                              json={"email": email, "pss": pswd})
            
            if response_consumidor.status_code == 200:
                data_consumidor = response_consumidor.json()
                    # Es un usuario consumidor, guardamos sus datos en la sesión
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
                    # Es un usuario comerciante, guardamos sus datos y los de su comercio
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
            
            # Si ninguno de los dos tipos de autenticación funciona
            flash("Credenciales inválidas", "error")
            return redirect(url_for("login"))
            
        except Exception as e:
            flash("Error de conexión con el servidor", "error")
            return redirect(url_for("login"))

# Register usuario
@app.route("/register")
def register():
    return render_template("register.html")

# Logout
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="localhost", port=8200, debug=True)
