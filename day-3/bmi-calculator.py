height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

body_mass_index = round(weight / (height ** 2))

message = "Your BMI is {}, you {}"


def set_message(weight_interpretation: str) -> None:
    global message
    message = message.format(body_mass_index, weight_interpretation) + "."


if body_mass_index < 18.5:
    set_message("are underweight")
elif body_mass_index < 25:
    set_message("have a normal weight")
elif body_mass_index < 30:
    set_message("are slightly overweight")
elif body_mass_index < 35:
    set_message("are obese")
else:
    set_message("are clinically obese")

print(message)
