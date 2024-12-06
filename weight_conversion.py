weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds (K or L): ")
if unit == "K":
    weight = weight * 2.205
    unit = "LBS."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} ia not a valid input.")

print(f"Your weight is {round(weight,1)} {unit}.")