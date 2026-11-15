library = {
    "Python": 5,
    "Java": 3,
    "C++": 4
}

print("Library Books:", library)

book = input("Enter book name: ")

if book in library:
    print("Available Quantity:", library[book])
else:
    print("Book not found")

new_book = input("Enter new book name: ")
quantity = int(input("Enter quantity: "))

library[new_book] = quantity

print("Updated Library:", library)
