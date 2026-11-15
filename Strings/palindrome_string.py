
s = input("Enter a string: ")

s = s.replace(" ", "").lower()

if s == s[::-1]:
    print("Palindrome String")
else:
    print("Not a Palindrome String")
