from flask import Flask, request, render_template
import requests                 # Libreria para realizar peticiones HTTP

app=Flask(__name__)

API_BACK="http://localhost:8100"

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        # Si la petición recibida por el usuario es del tipo 'GET'
        return render_template("login.html")
    elif request.method == 'POST':
        # Si la petición recibida por el usuario es del tipo 'POST'
        usuario=request.form["username"]
        contrasena=request.form["password"]
        response=requests.post(f"{API_BACK}/auth/usr", json={"usr":usuario,"pss":contrasena})          # Envío una petición al backend para comprobar si el usuario ingresado existe en la BDD
        return response.json()                                                                         # Estructura de control que si el ingreso no es exitoso rediriga nuevamente al login

if __name__ == "__main__":
    app.run(host="localhost", port=8200, debug=True)