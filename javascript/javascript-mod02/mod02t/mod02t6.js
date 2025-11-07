// Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
// Write a main program that rolls the dice until the result is 6.
// The main program should print out the result of each roll in an unordered list (<ul>). (2p)

javascript// Function to return a random dice roll (1 to 6)
function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

// Main program
let rolls = [];
let result;

do {
    result = rollDice();
    rolls.push(result);
} while (result !== 6);

// Generate unordered list HTML
let html = "<ul>";
for (let roll of rolls) {
    html += `<li>${roll}</li>`;
}
html += "</ul>";

// Display on the web page
document.body.innerHTML = "<h2>Dice Rolls until 6</h2>" + html;