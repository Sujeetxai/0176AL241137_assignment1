
salary = float(input("Enter your salary: "))
credit = int(input("Enter credit score: "))
age = int(input("Enter your age: "))

if salary >= 30000 and credit >= 700 and 21 <= age <= 60:
    print("Loan Approved")

elif salary >= 30000 and credit >= 700:
    print("Conditionally Approved")

else:
    print("Loan Rejected")
