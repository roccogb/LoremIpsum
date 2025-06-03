# Modulo que va a establecer a la carpeta 'routes-backend' como un paquete.
from comercios import comercios_bp

# Esta funcion va a registrar cada blueprint en una aplicacion Flask con un prefijo
def register_routes(app):
    app.regiter_blueprint(comercios_bp,url_prefix="/comercio")