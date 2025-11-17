document.addEventListener('DOMContentLoaded', () => {
    const section = document.querySelector('section');
    const dialog = document.querySelector('dialog');
    const modalImage = document.getElementById('modalImage');
    const closeBtn = document.getElementById('closeBtn');

    // Build all cards (same as Task 5 but using medium + store large)
    picArray.forEach(pic => {
        const article = document.createElement('article');
        article.classList.add('card');

        const h2 = document.createElement('h2');
        h2.textContent = pic.title;

        const figure = document.createElement('figure');

        const img = document.createElement('img');
        img.src = pic.medium;           // medium image in card
        img.alt = pic.title;

        const figcaption = document.createElement('figcaption');
        figcaption.textContent = pic.caption;

        const p = document.createElement('p');
        p.textContent = pic.description;

        // Store large image path in data attribute for easy access
        article.dataset.large = pic.large;
        article.dataset.title = pic.title;

        // Assemble card
        figure.appendChild(img);
        figure.appendChild(figcaption);
        article.appendChild(h2);
        article.appendChild(figure);
        article.appendChild(p);

        section.appendChild(article);
    });

    // === MODAL FUNCTIONALITY ===

    // Click on any article → open modal with large image
    section.addEventListener('click', (e) => {
        const card = e.target.closest('article');
        if (!card) return;

        const largeSrc = card.dataset.large;
        const title = card.dataset.title;

        modalImage.src = largeSrc;
        modalImage.alt = title;

        dialog.showModal();  // opens the modal
    });

    // Close modal when clicking the × (span)
    closeBtn.addEventListener('click', () => {
        dialog.close();
    });

    // Optional: close when clicking outside the image
    dialog.addEventListener('click', (e) => {
        if (e.target === dialog) {
            dialog.close();
        }
    });
});