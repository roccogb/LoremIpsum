# Modulo que va a ejecutar el back-end de FoodyBA
from flask import Flask
from routes_backend import register_routes

app = Flask(__name__)
app.config["SECRET_KEY"] = 'tp-ids-2025'

register_routes(app)  # Registro los blueprints creados en mi app Flask

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8100, debug=True)
