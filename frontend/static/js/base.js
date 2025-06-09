document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".nav-links a");

    navLinks.forEach(link => {
        link.addEventListener("click", function () {
            // Quitar la clase 'active' de todos los links
            navLinks.forEach(l => l.classList.remove("active"));

            // Agregar la clase 'active' al link clickeado
            this.classList.add("active");
        });
    });
});

        // Función para toggle del menú móvil
        function toggleMobileMenu() {
            const navLinks = document.getElementById('navLinks');
            navLinks.classList.toggle('show');
        }
        
        // Cerrar menú móvil al hacer click fuera
        document.addEventListener('click', function(event) {
            const navLinks = document.getElementById('navLinks');
            const hamburger = document.querySelector('.hamburger');
            
            if (!navLinks.contains(event.target) && !hamburger.contains(event.target)) {
                navLinks.classList.remove('show');
            }
        });
        
        // Función placeholder para ayuda
        function showHelp() {
            alert('Sección de ayuda - Próximamente');
        }
        
        // Función placeholder para menú de usuario
        function showUserMenu() {
            alert('Menú de usuario - Próximamente');
        }
        
        // Cerrar menú móvil al redimensionar ventana
        window.addEventListener('resize', function() {
            const navLinks = document.getElementById('navLinks');
            if (window.innerWidth > 576) {
                navLinks.classList.remove('show');
            }
        });
        
        // Mejorar accesibilidad del menú de usuario
        document.querySelector('.nav-user').addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                showUserMenu();
            }
        });
          // Función para toggle del menú móvil
        function toggleMobileMenu() {
            const navLinks = document.getElementById('navLinks');
            navLinks.classList.toggle('show');
        }
        
        // Cerrar menú móvil al hacer click fuera
        document.addEventListener('click', function(event) {
            const navLinks = document.getElementById('navLinks');
            const hamburger = document.querySelector('.hamburger');
            
            if (!navLinks.contains(event.target) && !hamburger.contains(event.target)) {
                navLinks.classList.remove('show');
            }
        });
        
        // Función placeholder para ayuda
        function showHelp() {
            alert('Sección de ayuda - Próximamente');
        }
        
        // Función placeholder para menú de usuario
        function showUserMenu() {
            alert('Menú de usuario - Próximamente');
        }
        
        // Cerrar menú móvil al redimensionar ventana
        window.addEventListener('resize', function() {
            const navLinks = document.getElementById('navLinks');
            if (window.innerWidth > 576) {
                navLinks.classList.remove('show');
            }
        });
        
        // Mejorar accesibilidad del menú de usuario
        document.querySelector('.nav-user').addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                showUserMenu();
            }
        });