from flask import Flask
from auth.routes import auth_bp  # Importar el blueprint de autenticación

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "clave_ids"
    
    # Registrar blueprint de autenticación
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
