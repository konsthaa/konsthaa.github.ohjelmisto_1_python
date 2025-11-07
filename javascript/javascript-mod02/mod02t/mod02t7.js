// Modify the function above so that it gets the number of sides on the dice as a parameter.
// With the modified function you can for example roll a 21-sided role-playing dice.
// The difference to the last exercise is that the dice rolling in the main program continues
// until the program gets the maximum number on the dice, which is asked from the user at the beginning. (2p)

// Function: roll a dice with given number of sides (returns 1 to sides)
function rollDice(sides) {
    return Math.floor(Math.random() * sides) + 1;
}

// Main program
// Ask user for the number of sides
let sidesInput = prompt("Enter the number of sides on the dice:");
let sides = parseInt(sidesInput);

// Validate input
while (isNaN(sides) || sides < 2) {
    sidesInput = prompt("Please enter a valid number of sides (at least 2):");
    sides = parseInt(sidesInput);
}

let maxValue = sides; // The maximum number on the dice
let rolls = [];
let result;

// Roll until we get the maximum value
do {
    result = rollDice(sides);
    rolls.push(result);
} while (result !== maxValue);

// Generate unordered list HTML
let html = "<ul>";
for (let roll of rolls) {
    html += `<li>${roll}</li>`;
}
html += "</ul>";

// Display result on the web page
document.body.innerHTML = `
    <h2>Dice Rolls (1–${sides}) until ${maxValue}</h2>
    <p>All rolls:</p>
    ${html}
`;