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

// Selecciona todos los botones de favoritos ¿?
// document.querySelectorAll('.heart-btn').forEach(function(btn) {
//     btn.addEventListener('click', function(event) {
//         event.stopPropagation();
//         const id_comercio = btn.getAttribute('data-id');
//         const id_usr = btn.getAttribute('data-usr');
//         if (!id_usr) {
//             window.location.href = "/login";
//             return;
//         }
//         fetch('/favoritos/marcar', {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json'},
//             body: JSON.stringify({ id_usr: id_usr, id_comercio: id_comercio })
//         })
        
//         .then(response => response.json())
//         .then(data => {
//             const icon = document.getElementById('icono-fav-' + id_comercio);
//             if (data.favorito) {
//                 icon.innerHTML = "&#9829;";
//                 icon.classList.add('heart-btn.active');
//             } else {
//                 icon.innerHTML = "&#9825;";
//                 icon.classList.remove('heart-btn.active');
//             }
//         });
//     });
// });

// Realiza una animación y cambia el estado del botón de "favorito" (corazón). Recibe de parametro el boton en cuestión
// Nota: event.stopPropagation() evita que el evento se propague al contenedor padre.
function toggleHeart(button) {
    // Detiene la propagación del evento para que no active otros listeners (como el click de la carta)
    event.stopPropagation();
    const id_comercio=button.getAttribite('data-id')

    // Alterna la clase 'active' en el botón (si la tiene, la quita; si no, la añade)
    button.classList.toggle('active');

    // Si el botón está activo (es favorito)
    if (button.classList.contains('active')) {
        button.innerHTML = '♥'; // Cambia a corazón lleno
        button.style.transform = 'scale(1.2)'; // Efecto de escala (agrandar)

        window.location.href=`/dar_fav/${id_comercio}`

        // Después de 150ms, reduce ligeramente el tamaño para efecto de "rebote"
        setTimeout(() => {
            button.style.transform = 'scale(1.1)';
        }, 150);
    } 
    // Si el botón NO está activo
    else {
        button.innerHTML = '♡'; // Vuelve a corazón vacío
        button.style.transform = 'scale(0.9)'; // Efecto de encogimiento

        // Después de 150ms, vuelve al tamaño normal con efecto de "rebote"
        setTimeout(() => {
            button.style.transform = 'scale(1)';
        }, 150);
    }
};