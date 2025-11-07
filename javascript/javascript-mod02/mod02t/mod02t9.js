// Write a function called even(), which receives an array containing numbers as a parameter.
// The function returns a second (usually smaller) array which has the even numbers of the original array.
// The function must not make changes to the original array. (3p)
// Example: In a three-item array, there are items 2, 7 and 4. The function returns a two-item array with items 2 and 4.
// Print both the original array and the new array to the console in the main program after you have called the function.
// You can hard code the array, no need for prompt().

// Function: even() - returns new array with only even numbers
function even(numbers) {
    let evens = [];
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] % 2 === 0) {
            evens.push(numbers[i]);
        }
    }
    return evens;
}

// Hardcoded array
let original = [2, 7, 4, 9, 12, 3, 8];

// Call function (original array remains unchanged)
let evenNumbers = even(original);

// Print both arrays to console
console.log("Original array:", original);
console.log("Even numbers:", evenNumbers);