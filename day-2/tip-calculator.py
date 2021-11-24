print("Welcome to the tip calculator!")
print("------------------------------")
bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

bill_as_number = float(bill)
tip_percentage_as_int = int(tip_percentage)
tip = bill_as_number * (tip_percentage_as_int / 100)
total_bill = bill_as_number + tip
bill_per_person = total_bill / int(people)

message = f"Each person should pay: ${bill_per_person:.2f}"

print(message)
