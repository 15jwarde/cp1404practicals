MIN_LENGTH = 8


def main():
    """Print a string of asterisks as long as the password input."""
    password = get_password()
    print_stars(password)


def get_password():
    """Ask user for a password that meets the required minimum length."""
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print("Invalid length")
        password = input("Enter password: ")
    return password


def print_stars(password):
    """Print asterisks as long as the password."""
    print(len(password) * "*")


main()
