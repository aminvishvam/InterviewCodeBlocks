/**
 * Calculates the nth Fibonacci number iteratively.
 *
 * @param {number} n The index (non-negative integer) in the Fibonacci sequence.
 * @returns {number | undefined} The nth Fibonacci number, or undefined if the input is negative.
 */
function fibonacciIterative(n) {
    if (n < 0) {
        console.error("Input must be a non-negative integer.");
        return undefined;
    }
    if (n === 0) {
        return 0;
    }
    if (n === 1) {
        return 1;
    }

    let a = 0;
    let b = 1;
    let result = 0; // To store the current Fibonacci number

    // Start loop from 2 because F(0) and F(1) are already handled
    for (let i = 2; i <= n; i++) {
        result = a + b;
        a = b;
        b = result;
    }

    return b; // Or result, since b will hold the nth Fibonacci number after the loop
}

// Let's test it out!
console.log("Fibonacci sequence (iterative):");
console.log("F(0):", fibonacciIterative(0));   // Expected: 0
console.log("F(1):", fibonacciIterative(1));   // Expected: 1
console.log("F(2):", fibonacciIterative(2));   // Expected: 1
console.log("F(3):", fibonacciIterative(3));   // Expected: 2
console.log("F(4):", fibonacciIterative(4));   // Expected: 3
console.log("F(5):", fibonacciIterative(5));   // Expected: 5
console.log("F(6):", fibonacciIterative(6));   // Expected: 8
console.log("F(10):", fibonacciIterative(10)); // Expected: 55
console.log("F(-1):", fibonacciIterative(-1)); // Expected: undefined (with error message)
