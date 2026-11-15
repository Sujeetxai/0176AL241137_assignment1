
marks = []

for i in range(5):
    m = int(input("Enter marks of subject " + str(i + 1) + ": "))
    marks.append(m)

if any(m < 33 for m in marks):
    print("Result: Fail")

else:
    percentage = sum(marks) / 5

    print("Total Marks:", sum(marks))
    print("Percentage:", percentage)

    if percentage >= 60:
        print("First Division")
    elif percentage >= 50:
        print("Second Division")
    elif percentage >= 40:
        print("Third Division")
