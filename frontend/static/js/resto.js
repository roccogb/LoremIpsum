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


document.addEventListener('DOMContentLoaded', function () {
  // Leer días y horarios desde data-attributes
  const datos = document.getElementById('datos-comercio');
  const diasRaw = datos.getAttribute('data-dias');         // ej: "jueves,viernes,sabado,domingo"
  const horariosRaw = datos.getAttribute('data-horarios'); // ej: "Cena(19:00-23:00)"

  const diasPermitidos = diasRaw ? diasRaw.split(',') : [];
  const horariosPermitidos = horariosRaw ? horariosRaw.split(',') : [];

  const fechaInput = document.getElementById('fecha_reserva');
  const form = document.getElementById('form-reserva');

  const diasSemana = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sabado'];

  // Verifica si el día es permitido
  function esDiaPermitido(fecha) {
    const nombreDia = diasSemana[fecha.getDay()];
    return diasPermitidos.includes(nombreDia);
  }

  // Verifica si la hora está dentro de alguno de los rangos permitidos
  function esHoraPermitida(fecha) {
    const hora = fecha.getHours();
    const minutos = fecha.getMinutes();

    for (const horario of horariosPermitidos) {
      // Extraer rango hora en formato (HH:mm-HH:mm)
      const match = horario.match(/\((\d{2}:\d{2})-(\d{2}:\d{2})\)/);
      if (match) {
        const [_, inicio, fin] = match;
        const [hIni, mIni] = inicio.split(':').map(Number);
        const [hFin, mFin] = fin.split(':').map(Number);

        const minutosTotales = hora * 60 + minutos;
        const inicioMin = hIni * 60 + mIni;
        const finMin = hFin * 60 + mFin;

        if (minutosTotales >= inicioMin && minutosTotales <= finMin) {
          return true;
        }
      }
    }
    return false;
  }

  flatpickr(fechaInput, {
  enableTime: true,
  time_24hr: true,
  dateFormat: "Y-m-d H:i",
  minDate: "today",
  disable: [
    function(date) {
      return !esDiaPermitido(date);
    }
  ],
  onClose: function(selectedDates, dateStr, instance) {
    if (!selectedDates.length) return;

    const selected = selectedDates[0];
    if (!esHoraPermitida(selected)) {
      alert("Ese horario no está disponible. Por favor, elige otro.");
      instance.clear();
    }
  }
});

  // Validación al enviar formulario
  form.addEventListener('submit', function(e) {
    const fecha = new Date(fechaInput.value);
    if (!esDiaPermitido(fecha)) {
      e.preventDefault();
      alert('La fecha seleccionada no corresponde a un día habilitado.');
      return;
    }
    if (!esHoraPermitida(fecha)) {
      e.preventDefault();
      alert('La hora seleccionada está fuera del horario permitido.');
      return;
    }
  });
});