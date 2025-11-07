// Write a program that prompts the user for numbers.
// When the user enters one of the numbers previously entered,
// the program will announce that the number has already been given and stops
// its operation and then prints all the given numbers to the console in ascending order. (2p)


javascript// Array to store unique numbers
let numbers = [];

// Keep asking until a duplicate is entered
while (true) {
    let input = prompt("Enter a number:");
    let num = parseFloat(input);

    // Validate input
    if (isNaN(num)) {
        alert("Please enter a valid number.");
        continue;
    }

    // Check if number was already given
    if (numbers.includes(num)) {
        console.log(`Number ${num} has already been given.`);
        break;
    }

    // Add number to the list
    numbers.push(num);
}

// Sort in ascending order
numbers.sort((a, b) => a - b);

// Print all given numbers to console
console.log("All given numbers in ascending order:");
for (let n of numbers) {
    console.log(n);
}