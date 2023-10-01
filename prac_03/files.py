FILE_NAME = "name.txt"

out_file = open(FILE_NAME, "w")
name = input("Name: ")
print(name, file=out_file)
out_file.close()


out_file = open(FILE_NAME, "r")
name = out_file.read().strip()  # Tested with different variable name to ensure output was reading from file.
out_file.close()
print(f"Your name is {name}")


in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(f"The sum of {number_1} and {number_2} is {number_1 + number_2}")


in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(f"The sum of all you numbers is {total}")
