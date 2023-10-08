# Example:
for i in range(1, 21, 2):
    print(i, end=' ')
print()


# a. count in 10s from 0 to 100:
for i in range(0, 101, 10):
    print(i, end=" ")
print()


# b. count down from 20 to 1:
for i in range(20, 0, -1):
    print(i, end=" ")
print()


# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
n = int(input("Number of stars: "))
for i in range(n):
    print("*", end="")
print("\n")  # Added to separate the outputs from question c and d.


# d. print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1.
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print("")
