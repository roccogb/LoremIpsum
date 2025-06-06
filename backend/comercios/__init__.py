# Este modulo hace que la carpeta 'comercios' trabaje como paquete. Al importar el mismo se va a crear el blueprint 'comercios' y se van a registrar automaticamente las rutas asociadas al mismo
from flask import Blueprint

# Defino el blueprint bajo el nombre 'comercios' y hago una referencia al modulo actual para así flask encuentra la definicio al mismo más facil
comercios_bp=Blueprint("comercios_bp",__name__)     

from . import routes        # Importo las rutas para registrarlas en el blueprint.