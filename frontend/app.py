from flask import Flask, request, render_template, redirect, session, url_for, flash, jsonify
import requests

app = Flask(__name__)
app.secret_key = "contra_ids"  # Necesario para usar session y flash

API_BACK = "http://0.0.0.0:8100"  # Dirección local del backend

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

<<<<<<< HEAD
@app.route("/restaurante")
def resto():
    return render_template("resto.html")

@app.route("/login", methods=['GET','POST'])
=======
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
>>>>>>> desarrollo
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        usuario = request.form["username"]
        contrasena = request.form["password"]

        try:
            response = requests.post(f"{API_BACK}/auth/usr", json={"usr": usuario, "pss": contrasena})
            data = response.json()
        except Exception as e:
            flash("Error de conexión con el servidor", "error")
            return redirect(url_for("login"))

        if response.status_code == 200 and data.get("msg") == "ingreso exitoso":
            session["usuario"] = usuario
            return redirect(url_for("home"))
        else:
            flash("Credenciales inválidas", "error")
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
