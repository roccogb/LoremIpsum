let currentIndex = 0;                       // Variable global que lleva el registro del comercio actualmente mostrado
let comerciosData = [];                     // Variable global que va a almacenar la informacion de los comercios

// Esta funcion se va a ejecutar en el momento que el template 'home' se renderice
document.addEventListener("DOMContentLoaded", () => {
    // Obtener los datos de los comercios
    const comerciosElement = document.getElementById("comercios_data");             // Almaceno los datos que se encuentran en el elemento 'comercios-data' que van a estar en formato JSON
    comerciosData = JSON.parse(comerciosElement.textContent);                       // Tomo el texto de ese elemento, que va a ser una cadena JSON, y lo convierto en un objeto que JS pueda usar
    
    // Mostrar el primer comercio
    updateRestauranteDisplay();
});

function updateRestauranteDisplay() {
    const tituloElement = document.querySelector(".restaurant-name");               // Selecciono los elementos que tienen los identificadores: '.restaurant-name' y '.hero-card'
    const heroCard = document.querySelector(".hero-card");                         
    const currentComercio = comerciosData[currentIndex];                            // Llamo al comercio actual por el indice
    
    // Actualizar nombre y imagen de fondo
    tituloElement.textContent = currentComercio.nombre_comercio;
    heroCard.style.backgroundImage = `url('static/${currentComercio.ruta_imagen}')`;
    
    // También puedes actualizar la imagen del logo si es necesario
    const logoImg = document.querySelector(".restaurant-info img");
    if (currentComercio.logo_url) {
        logoImg.src = currentComercio.logo_url;
        logoImg.style.display = "block";
    } else {
        logoImg.style.display = "none";
    }
}

function nextRestauranteTop() {
    // Si se presiona la flecha siguiente se va a actualizar el contador y nuevamente se van a cargar los datos nuevos
    currentIndex = (currentIndex + 1) % comerciosData.length;
    updateRestauranteDisplay();
}

function prevRestauranteTop() {
    // Si se presiona la flecha anterior se va a actualizar el contador y nuevamente se van a cargar los datos nuevos
    currentIndex = (currentIndex - 1 + comerciosData.length) % comerciosData.length;
    updateRestauranteDisplay();
};

// Esta funcion va a redirigir al usuario a la página de un restaurante específico. Va a recibir de parametro el id del mismo y luego va a modificar la URL llevandolo al endpoint en cuestión
function goToComercio(id) {
    // Cambia la URL actual para navegar a la página del restaurante
    window.location.href = `/ver_comercio/${id}`;
};

// Realiza una animación y cambia el estado del botón de "favorito" (corazón). Recibe de parametro el boton en cuestión
// Nota: event.stopPropagation() evita que el evento se propague al contenedor padre.
function toggleHeart(button) {
    // Detiene la propagación del evento para que no active otros listeners (como el click de la carta)
    event.stopPropagation();

    // Alterna la clase 'active' en el botón (si la tiene, la quita; si no, la añade)
    button.classList.toggle('active');

    // Si el botón está activo (es favorito)
    if (button.classList.contains('active')) {
        button.innerHTML = '♥'; // Cambia a corazón lleno
        button.style.transform = 'scale(1.2)'; // Efecto de escala (agrandar)

        // Después de 150ms, reduce ligeramente el tamaño para efecto de "rebote"
        setTimeout(() => {
            button.style.transform = 'scale(1.1)';
        }, 150);
    } 
    // Si el botón NO está activo
    else {
        button.innerHTML = '♡'; // Vuelve a corazón vacío
        button.style.transform = 'scale(0.9)'; // Efecto de encogimiento

        // Después de 150ms, vuelve al tamaño normal con efecto de "rebote"
        setTimeout(() => {
            button.style.transform = 'scale(1)';
        }, 150);
    }

// Esta funcion aplica una animación al hacer click en cualquier carta de restaurante. La misma no se activa si se clickea el botón de favoritos (heart-btn).
document.querySelectorAll('.restaurant-card').forEach(card => {
    card.addEventListener('click', function(e) {
        // Si el elemento clickeado es el botón de corazón, ignora el evento
        if (e.target.classList.contains('heart-btn')) {
            return;
        }

        // Aplica un efecto de escala (ligeramente más grande)
        this.style.transform = 'scale(1.05)';

        // Después de 150ms, vuelve al tamaño original
        setTimeout(() => {
            this.style.transform = 'scale(1)';
        }, 150);

        // Nota: Aquí podrías añadir también la redirección al restaurante
        // Ejemplo: goToRestaurant(card.dataset.restaurantId);
    });
});