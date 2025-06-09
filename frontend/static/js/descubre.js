    // Función para alternar favoritos
    function toggleFavorite(event, button) {
        event.stopPropagation(); // Prevenir que se active el click del card
        
        const icon = button.querySelector('i');
        if (icon.classList.contains('far')) {
            icon.classList.remove('far');
            icon.classList.add('fas');
            button.classList.add('active');
        } else {
            icon.classList.remove('fas');
            icon.classList.add('far');
            button.classList.remove('active');
        }
    }
    
    // Función para seleccionar restaurante
    function selectRestaurant(card) {
        // Aquí puedes agregar la lógica para navegar a la página del restaurante
        const restaurantName = card.querySelector('.restaurant-name').textContent;
        console.log('Restaurante seleccionado:', restaurantName);
        // Ejemplo: window.location.href = '/restaurant/' + restaurantId;
    }
    
    // Función para cambiar de página
    function goToPage(pageNumber) {
        // Remover clase active de todos los botones
        document.querySelectorAll('.pagination-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Agregar clase active al botón clickeado
        event.target.classList.add('active');
        
        // Aquí puedes agregar la lógica para cargar los datos de la página
        console.log('Navegando a la página:', pageNumber);
        
        // Scroll hacia arriba
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    
    // Funcionalidad de filtros
    document.addEventListener('DOMContentLoaded', function() {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                applyFilters();
            });
        });
    });
    
    function applyFilters() {
        // Obtener todos los filtros seleccionados
        const selectedFilters = {
            ubicacion: [],
            categoria: [],
            cocina: [],
            horario: []
        };
        
        // Recopilar filtros seleccionados
        document.querySelectorAll('#ubicacion1, #ubicacion2, #ubicacion3').forEach(cb => {
            if (cb.checked) selectedFilters.ubicacion.push(cb.id);
        });
        
        document.querySelectorAll('#categoria1, #categoria2, #categoria3').forEach(cb => {
            if (cb.checked) selectedFilters.categoria.push(cb.id);
        });
        
        document.querySelectorAll('#cocina1, #cocina2, #cocina3').forEach(cb => {
            if (cb.checked) selectedFilters.cocina.push(cb.id);
        });
        
        document.querySelectorAll('#horario1, #horario2, #horario3').forEach(cb => {
            if (cb.checked) selectedFilters.horario.push(cb.id);
        });
        
        console.log('Filtros aplicados:', selectedFilters);
        
        // Aquí puedes agregar la lógica para filtrar los restaurantes
        // Por ejemplo, hacer una petición AJAX al servidor con los filtros
    }