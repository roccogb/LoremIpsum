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

// Selecciona todos los botones de favoritos
document.querySelectorAll('.heart-btn').forEach(function(btn) {
    btn.addEventListener('click', function(event) {
        event.stopPropagation();
        const id_comercio = btn.getAttribute('data-id');
        const id_usr = btn.getAttribute('data-usr');
        if (!id_usr) {
            window.location.href = "/login";
            return;
        }
        fetch('/favoritos/marcar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id_usr: id_usr,
                id_comercio: id_comercio
            })
        })
        .then(response => response.json())
        .then(data => {
            const icon = document.getElementById('icono-fav-' + id_comercio);
            if (data.favorito) {
                icon.innerHTML = "&#9829;";
                icon.classList.add('heart-btn.active');
            } else {
                icon.innerHTML = "&#9825;";
                icon.classList.remove('heart-btn.active');
            }
        });
    });
});
