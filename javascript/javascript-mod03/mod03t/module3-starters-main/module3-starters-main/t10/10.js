document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const target = document.getElementById('target');

    form.addEventListener('submit', (event) => {
        // Stop the form from submitting (prevents page reload)
        event.preventDefault();

        // Select inputs using attribute selectors (as requested)
        const firstName = document.querySelector('input[name="firstname"]').value.trim();
        const lastName = document.querySelector('input[name="lastname"]').value.trim();

        // Display the result
        if (firstName && lastName) {
            target.textContent = `Your name is ${firstName} ${lastName}`;
        } else {
            target.textContent = 'Please fill in both fields';
        }
    });
});