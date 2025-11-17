// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Find the button (assuming it has id="myButton" or just the only button)
    const button = document.querySelector('button');

    // Add click event listener
    button.addEventListener('click', () => {
        alert('Button Clicked');
    });
});