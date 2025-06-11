from flask import Flask, request, render_template, redirect, session, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "contra_ids"  # Necesario para usar sesiones y flash

API_BACK = "http://127.0.0.1:8100"  # Dirección local del backend

# Pagina de inicio
@app.route("/")
def home():
    return render_template("home.html")

# Pagina de descubre
@app.route("/descubre")
def descubre():
    return render_template("descubre.html")

# Pagina de ayuda
@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")

#Prueba-> Pagina de review
@app.route("/review")
def review():
    return render_template("review.html")

# Login de usuario
@app.route("/login", methods=["GET", "POST"])
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
