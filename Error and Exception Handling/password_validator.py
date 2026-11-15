class PasswordError(Exception):
    pass


password = input("Enter your password: ")

try:
    if len(password) < 8:
        raise PasswordError("Password must contain at least 8 characters")

    if not any(char.isupper() for char in password):
        raise PasswordError("Password must contain an uppercase letter")

    if not any(char.isdigit() for char in password):
        raise PasswordError("Password must contain a number")

    print("Password is valid")

except PasswordError as e:
    print("Error:", e)
