
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Palindrome numbers are:")

for i in range(start, end + 1):
    n = i
    rev = 0

    while n > 0:
        r = n % 10
        n = n // 10
        rev = rev * 10 + r

    if i == rev:
        print(i, end=" ")


