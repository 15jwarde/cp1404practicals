from prac_06.guitar import Guitar


def run_tests():
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Line 6 JTV-59", 2010, 1512.90)

    print(f"{guitar_1.name} get_age() - Expected 101. Got {guitar_1.get_age()}")
    print(f"{guitar_2.name} get_age() - Expected 13. Got {guitar_2.get_age()}")


if __name__ == "__main__":
    run_tests()