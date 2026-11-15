
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while b != 0:
    r = a % b
    a = b
    b = r

hcf = a
lcm = (x * y) // hcf

print("HCF =", hcf)
print("LCM =", lcm)
