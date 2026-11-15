students = {
    "Aman": 85,
    "Rahul": 72,
    "Priya": 91,
    "Rohit": 28,
    "Neha": 65
}

topper = max(students, key=students.get)
average = sum(students.values()) / len(students)

print("Topper:", topper)
print("Highest Marks:", students[topper])
print("Average Marks:", average)

print("Failed Students:")
for name, marks in students.items():
    if marks < 33:
        print(name, marks)
