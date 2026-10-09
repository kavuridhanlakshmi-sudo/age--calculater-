from datetime import date

print("--- Age Calculator ---")

try:
    birth_year = int(input("Enter your birth year (YYYY): "))
    birth_month = int(input("Enter your birth month (MM): "))
    birth_day = int(input("Enter your birth day (DD): "))

    dob = date(birth_year, birth_month, birth_day)
    today = date.today()

    age_years = today.year - dob.year
    age_months = today.month - dob.month
    age_days = today.day - dob.day

    if age_days < 0:
        age_months -= 1
        age_days += 30
    
    if age_months < 0:
        age_years -= 1
        age_months += 12

    print(f"\nYour Age is: {age_years} years, {age_months} months, {age_days} days")

except ValueError:
    print("Error: Please enter a valid date.")