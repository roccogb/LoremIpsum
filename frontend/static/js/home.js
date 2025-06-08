// static/js/home.js

// Restaurant navigation function
function goToRestaurant(id) {
    window.location.href = `/restaurante/${id}`;
}

// Heart button toggle functionality
function toggleHeart(button) {
    // Prevent card click when heart is clicked
    event.stopPropagation();

    button.classList.toggle('active');
    if (button.classList.contains('active')) {
        button.innerHTML = '♥';
        button.style.transform = 'scale(1.2)';
        setTimeout(() => {
            button.style.transform = 'scale(1.1)';
        }, 150);
    } else {
        button.innerHTML = '♡';
        button.style.transform = 'scale(0.9)';
        setTimeout(() => {
            button.style.transform = 'scale(1)';
        }, 150);
    }
}

// Add some interactivity
document.querySelectorAll('.restaurant-card').forEach(card => {
    card.addEventListener('click', function(e) {
        // Don't trigger card click when heart button is clicked
        if (e.target.classList.contains('heart-btn')) {
            return;
        }
        this.style.transform = 'scale(1.05)';
        setTimeout(() => {
            this.style.transform = 'scale(1)';
        }, 150);
    });
});


