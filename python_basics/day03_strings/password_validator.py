def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if not (has_upper and has_lower and has_digit):
        return "Password must include uppercase, lowercase, and a number"

    return "Strong Password ✅"


input_pwd = input("Enter password: ")
print(validate_password(input_pwd))