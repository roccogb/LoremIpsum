document.addEventListener('DOMContentLoaded', function() {
        // Establecer fecha y hora mínima para el input datetime-local
        const fechaHoraInput = document.querySelector('input[name="fecha_reserva"]');
        if (fechaHoraInput) {
            const ahora = new Date();
            const fechaMinima = new Date(ahora.getTime() - ahora.getTimezoneOffset() * 60000);
            fechaHoraInput.min = fechaMinima.toISOString().slice(0, 16);
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

// Funcion javascript que va a cargar el mapa 'Leaflet' con las capaz de Openstreetmap
document.addEventListener('DOMContentLoaded', function () {
    const coordElement = document.getElementById('coordenadas_comercio');
    if (coordElement) {
        const [lat, lng] = coordElement.textContent.split(';').map(coord => parseFloat(coord.trim()));

        const map = L.map('map').setView([lat, lng], 15);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        L.marker([lat, lng])
            .addTo(map)
            .bindPopup('Ubicación del comercio')
            .openPopup();
    }
});


document.addEventListener('DOMContentLoaded', function () {
  // Leer días y horarios desde data-attributes
  const datos = document.getElementById('datos-comercio');
  const diasRaw = datos.getAttribute('data-dias');        
  const horariosRaw = datos.getAttribute('data-horarios');

  const diasPermitidos = diasRaw ? diasRaw.split(',') : [];
  const horariosPermitidos = horariosRaw ? horariosRaw.split(',') : [];

  const fechaInput = document.getElementById('fecha_reserva');
  const form = document.getElementById('form-reserva');

  const diasSemana = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];

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
        const match = horario.match(/\((\d{2}):(\d{2})-(\d{2}):(\d{2})\)/);
        if (match) {
            const hIni = parseInt(match[1]);
            const mIni = parseInt(match[2]);
            const hFin = parseInt(match[3]);
            const mFin = parseInt(match[4]);

            const minutosTotales = hora * 60 + minutos;
            const inicioMin = hIni * 60 + mIni;
            const finMin = hFin * 60 + mFin;

            if (inicioMin <= finMin) {
                // Rango normal
                if (minutosTotales >= inicioMin && minutosTotales <= finMin) {
                    return true;
                }
            } else {
                // Rango que cruza medianoche
                if (minutosTotales >= inicioMin || minutosTotales <= finMin) {
                    return true;
                }
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