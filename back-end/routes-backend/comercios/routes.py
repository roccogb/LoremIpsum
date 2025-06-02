# Modulo que va a contener la definicion del blueprint 'Comercios' y el conjunto de servicios vinculado a el
from flask import jsonify
from . import comercios_bp
from database.db import get_connection
         
# Endpoint que va a retornar TODA la información de los comercios. La misma será retornada en formato JSON
@comercios_bp.route("/")
def get_comercios():
    conn=get_connection()                   # Me conecto al servidor MySQL y a la BDD
    # Creo un cursor para así poder ejecutar sentencias SQL. El parametro dictionary hace que cada vez que haga una consulta a la BDD, me devuelva los datos como diccionarios facilitando asi la transformación de los mismos a JSON
    cursor=conn.cursor(dictionary=True)
    comercios=cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(comercios),200

# Endpoint que va a retornar TODA la información de un comercio. La misma será retornada en formato JSON
@comercios_bp.route("/<int:id_comercio>")
def get_comercio(id_comercio):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    #Parametrizo la consulta, esto va a mejorar la seguridad y la legibilidad del código
    sql="SELECT * FROM comercios WHERE id_comercio=%s"      # Sentencia SQL con un marcador que trabaja como parametro
    cursor.execute(sql,(id_comercio,))                      # Con el cursor ejecuto la sentencia y de segundo parametro le paso una tupla con los parametros a utilizar

    comercio_encontrado=cursor.fetchone()                   # El método fetchone va a retornar la primera fila del resultado de la consulta

    cursor.close()
    conn.close()
    if not comercio_encontrado:
        # Si no se encontró ningun comercio bajo ese ID, retorno un código 404
        return jsonify({"ERROR":"Comercio no encontrado"}),404
    else:
        # Si se encontró un comercio bajo ese ID
        return jsonify(comercio_encontrado),200
    
# Endpoint que va a retornar información de la BDD de un comercio siguiendo un patrón pasado por parametro dinamico. Ej: 'retornar toda la información de los comercios con tipo de cocina china'
@comercios_bp.route("/<filtro>/<valor>")
def get_comercios_filter(filtro,valor):
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)

    #Parametrizo la consulta, brindando asi mejor seguridad y legibilidad al código
    sql="SELECT * FROM comercios WHERE %s=%s"
    cursor.execute(sql,(filtro,valor))

    comercios_filtrados=cursor.fetchall()                   # El método fetchall va a retornar todas las filas del resultado de la consulta
    cursor.close()
    conn.close()
    if not comercios_filtrados:
        # Si no encontró comercios que cumplan con el filtro
        return jsonify({"ERROR":"No existen comercios que compartan esa caracteristica"}),404
    else:
        # Si se encontraron comercios que cumplan con el filtro
        return jsonify(comercios_filtrados),200