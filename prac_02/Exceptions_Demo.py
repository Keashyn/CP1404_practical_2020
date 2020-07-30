"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if  denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
"""""
1. When will a ValueError occur? When any character other than a valid integer is entered into either the
numerator or denominator fields.
2. When will a ZeroDivisionError occur? When a negative number is inserted in the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Add an if statement that continues
    to prompt the user until a valid denominator is entered.
"""""
