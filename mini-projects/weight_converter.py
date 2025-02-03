# Python Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit.upper() == 'K':
    weight *= 2.205
    unit = 'Lbs.'
    print(f"Your weight is: {weight:.2f} {unit}")
elif unit.upper() == 'L':
    weight /= 2.205
    unit = "Kgs."
    print(f"Your weight is: {weight:.2f} {unit}")
else:
    print(f"{unit} was not valid.")
