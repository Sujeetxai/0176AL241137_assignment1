balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise Exception("Insufficient balance")

    balance = balance - amount

    print("Withdrawal successful")
    print("Remaining Balance:", balance)

except Exception as e:
    print("Error:", e)
