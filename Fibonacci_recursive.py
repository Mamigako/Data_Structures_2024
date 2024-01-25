"""Returning the Fibbonacci number at index n in the sequence using recursion."""

def fibonacci(n):

    if n <= 1:
        return 1
    
    return fibonacci_recurr(n, 1, 0)


def fibonacci_recurr(counter, current, previous):

    #Base case
    if counter == 2:
        return 1
    
    #Recursive step:
    else:
        return current + fibonacci_recurr(counter-1, current+previous, current)


print(fibonacci(6))