from flask import Blueprint, render_template, redirect, session, url_for

routes_bp = Blueprint('routes_bp', __name__)

@routes_bp.route('/')
def home():
    return render_template(
        'home.html',
        rank_comercios=[],  # evita error de json
        comercios_destacados=[]  # evita errores en el for
    )

@routes_bp.route('/login')
def login():
    return render_template('login.html')

@routes_bp.route('/register')
def register():
    return render_template('register.html')

@routes_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('routes_bp.login'))

@routes_bp.route('/descubre/<int:indice_pag>', methods=['GET'], endpoint='descubre')
def descubre(indice_pag):
    return render_template(
        'descubre.html',
        total_comercios=0,
        total_paginas=1,
        pagina_actual=indice_pag,
        comercios=[]
    )

