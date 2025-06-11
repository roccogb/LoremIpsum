    let selectedRating = 0;
    
    // Manejo de calificación con estrellas
    document.addEventListener('DOMContentLoaded', function() {
        const stars = document.querySelectorAll('.star');
        const reviewText = document.getElementById('reviewText');
        const charCount = document.getElementById('charCount');
        
        // Event listeners para las estrellas
        stars.forEach(star => {
            star.addEventListener('click', function() {
                const rating = parseInt(this.dataset.rating);
                setRating(rating);
            });
            
            star.addEventListener('mouseenter', function() {
                const rating = parseInt(this.dataset.rating);
                highlightStars(rating);
            });
        });
        
        // Restaurar estrellas al salir del mouse
        document.getElementById('starRating').addEventListener('mouseleave', function() {
            highlightStars(selectedRating);
        });
        
        // Contador de caracteres
        reviewText.addEventListener('input', function() {
            const count = this.value.length;
            charCount.textContent = count;
            
            if (count > 450) {
                charCount.style.color = '#ff6b6b';
            } else {
                charCount.style.color = '#666';
            }
        });
    });
    
    function setRating(rating) {
        selectedRating = rating;
        highlightStars(rating);
    }
    
    function highlightStars(rating) {
        const stars = document.querySelectorAll('.star');
        stars.forEach((star, index) => {
            if (index < rating) {
                star.textContent = '★';
                star.classList.add('active');
            } else {
                star.textContent = '☆';
                star.classList.remove('active');
            }
        });
    }
    
    function submitReview(event) {
        event.preventDefault();
        
        const reviewText = document.getElementById('reviewText').value.trim();
        
        if (selectedRating === 0) {
            alert('Por favor, selecciona una calificación con estrellas.');
            return;
        }
        
        if (reviewText === '') {
            alert('Por favor, escribe una reseña.');
            return;
        }
        
        // Aquí iría la lógica para enviar la reseña
        console.log('Reseña enviada:', {
            rating: selectedRating,
            text: reviewText
        });
        
        // Simulación de envío exitoso
        const submitBtn = document.getElementById('submitBtn');
        const originalText = submitBtn.textContent;
        
        submitBtn.textContent = 'ENVIANDO...';
        submitBtn.disabled = true;
        
        setTimeout(() => {
            submitBtn.textContent = '¡ENVIADO!';
            submitBtn.style.backgroundColor = '#4CAF50';
            
            setTimeout(() => {
                // Redirigir o limpiar formulario
                alert('¡Gracias por tu reseña!');
                document.getElementById('reviewForm').reset();
                setRating(0);
                document.getElementById('charCount').textContent = '0';
                
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
                submitBtn.style.backgroundColor = '';
            }, 1500);
        }, 1000);
    }
    
    function goBack() {
        // Aquí puedes usar window.history.back() o redirigir a una URL específica
        if (document.referrer) {
            window.history.back();
        } else {
            window.location.href = '/'; // Redirigir al inicio si no hay historial
        }
    }