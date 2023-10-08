numbers = []

for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)

average = sum(numbers) / 5

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {average}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

guess = input("Username: ")

if guess in usernames:
    print("Access granted")
else:
    print("Access denied")
