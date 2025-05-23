let array_coords=document.getElementById("coordenadas_comercio").innerHTML.split(";")        //Extraigo las coordenadas del elemento 'p'
let coord_x=array_coords[0]                                          
let coord_y=array_coords[1]

let map=L.map("map").setView([coord_x, coord_y],15);            //Inicializo el mapa y lo configuro. [coord(x),coord(y), zoom]

// Añado la capa de mosaicos al mapa. Se va a utilizar una capa de mosaicos de OpenStreetMap
// El crear una capa de mosaico significa configurar la plantilla URL(https://tile.openstreetmap.org/{z}/{x}/{y}.png) para las imagenes de los mosaicos, el texto de atribución y el nivel maximo de la capa
// {z} -> Nivel del zoom
// {x} -> Coord x
// {y} -> Coord y
// {title} -> Subdominio que mejora la velocidad y la carga de los mosaicos del mapa
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,            // Configuro el zoom max
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'    // Menciono la página que utilizo para las capas de mosaicos
}).addTo(map);

let marcador=L.marker([coord_x, coord_y]).addTo(map);                                     // Creo un marcador y lo añado al mapa

