document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        document.body.classList.add('loaded');
    }, 1500); // Tempo em milissegundos antes de ocultar o preloader
});