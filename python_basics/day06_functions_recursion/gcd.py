def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


#using recurive
def gcd_recursive(a, b):
    if b == 0:
        return a
    
    print(f"b={b},   a % b={ a % b}")
    return gcd_recursive(b, a % b)

print("GCD:", gcd_recursive(x, y))