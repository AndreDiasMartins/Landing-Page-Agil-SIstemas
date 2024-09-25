const fadeInSections = document.querySelectorAll('.fade-in-section');

const observerOptions = {
    threshold: 0.1, // Lowered threshold for mobile devices
    rootMargin: "0px 0px -50px 0px" // Adjusted root margin to trigger earlier on mobile
};

const fadeInObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            requestAnimationFrame(() => {
                entry.target.classList.add('is-visible');
            });
        } else {
            requestAnimationFrame(() => {
                entry.target.classList.remove('is-visible');
            });
        }
    });
}, observerOptions);

fadeInSections.forEach(section => {
    fadeInObserver.observe(section);
});
