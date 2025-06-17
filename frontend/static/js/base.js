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
function toggleHeart(button, event) {
    event.stopPropagation();

    const id_comercio = button.getAttribute('data-id');

    // Si ya es favorito, lo borra.
    if (button.classList.contains('active')) {
        button.classList.remove('active');
        button.innerHTML = '♡';
        button.style.transform = 'scale(1.2)';
        setTimeout(() => button.style.transform = 'scale(1)', 150);
    } else { 
        // Sino lo marca como favorito.
        button.classList.add('active');
        button.innerHTML = '♥';
        button.style.transform = 'scale(1.2)';
        setTimeout(() => button.style.transform = 'scale(1.1)', 150);
    }

    // Después de 150ms, vuelve al tamaño normal con efecto de "rebote"
    setTimeout(() => {
        button.style.transform = 'scale(1.1)';
    }, 150);

    // Manda la petición de agregar o eliminar favorito.o.
    window.location.href = `/marcar_fav/${id_comercio}`;
}