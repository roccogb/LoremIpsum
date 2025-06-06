# Modulo que va a establecer a la carpeta 'routes-backend' como un paquete
from reservas import reservas_bp
from comercios import comercios_bp
from auth import auth_bp

# Esta funcion va a registrar cada blueprint en una aplicacion Flask con un prefijo
def register_routes(app):
    app.register_blueprint(reservas_bp, url_prefix="/reserva")
    app.register_blueprint(comercios_bp,url_prefix="/comercio")
    app.register_blueprint(auth_bp, url_prefix='/auth')
