from flask import Blueprint

favoritos_bp = Blueprint('favoritos_bp', __name__)

from . import routes
# Este modulo inicializa el blueprint de favoritos y lo importa para que las rutas sean accesibles.
