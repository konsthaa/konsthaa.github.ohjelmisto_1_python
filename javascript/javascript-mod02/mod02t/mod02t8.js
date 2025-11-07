// Write a function called concat(), which receives an array of strings as a parameter. The function returns a string formed by concatenating the elements of the array. (2p)
// Example: In a four-item array, there are items Johnny, DeeDee, Joey and Marky. The function returns the string JohnnyDeeDeeJoeyMarky.
// Do not use array.join() function
// You can hardcode the array, no need for prompt().
// Print the result to HTML document.

javascript// Function: concat() - concatenates array of strings without using join()
function concat(arr) {
    let result = "";
    for (let i = 0; i < arr.length; i++) {
        result += arr[i];
    }
    return result;
}

// Hardcoded array of strings
let names = ["Johnny", "DeeDee", "Joey", "Marky"];

// Call the function
let concatenated = concat(names);

// Print result to HTML document
document.body.innerHTML = `
    <h2>Concatenated String</h2>
    <p><strong>Input array:</strong> ${names.join(", ")}</p>
    <p><strong>Output:</strong> ${concatenated}</p>
`;