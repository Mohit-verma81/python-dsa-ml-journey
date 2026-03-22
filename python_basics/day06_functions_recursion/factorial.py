def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


num = int(input("Enter a number: "))
print("Factorial:", factorial(num))
print("Factorial Iterative:", factorial_iterative(num))