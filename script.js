function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculateResult() {
    const display = document.getElementById('display');
    try {
        // Using eval to evaluate the arithmetic expression
        display.value = eval(display.value);
    } catch {
        display.value = 'Error';
    }
}
