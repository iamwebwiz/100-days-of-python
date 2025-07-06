print("Welcome to the Leap Year Calculator!")

year = int(input("Which year do you want to check? "))

message = ''

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            message = "Leap year."
        else:
            message = "Not leap year."
    else:
        message = "Leap year."
else:
    message = "Not leap year."

print(message)
