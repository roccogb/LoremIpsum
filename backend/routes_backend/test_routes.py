from flask import Blueprint, render_template

test_bp = Blueprint('test_bp', __name__)

@test_bp.route('/perfil')
def perfil():
    usuario = {
        'nombre_usuario': 'Rocco',
        'email_usuario': 'rocco@example.com',
        'fecha_creacion': '2024-09-15'
    }

    reservas = [
        {'nombre_restaurante': 'La Parrilla de Pepe', 'fecha': '2025-06-08', 'estado': 'Confirmada'},
        {'nombre_restaurante': 'Sushi Club', 'fecha': '2025-06-10', 'estado': 'Pendiente'}
    ]

    resenas = [
        {'nombre_restaurante': 'La Parrilla de Pepe', 'comentario': 'Excelente comida', 'puntaje': 5},
        {'nombre_restaurante': 'Pizza Loca', 'comentario': 'Bien, pero nada especial', 'puntaje': 3}
    ]

    return render_template("perfil_consumidor.html", usuario=usuario, reservas=reservas, resenas=resenas)
