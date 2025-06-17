document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".nav-links a");
    navLinks.forEach(link => {
        link.addEventListener("click", function () {
            navLinks.forEach(l => l.classList.remove("active"));
            this.classList.add("active");
        });
    });
});

function toggleMobileMenu() {
    const navLinks = document.getElementById("navLinks");
    const hamburger = document.querySelector(".hamburger");
    navLinks.classList.toggle("show");
    hamburger.classList.toggle("active");
}

function showUserMenu() {
    const dropdown = document.getElementById("userDropdown");
    dropdown.classList.toggle("show");
}

document.addEventListener("click", function (event) {
    const userDropdown = document.getElementById("userDropdown");
    const userTrigger = document.querySelector(".nav-user");
    const navLinks = document.getElementById("navLinks");
    const hamburger = document.querySelector(".hamburger");

    if (!userTrigger.contains(event.target) && !userDropdown.contains(event.target)) {
        userDropdown.classList.remove("show");
    }
    if (!hamburger.contains(event.target) && !navLinks.contains(event.target)) {
        navLinks.classList.remove("show");
        hamburger.classList.remove("active");
    }
});

document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
        document.getElementById("userDropdown").classList.remove("show");
        document.getElementById("navLinks").classList.remove("show");
        document.querySelector(".hamburger").classList.remove("active");
    }
});

window.addEventListener("resize", function () {
    const navLinks = document.getElementById("navLinks");
    if (window.innerWidth > 576) {
        navLinks.classList.remove("show");
        document.querySelector(".hamburger").classList.remove("active");
    }
});

document.querySelector(".nav-user").addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        showUserMenu();
    }
});

document.querySelectorAll('.heart-btn').forEach(function(btn) {
    btn.addEventListener('click', function(event) {
        toggleHeart(this, event);
    });
});

// Realiza una animación y cambia el estado del botón de "favorito" (corazón).
async function toggleHeart(button, event) {
    event.stopPropagation();
    
    const id_comercio = button.getAttribute('data-id');
    const wasActive = button.classList.contains('active');
    
    // Cambia el estado visual inmediatamente
    if (wasActive) {
        button.classList.remove('active');
        button.innerHTML = '♡';
    } else { 
        button.classList.add('active');
        button.innerHTML = '♥';
    }
    
    // Animación
    button.style.transform = 'scale(1.2)';
    setTimeout(() => {
        button.style.transform = wasActive ? 'scale(1)' : 'scale(1.1)';
    }, 150);
    
    // Hacer la petición AJAX al backend
    const response = await fetch(`/click_fav/${id_comercio}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    });
    
    const data = await response.json();
    
    if (!response.ok) {
        // Si hubo error, revertir el estado visual
        if (wasActive) {
            button.classList.add('active');
            button.innerHTML = '♥';
        } else {
            button.classList.remove('active');
            button.innerHTML = '♡';
        }
    }
}

// Función para manejar el clic en la carta del restaurante
function handleCardClick(event, element) {
    if (event.target.closest('.heart-btn')) {
        return;
    }
    else if(event.target.closest('.nav-arrow left')){
        return;
    }
    else if(event.target.closest('.nav-arrow right')){
        return;
    }
    // Redirigir a la página del restaurante
    window.location.href = element.dataset.url;
}