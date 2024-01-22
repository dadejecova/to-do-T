from bonus.bonus_Convert_14 import convert
from bonus.bonus_Parse_14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['Feet'], parsed['Inches'])

print(f"{parsed['Feet']} feet and {parsed['Inches']} inches is equal to {result} meters")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide")
