document.addEventListener('DOMContentLoaded', () => {
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const operationSelect = document.getElementById('operation');
    const calculateButton = document.querySelector('button');
    const resultParagraph = document.getElementById('result');

    calculateButton.addEventListener('click', () => {
        // Get values from inputs and convert to numbers
        const num1 = parseFloat(num1Input.value);
        const num2 = parseFloat(num2Input.value);
        const operation = operationSelect.value;  // This uses the <option value="...">

        let result;

        // Perform calculation based on the selected operation (using value attribute)
        switch (operation) {
            case 'add':
                result = num1 + num2;
                break;
            case 'subtract':
                result = num1 - num2;
                break;
            case 'multiply':
                result = num1 * num2;
                break;
            case 'divide':
                if (num2 === 0) {
                    result = 'Error: Division by zero!';
                } else {
                    result = num1 / num2;
                }
                break;
            default:
                result = 'Invalid operation';
        }

        // Display the result in <p id="result">
        resultParagraph.textContent = 'Result: ' + result;
    });
});