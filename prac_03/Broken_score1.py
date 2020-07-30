"""
CP1404/CP5632 - Practical
Broken program to determine score status
The intention is that the score must be between 0 and 100 inclusive;
90 or more is excellent;
50 or more is a pass; below 50 is bad.
"""
import random


def main():
    score = float(input("Enter score: "))
    print(result(score))
    score = random.randint(0, 100)
    print(result(score))


def result(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif 50 <= score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


main()

