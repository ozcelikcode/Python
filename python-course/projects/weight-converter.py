weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")

print(f"Your weights is: {round(weight, 1)} {unit}")