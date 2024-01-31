""" Coding Exercise 1
    Your task is to create a program that generates a random whole number.
    The program first asks the user to enter a whole number.
    Then, once the user enters a number, the program asks the user again to enter another number.
    Then, the program returns a random number that falls between the two whole numbers.
"""
import random
number_lower = int(input("Enter the lower number"))
number_upper = int(input("Enter the upper number"))

if number_upper > number_lower:
    number_randomized = random.randrange(number_lower, number_upper)
    print(f"Randomized number between Lower and Upper: {number_randomized}")
else:
    print('Number lower cannot be greater than Upper number')
