//tehtävä 2

document.addEventListener('DOMContentLoaded', () => {
    const target = document.getElementById('target');

    // li elementti
    const li1 = document.createElement('li');
    li1.textContent = 'First item';

    const li2 = document.createElement('li');
    li2.textContent = 'Second item';
    li2.classList.add('my-item');        // class toiseen itemiin

    const li3 = document.createElement('li');
    li3.textContent = 'Third item';

    // Appendi
    target.appendChild(li1);
    target.appendChild(li2);
    target.appendChild(li3);
});