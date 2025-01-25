def function_with_uncommon_error_solution(n):
    fib_sequence = [0, 1]
    if n <= 1:
        return fib_sequence[n]
    else:
        for i in range(2, n + 1):
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)
        return fib_sequence[n]

# This will not cause a RecursionError
result = function_with_uncommon_error_solution(100) #test with large number