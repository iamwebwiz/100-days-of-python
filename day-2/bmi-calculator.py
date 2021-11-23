height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

body_mass_index = int(int(weight) / (float(height) ** 2))

print(body_mass_index)
