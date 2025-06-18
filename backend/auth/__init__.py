from flask import Blueprint

auth_bp = Blueprint("auth_bp", __name__, template_folder="../../frontend/templates")

from . import routes
