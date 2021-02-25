import math

def fibonacci(n):
    if n < 0:
        raise Exception("Not in range of fibonacci")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(f):
    if f < 2:
        return 1
    else:
        return f * factorial(f - 1)


