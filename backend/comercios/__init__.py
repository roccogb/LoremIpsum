# Este modulo hace que la carpeta 'comercios' trabaje como paquete. Al importar el mismo se va a crear el blueprint 'comercios' y se van a registrar automaticamente las rutas asociadas al mismo
from flask import Blueprint

comercios_bp=Blueprint("comercios_bp",__name__)     

from . import routes        