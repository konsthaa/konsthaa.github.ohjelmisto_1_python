'use strict';
const names = ['John', 'Paul', 'Jones'];

document.addEventListener('DOMContentLoaded', () => {
    const target = document.getElementById('target');

    // The array of names (this should already be in the starter code or you add it)
    const names = ['John', 'Paul', 'Jones'];

    // Build the HTML string using a for-loop
    let html = '';
    for (let i = 0; i < names.length; i++) {
        html += `<li>${names[i]}</li>`;
    }

    // Assign the complete HTML to the target element using innerHTML
    target.innerHTML = html;
});
