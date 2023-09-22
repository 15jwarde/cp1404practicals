min_length = 8
password = input("Enter password: ")
while len(password) < min_length:
    print("Invalid length")
    password = input("Enter password: ")
print(len(password) * "*")