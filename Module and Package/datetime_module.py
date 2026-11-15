from datetime import datetime, date

# Current date and time
now = datetime.now()

print("Current Date:", now.date())
print("Current Time:", now.time())

# Calculate age
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

today = date.today()
dob = date(birth_year, birth_month, birth_day)

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Your Age:", age)
