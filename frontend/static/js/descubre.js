let indice_pag=0;
let total_comercios=0;
let total_pag=0;

    
    // Esta funcion se va a ejecutar directamente cuando el template se renderice
    document.addEventListener('DOMContentLoaded', function() {
        total_comercios = parseInt(document.getElementById("total_comercios").textContent); // Se podría eliminar
        total_pag = parseInt(document.getElementById("total_paginas").textContent);
        indice_pag = parseInt(document.getElementById("pagina_actual").textContent);

        actualizarBotonesPagina();
        
    });

    // Esta funcion va a renderizar la pagina descubre segun el indice actual
    function actualizarPag(){
        window.location.href = `/descubre/${indice_pag}`;
    };

    // Esta funcion va a modificar el estado de los botones de paginacion. Si nos encontramos en la primera pág se va a deshabilitar el boton previo y si se llega a la ultima el de boton siguiente
    function actualizarBotonesPagina(){
        const btn_previo=document.getElementById("btn_prev");
        const btn_siguiente=document.getElementById("btn_sig");

        btn_previo.disabled=(indice_pag <= 0);
        btn_siguiente.disabled=(indice_pag >= total_pag);
    };

    // Funcion que me va a permitir retroceder una pág
    function prevPage(){
        if (indice_pag > 0)
        {
            indice_pag--;
            actualizarPag();
            actualizarBotonesPagina();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    };

    // Funcion que me va a permitir avanzar una pág
    function nextPage(){
        if ( indice_pag < total_pag){
            indice_pag++;
            actualizarPag();
            actualizarBotonesPagina();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        };
    };

    // Función para seleccionar restaurante REVISAR
    function selectRestaurant(card) {
        // Aquí puedes agregar la lógica para navegar a la página del restaurante
        const restaurantName = card.querySelector('.restaurant-name').textContent;
        const id = card.getAttribute('data-id');
            if (id) {
                window.location.href = '/restaurante/' + id;
            }
    }
