// Write a program that asks for the names of six dogs.
// The program prints dog names to unordered list <ul> in reverse alphabetical order. (2p)

// Array to store 6 dog names
let dogs = [];

// Collect 6 dog names
for (let i = 0; i < 6; i++) {
    let name = prompt(`Enter name of dog ${i + 1}:`);
    name = name.trim();
    while (!name) {
        name = prompt(`Name cannot be empty. Enter name of dog ${i + 1} again:`).trim();
    }
    dogs.push(name);
}

// Sort in reverse alphabetical order (Z to A)
dogs.sort((a, b) => b.localeCompare(a));

// Generate unordered list HTML
let html = "<ul>";
for (let dog of dogs) {
    html += `<li>${dog}</li>`;
}
html += "</ul>";

// Display on the web page
document.body.innerHTML = "<h2>Dog Names (Z to A)</h2>" + html;