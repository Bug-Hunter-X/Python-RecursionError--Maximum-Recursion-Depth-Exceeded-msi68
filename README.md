# Python RecursionError Example

This repository contains a simple Python program that demonstrates a `RecursionError`. The program calculates Fibonacci numbers using recursion. When the input number is large enough, it exceeds the maximum recursion depth, leading to the error.

## Bug Description
The `function_with_uncommon_error` function uses recursion to calculate Fibonacci numbers.  For large input values, this function exceeds Python's default recursion depth limit, resulting in a `RecursionError`. 

## Bug Solution
The `bugSolution.py` file provides a solution to prevent this error by using dynamic programming to avoid repeated recursive calls.