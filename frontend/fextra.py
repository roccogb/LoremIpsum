from ast import literal_eval

# Funciones auxiliares que van a transformar los datos de la BDD para que sean visibles en el front
def transformar_horarios_comercio(str_list_horarios):
    horarios_visibles={"7-11":"Desayuno(7:00-11:00)","12-15":"Almuerzo(12:00-15:00)",
            "16-18":"Merienda(16:00-18:00)","19-23":"Cena(19:00-23:00)",
            "23-5":"Nocturno(23:00-05:00)","0-24":"24h"}
    list_horarios=[ horarios_visibles[hor] for hor in literal_eval(str_list_horarios)]
    return list_horarios

def transformar_tags_comercio(str_list_tags):
    etiquetas_visibles={"musica_vivo":"Musica en vivo", "happy_hour":"Happy hour",
             "vegetariano":"Vegetariano","vegano":"Vegano",
             "sin_gluten":"Sin Gluten", "apto_mascotas":"Apto para mascotas",
             "wifi":"WiFi","zona_fumadores":"Zona fumadores",
             "delivery":"Delivery","para_llevar":"Para llevar","accesible":"Accesible"}
    lista_tags=[etiquetas_visibles[tag] for tag in literal_eval(str_list_tags)]
    return lista_tags

def transformar_tp_comercio(tipo_cocina_comercio):
    tipos_cocina_visibles={"alta_cocina":"Alta cocina", "tecnico_conceptual":"Cocina técnico-conceptual",
           "vanguardia":"Cócina de vanguardia", "autor":"Cócina de autor", "clasica":"Cócina clasica"}
    return tipos_cocina_visibles[tipo_cocina_comercio]

def transformar_dias_comercio(str_list_dias):
    return literal_eval(str_list_dias)