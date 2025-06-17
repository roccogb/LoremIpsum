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