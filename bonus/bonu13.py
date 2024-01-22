feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"Feet": feet, "Inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches)

result = convert(parsed['Feet'], parsed['Inches'])

print(f"{parsed['Feet']} feet and {parsed['Inches']} inches is equal to {result} meters" )

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide")
