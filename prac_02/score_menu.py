MENU = "(G)et a valid score (0-100)\n(P)rint result\n(S)how stars\n(Q)uit)"


def main():
    """Error check a score to allocate it a result and print the score as stars."""
    score = 0
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("> ").upper()
    print("Farewell :)")


def get_valid_score():
    """Return a valid score."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def get_result(number):
    """Allocate a result to a score."""
    if number < 50:
        return "Bad"
    elif number < 90:
        return "Passable"
    else:
        return "Excellent"


def print_stars(score):
    """Print asterisks as long as the score."""
    print(score * "*")


main()
