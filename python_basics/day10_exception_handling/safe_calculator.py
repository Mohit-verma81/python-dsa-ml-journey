def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid operator"

    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Unexpected error: {e}"


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    print("Result:", calculate(a, b, op))

except ValueError:
    print("Invalid input! Please enter numeric values.")