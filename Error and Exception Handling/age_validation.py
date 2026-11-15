try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise Exception("Age must be 18 or above")

    print("You are eligible.")

except Exception as e:
    print("Error:", e)
