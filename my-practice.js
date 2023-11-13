function fibsSum(n) { //This function is used to find the sum of the first n Fibonacci numbers.
    if (n ===1 ) return 1 // is this the base case ???
    if (n === 2) return 2 // or is it this one?
    return fibsSum(n -1) + fib(n)
}


function fib(n) { //This is a helper function to calculate the nth Fibonacci number.
    if ( n===1 ) return 1
    if ( n=== 2) return 1

    return fib(n - 1) + fib( n - 2)
}

console.log(fib(9)) //output 21
console.log(fibsSum(9)) //output 33
