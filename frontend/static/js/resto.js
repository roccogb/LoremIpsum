document.addEventListener('DOMContentLoaded', function() {
    // Obtener los datos de horarios del comercio desde el HTML
    const diasElement = document.querySelector('.dias-section');
    const horariosElement = document.querySelectorAll('.dias-section')[1]; // El segundo elemento con clase dias-section

    let diasFuncionamiento = [];
    let horariosFuncionamiento = [];

    if (diasElement) {
        const diasItems = diasElement.querySelectorAll('.dia-item');
        diasFuncionamiento = Array.from(diasItems).map(item => item.textContent.trim().toLowerCase());
    }

    if (horariosElement) {
        const horariosItems = horariosElement.querySelectorAll('.dia-item');
        horariosFuncionamiento = Array.from(horariosItems).map(item => {
            const match = item.textContent.trim().match(/\((\d{2}:\d{2}-\d{2}:\d{2})\)/);
            return match ? match[1] : null;
        }).filter(Boolean);
    }

    console.log('Días de funcionamiento:', diasFuncionamiento);
    console.log('Horarios de funcionamiento:', horariosFuncionamiento);

    // Mapeo de días en español a números (0 = domingo, 1 = lunes, etc.)
    const diasSemana = {
        'domingo': 0,
        'lunes': 1, 
        'martes': 2,
        'miércoles': 3,
        'miercoles': 3,
        'jueves': 4,
        'viernes': 5,
        'sábado': 6,
        'sabado': 6
    };

    function parsearHorario(horarioStr) {
        const horarioLimpio = horarioStr.replace(/\s/g, '');
        const partes = horarioLimpio.split('-');
        if (partes.length !== 2) return null;
        return {
            inicio: partes[0],
            fin: partes[1]
        };
    }

    function horaAMinutos(horaStr) {
        const [horas, minutos] = horaStr.split(':').map(Number);
        return horas * 60 + minutos;
    }

    function validarFechaHora(fechaHora) {
        const fecha = new Date(fechaHora);
        const diaSemana = fecha.getDay();
        const horaMinutos = fecha.getHours() * 60 + fecha.getMinutes();
        const nombreDia = Object.keys(diasSemana).find(dia => diasSemana[dia] === diaSemana);
        if (!diasFuncionamiento.includes(nombreDia)) {
            return {
                valido: false,
                mensaje: `El comercio no atiende los ${nombreDia}s`
            };
        }

        let dentroDeHorario = false;
        let mensajeHorario = '';

        for (let horario of horariosFuncionamiento) {
            const horarioParsed = parsearHorario(horario);
            if (horarioParsed) {
                const inicioMinutos = horaAMinutos(horarioParsed.inicio);
                const finMinutos = horaAMinutos(horarioParsed.fin);

                if (horaMinutos >= inicioMinutos && horaMinutos <= finMinutos) {
                    dentroDeHorario = true;
                    break;
                }

                if (!mensajeHorario) {
                    mensajeHorario = `Horarios disponibles: ${horariosFuncionamiento.join(', ')}`;
                }
            }
        }

        if (!dentroDeHorario) {
            return {
                valido: false,
                mensaje: `La hora seleccionada está fuera del horario de atención. ${mensajeHorario}`
            };
        }

        return { valido: true };
    }

    const fechaHoraInput = document.querySelector('input[name="fecha_reserva"]');
    if (fechaHoraInput) {
        const ahora = new Date();
        const fechaMinima = new Date(ahora.getTime() - ahora.getTimezoneOffset() * 60000);
        fechaHoraInput.min = fechaMinima.toISOString().slice(0, 16);

        fechaHoraInput.addEventListener('change', function() {
            const fechaSeleccionada = this.value;
            if (fechaSeleccionada) {
                const validacion = validarFechaHora(fechaSeleccionada);
                const errorPrevio = document.querySelector('.horario-error');
                if (errorPrevio) errorPrevio.remove();

                if (!validacion.valido) {
                    const errorDiv = document.createElement('div');
                    errorDiv.className = 'horario-error alert alert-warning mt-2';
                    errorDiv.textContent = validacion.mensaje;
                    this.parentNode.parentNode.appendChild(errorDiv);
                    this.value = '';
                }
            }
        });
    }

    const heartBtn = document.querySelector('.heart-btn');
    if (heartBtn) {
        heartBtn.addEventListener('click', function() {
            const comercioId = this.getAttribute('data-id');
            const isActive = this.classList.contains('active');

            fetch('/toggle_favorito', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id_comercio: comercioId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    if (isActive) {
                        this.classList.remove('active');
                        this.innerHTML = '♡';
                    } else {
                        this.classList.add('active');
                        this.innerHTML = '♥';
                    }
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }

    const formReserva = document.getElementById('form-reserva');
    if (formReserva) {
        formReserva.addEventListener('submit', function(e) {
            const fechaHoraInput = document.querySelector('input[name="fecha_reserva"]');
            if (fechaHoraInput && fechaHoraInput.value) {
                const fechaHoraSeleccionada = new Date(fechaHoraInput.value);
                const ahora = new Date();

                if (fechaHoraSeleccionada <= ahora) {
                    e.preventDefault();
                    alert('La fecha y hora de la reserva debe ser futura.');
                    return false;
                }

                const validacion = validarFechaHora(fechaHoraInput.value);
                if (!validacion.valido) {
                    e.preventDefault();
                    alert(validacion.mensaje);
                    return false;
                }
            }
        });
    }

    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            const closeButton = alert.querySelector('.close');
            if (closeButton) closeButton.click();
        });
    }, 5000);
});

document.addEventListener('DOMContentLoaded', function () {
    const coordElement = document.getElementById('coordenadas_comercio');
    if (coordElement) {
        const [lat, lng] = coordElement.textContent.split(';').map(coord => parseFloat(coord.trim()));
        const map = L.map('map').setView([lat, lng], 15);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
        L.marker([lat, lng]).addTo(map).bindPopup('Ubicación del comercio').openPopup();
    }
});
