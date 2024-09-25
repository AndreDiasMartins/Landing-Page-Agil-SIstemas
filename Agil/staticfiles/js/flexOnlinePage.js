const video = document.getElementById("systemVideo");

// Configura o IntersectionObserver
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            video.play(); // Inicia o vídeo quando ele se torna visível
            observer.unobserve(video); // Para de observar depois que o vídeo começa a tocar
        }
    });
}, {
    threshold: 0.5 // 50% do vídeo precisa estar visível para iniciar
});

// Começa a observar o vídeo
observer.observe(video);

// Função para expandir o vídeo em dispositivos móveis
function toggleFullscreen() {
    const videoContainer = document.querySelector('.video-container');
    if (videoContainer.classList.contains('fullscreen')) {
        videoContainer.classList.remove('fullscreen');
        video.muted = true; // Mantém o vídeo mudo quando sair do modo fullscreen
    } else {
        videoContainer.classList.add('fullscreen');
        video.muted = false; // Ativa o som no modo fullscreen
    }
}

// Detecta dispositivos móveis e adiciona o evento de toque
if (/Mobi|Android/i.test(navigator.userAgent)) {
    video.addEventListener('click', toggleFullscreen);
}
