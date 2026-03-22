def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)


num = int(input("Enter a number: "))
print("Factorial:", factorial(num))