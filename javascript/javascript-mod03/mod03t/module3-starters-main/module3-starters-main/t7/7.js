document.addEventListener('DOMContentLoaded', () => {
    const trigger = document.getElementById('trigger');
    const target  = document.getElementById('target');

    // Store the original source (this is usually something like http://127.0.0.1:.../picA.jpg)
    const originalSrc = target.src;

    trigger.addEventListener('mouseenter', () => {
        // Add a timestamp to force browser to treat it as a new image
        target.src = 'picB.jpg' + Date.now();
        // Or simply use the correct path if files are in the same folder:
        // target.src = 'picB.jpg';
    });

    trigger.addEventListener('mouseleave', () => {
        target.src = originalSrc;   // goes back perfectly
    });
});