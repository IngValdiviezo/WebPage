// Galería de imágenes
function initGallery() {
    let current = 0;
    const images = document.querySelectorAll('.gallery-image');
    
    if (images.length > 0) {
        // Activar la primera imagen inmediatamente
        images[0].classList.add('active');
        
        setInterval(() => {
            images[current].classList.remove('active');
            current = (current + 1) % images.length;
            images[current].classList.add('active');
        }, 3000);
    }
}

// Inicializar todo cuando la página carga
window.onload = function() {
    initGallery();
};