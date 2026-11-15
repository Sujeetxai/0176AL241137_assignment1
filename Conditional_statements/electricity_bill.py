n = float(input("Enter Unit Consumed: "))

total = 0
surcharge = 0

if n <= 100:
    total = n * 5

elif n <= 300:
    total = (100 * 5) + (n - 100) * 7

else:
    total = (100 * 5) + (200 * 7) + (n - 300) * 10

if total > 2000:
    surcharge = (total * 5) / 100

print("Unit consumed:", n)
print("Bill:", total)
print("Surcharge charges:", surcharge)
print("Total Bill:", total + surcharge)
