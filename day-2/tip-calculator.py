print("Welcome to the tip calculator!")
print("------------------------------")
bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
splitters = input("How many people to split the bill? ")

bill_as_number = float(bill)
tip_percentage_as_int = int(tip_percentage)
tip = bill_as_number * (tip_percentage_as_int / 100)
total_bill = bill_as_number + tip
splits = total_bill / int(splitters)

message = f"Each person should pay: ${round(splits, 2)}"

print(message)
