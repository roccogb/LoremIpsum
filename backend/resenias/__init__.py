# Este modulo hace que la carpeta 'resenias' trabaje como un paquete. Al importar el mismo se va a crear el blueprint 'resenias' y se van a registrar automaticamente las rutas asociadas al mismo
from flask import Blueprint

resenias_bp=Blueprint("resenias_bp",__name__)

from . import routes