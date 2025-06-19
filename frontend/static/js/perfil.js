// Funcion utilizada para desplegar las reservas, reseñas, como tambien la de los restaurantes favoritos.
// Esto se va a poder realizar agregando clases con determinados estilos que van a lograr el efecto de menu desplegable('expanded','collapsed')
function toggleSection(sectionId) {
    const content = document.getElementById(sectionId);
    const title = document.querySelector(`[onclick="toggleSection('${sectionId}')"]`);
    
    if (content.classList.contains('expanded')) {
        content.classList.remove('expanded');
        title.classList.add('collapsed');
    } else {
        content.classList.add('expanded');
        title.classList.remove('collapsed');
    }
};

function openQRPopup(popupId) {
    const popup = document.getElementById(popupId);
    if (popup) {
        popup.classList.add('show');
    }
}

function closeQRPopup(popupId) {
    const popup = document.getElementById(popupId);
    if (popup) {
        popup.classList.remove('show');
    }
}