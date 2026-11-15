
n = int(input("Enter number of rows: "))

print("\nRight Triangle:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nPyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("\nDiamond:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * (2 * i - 1))
