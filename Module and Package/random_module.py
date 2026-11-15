import random
import string

# Generate OTP
otp = random.randint(100000, 999999)
print("OTP:", otp)

# Generate random password
characters = string.ascii_letters + string.digits
password = ""

for i in range(8):
    password += random.choice(characters)

print("Random Password:", password)

# Generate random numbers
numbers = []

for i in range(5):
    numbers.append(random.randint(1, 100))

print("Random List:", numbers)
