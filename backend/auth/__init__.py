from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__)

from . import routes  # importa las rutas para registrarlas
