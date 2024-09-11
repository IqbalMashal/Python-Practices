

weight = float(input("Enter your weight: "))

unit = input("Kilograms or punds? (K or L): ")


if unit == "K":
    result = weight * 2.2046
    unit = "Lbs."
elif unit == "L":
    result = weight / 2.2046
    unit = "kgs."
else:
    print(f"{unit} is not a valid option")


print(f"Your weight is: {round(weight, 1)} {unit}")
