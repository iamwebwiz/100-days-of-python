age = int(input("What is your current age? "))

TOTAL_YEARS = 90

years_remaining = TOTAL_YEARS - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

output = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."

print(output)
