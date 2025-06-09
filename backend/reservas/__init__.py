# Este modulo hace que la carpeta 'reservas' trabaje como un paquete. Al importar el mismo se va a crear el blueprint 'reservas' y se van a registrar automaticamente las rutas asociadas al mismo
from flask import Blueprint

reservas_bp=Blueprint("reservas_bp",__name__)

from . import routes