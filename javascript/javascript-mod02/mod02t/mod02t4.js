// Write a program that asks the user for numbers until the user gives zero.
// The given numbers are printed in the console from the largest to the smallest. (2p)

// Array to store the numbers
let numbers = [];

// Ask for numbers until user enters 0
while (true) {
    let input = prompt("Enter a number (0 to stop):");
    let num = parseFloat(input);

    // Check if input is a valid number
    if (isNaN(num)) {
        alert("Please enter a valid number.");
        continue;
    }

    // Stop if user enters 0
    if (num === 0) {
        break;
    }

    // Add number to array
    numbers.push(num);
}

// Sort numbers from largest to smallest
numbers.sort((a, b) => b - a);

// Print to console
console.log("Numbers from largest to smallest:");
for (let num of numbers) {
    console.log(num);
}