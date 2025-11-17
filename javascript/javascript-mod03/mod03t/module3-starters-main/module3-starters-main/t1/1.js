//tehtävä 1j

// DOM
document.addEventListener('DOMContentLoaded', () => {
    const target = document.getElementById('target');

//class list
    target.classList.add('my-list');

//elementit Inner html
    target.innerHTML = `
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    `;
});