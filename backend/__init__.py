from backend.reservas import reservas_bp
from backend.comercios import comercios_bp
from backend.auth import auth_bp
from backend.favoritos import favoritos_bp
from backend.resenias import review_bp

def register_routes(app):
    app.register_blueprint(reservas_bp, url_prefix="/reserva")
    app.register_blueprint(comercios_bp, url_prefix="/comercio")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(favoritos_bp, url_prefix="/favs")
    app.register_blueprint(review_bp, url_prefix="/review")
