document.addEventListener('DOMContentLoaded', () => {
    const inputField = document.getElementById('expression');
    const calculateButton = document.querySelector('button');
    const resultParagraph = document.getElementById('result');

    calculateButton.addEventListener('click', () => {
        const expression = inputField.value.trim();

        // Check if input is empty
        if (!expression) {
            resultParagraph.textContent = 'Please enter a calculation';
            return;
        }

        let num1, num2, operator, result;

        // Detect operator: +, -, *, /
        if (expression.includes('+')) {
            [num1, num2] = expression.split('+');
            operator = '+';
        } else if (expression.includes('-')) {
            [num1, num2] = expression.split('-');
            operator = '-';
        } else if (expression.includes('*')) {
            [num1, num2] = expression.split('*');
            operator = '*';
        } else if (expression.includes('/')) {
            [num1, num2] = expression.split('/');
            operator = '/';
        } else {
            resultParagraph.textContent = 'Invalid operator. Use +, -, *, or /';
            return;
        }

        // Convert to integers
        num1 = parseInt(num1);
        num2 = parseInt(num2);

        // Validate numbers
        if (isNaN(num1) || isNaN(num2)) {
            resultParagraph.textContent = 'Please enter valid numbers';
            return;
        }

        // Perform calculation
        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 === 0) {
                    resultParagraph.textContent = 'Error: Division by zero';
                    return;
                }
                result = Math.floor(num1 / num2); // integer division only
                break;
        }

        // Show result
        resultParagraph.textContent = `Result: ${result}`;
    });
});