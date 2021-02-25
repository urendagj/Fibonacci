import math

def fibonacci(n):
    if n < 0:
        print("Not in range of fibonacci")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

