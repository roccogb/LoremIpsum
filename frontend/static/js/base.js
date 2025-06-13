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
