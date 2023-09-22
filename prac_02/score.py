"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """Use a users and a random score to allocate a result."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = get_result(score)
    random_result = get_result(random.randint(0, 100))
    print(f"Your result: {result}\nRandom result: {random_result}")


def get_result(number):
    """Allocate a result to a score."""
    if number < 50:
        return "Bad"
    elif number < 90:
        return "Passable"
    else:
        return "Excellent"


main()
