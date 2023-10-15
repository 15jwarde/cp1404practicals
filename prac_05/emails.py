"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes  # Estimate as I forgot to record my time on the second day of working on this.
"""

def main():
    """Get users name and email."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        is_name = input(f"Is your name {name}? (Y/n)").upper()
        if is_name != "Y" and is_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name, in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    """Get name from email."""
    full_name = email.split('@')[0]
    split_name = full_name.split('.')  # does this sound too much like a verb?
    name = " ".join(split_name).title()
    return name


main()
