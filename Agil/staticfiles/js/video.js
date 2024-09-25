const video = document.getElementById('video');
const overlay = document.getElementById('overlay');
const playButton = document.getElementById('playButton');

playButton.addEventListener('click', () => {
    overlay.classList.add('hidden');
    video.play();
});

video.addEventListener('play', () => {
    video.style.opacity = '1';
});

window.onload = function() {
    video.pause();
};