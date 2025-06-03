# Modulo que va a contener el conjunto de servicios vinculados al blueprint 'Comercios'
from flask import jsonify, request
from . import comercios_bp
from database.db import get_connection

# Funcion auxiliar para verificar si la información ingresada es valida. Para que la información que se ingresa sea considerada válida se deben cumplir las siguientes condiciones:
#               - 'nombre_comercio' -> No debe contener digitos
#               - 'categoria_comercio' -> Se tiene que haber seleccionado una categoría
#               - 'tipo_cocina' -> Se tiene que haber seleccionado un tipo de cocina
#               - 'email_comercio' -> El email ingresado debe seguir un patrón
#               - 'nombre_responsable_comercio' -> El nombre del responsable no debe contener digitos
#               - 'dni_responsable_comercio' -> El DNI deben ser un total de 8 digitos
#               - 'cuit_responsable_comercio' -> El CUIT del responsable debe contener 11 digitos
def verificar_data_comercio(nombre_comercio, categoria_comercio, tipo_cocina, direccion_comercio, email_comercio, nombre_responsable_comercio, dni_responsable_comercio, cuit_responsable_comercio):
    pass

# Endpoint que va a retornar TODA la información de los comercios. La misma será retornada en formato JSON
@comercios_bp.route("/")
def get_comercios():
    conn=get_connection()                               # Me conecto al servidor MySQL y a la BDD
    # Creo un cursor para así poder ejecutar sentencias SQL. El parametro dictionary hace que cada vez que haga una consulta a la BDD, me devuelva los datos como diccionarios facilitando asi la transformación de los mismos a JSON
    cursor=conn.cursor(dictionary=True)

    qsql_comercios="""SELECT * FROM comercios"""
    cursor.execute(qsql_comercios)                      # Ejecuto la consulta
    comercios=cursor.fetchall()                         # Almaceno todas las filas en la lista comercios.

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

# Endpoint que va a registrar un nuevo comercio en la BDD. La información del mismo será recibida a traves de un formulario
@comercios_bp.route("/agregar")
def add_comercio():
    nombre_comercio=request.form["name_bss"]
    categoria_comercio=request.form["categoria"]
    tipo_cocina=request.form["tipo_cocina"]
    direccion_comercio=request.form["dir_bss"]  #Convertir la direccion en coords
    email_comercio=request.form["email_bss"]
    nombre_responsable_comercio=request.form["nr_bss"]
    dni_responsable_comercio=request.form["dni_responsable_bss"]
    cuit_responsable_comercio=request.form["cuit_responsable_bss"]
    # Resolver el como almacenar el PDF que certifica la existencia del comercio

    if verificar_data_comercio(nombre_comercio,categoria_comercio,tipo_cocina,direccion_comercio, email_comercio, nombre_responsable_comercio, dni_responsable_comercio, cuit_responsable_comercio):
        pass
    else:
        return jsonify({"ERROR":"Error con los datos ingresados"}),400