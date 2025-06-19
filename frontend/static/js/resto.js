

    
    document.addEventListener('DOMContentLoaded', function() {
        // Establecer fecha y hora mínima para el input datetime-local
        const fechaHoraInput = document.querySelector('input[name="fecha_reserva"]');
        if (fechaHoraInput) {
            const ahora = new Date();
            const fechaMinima = new Date(ahora.getTime() - ahora.getTimezoneOffset() * 60000);
            fechaHoraInput.min = fechaMinima.toISOString().slice(0, 16);
        }

        // Manejar botón de favoritos
        const heartBtn = document.querySelector('.heart-btn');
        if (heartBtn) {
            heartBtn.addEventListener('click', function() {
                const comercioId = this.getAttribute('data-id');
                const isActive = this.classList.contains('active');
                
                // Hacer petición AJAX para agregar/quitar favorito
                fetch('/toggle_favorito', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        id_comercio: comercioId
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Alternar clase active y símbolo
                        if (isActive) {
                            this.classList.remove('active');
                            this.innerHTML = '♡';
                        } else {
                            this.classList.add('active');
                            this.innerHTML = '♥';
                        }
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            });
        }

        // Validación de formulario de reserva adaptada para datetime-local
        const formReserva = document.getElementById('form-reserva');
        if (formReserva) {
            formReserva.addEventListener('submit', function(e) {
                const fechaHoraInput = document.querySelector('input[name="fecha_reserva"]');
                
                if (fechaHoraInput) {
                    const fechaHoraSeleccionada = new Date(fechaHoraInput.value);
                    const ahora = new Date();
                    
                    if (fechaHoraSeleccionada <= ahora) {
                        e.preventDefault();
                        alert('La fecha y hora de la reserva debe ser futura.');
                        return false;
                    }
                }
            });
        }

        // Auto-cerrar alertas después de 5 segundos
        setTimeout(function() {
            const alerts = document.querySelectorAll('.alert');
            alerts.forEach(function(alert) {
                const closeButton = alert.querySelector('.close');
                if (closeButton) {
                    closeButton.click();
                }
            });
        }, 5000);
    });


    


document.addEventListener('DOMContentLoaded', function () {
    // Obtener las coordenadas del elemento HTML
    const coordElement = document.getElementById('coordenadas_comercio');
    if (coordElement) {
        const [lat, lng] = coordElement.textContent.split(';').map(coord => parseFloat(coord.trim()));

        // Inicializar el mapa con Leaflet
        const map = L.map('map').setView([lat, lng], 15);  // Zoom 15 es ideal para ciudad

        // Cargar y mostrar el mapa con tiles de OpenStreetMap
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Agregar marcador
        L.marker([lat, lng])
            .addTo(map)
            .bindPopup('Ubicación del comercio')
            .openPopup();
    }
});
