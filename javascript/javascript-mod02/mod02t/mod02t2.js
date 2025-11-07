// Write a program that asks the user for the number of participants.
// After this, the program asks for the names of all participants.
// Finally, the program prints the names of the participants on the web page in an ordered list (<ol>) in alphabetical order. (2p)

// Prompt for the number of participants
let count = parseInt(prompt("Enter the number of participants:"));

// Input validation: ensure a positive number
while (isNaN(count) || count <= 0) {
    count = parseInt(prompt("Invalid input. Please enter a positive number:"));
}

// Array to store names
let names = [];

// Collect names
for (let i = 0; i < count; i++) {
    let name = prompt(`Enter name of participant ${i + 1}:`);

    // Trim and validate non-empty name
    name = name.trim();
    while (!name) {
        name = prompt(`Name cannot be empty. Please enter name of participant ${i + 1} again:`).trim();
    }
    names.push(name);
}

// Sort names alphabetically (case-sensitive using localeCompare)
names.sort((a, b) => a.localeCompare(b));

// Generate the ordered list HTML
let html = "<ol>";
for (let name of names) {
    html += `<li>${name}</li>`;
}
html += "</ol>";

// Print to the web page (browser only)
document.body.innerHTML = "<h2>Participants (Alphabetical Order)</h2>" + html;