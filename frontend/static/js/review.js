    const stars = document.querySelectorAll('.star');
    const ratingText = document.getElementById('ratingText');
    const radioButtons = document.querySelectorAll('input[name="calificacion"]');

    const ratingTexts = {
        1: "⭐ Malo",
        2: "⭐⭐ Regular", 
        3: "⭐⭐⭐ Bueno",
        4: "⭐⭐⭐⭐ Muy Bueno",
        5: "⭐⭐⭐⭐⭐ Excelente"
    };

    // Actualizar texto cuando se selecciona una estrella
    radioButtons.forEach(radio => {
        radio.addEventListener('change', function() {
            if (this.checked) {
                ratingText.textContent = ratingTexts[this.value];
            }
        });
    });