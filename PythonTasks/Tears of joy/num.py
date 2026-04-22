number = input("Enter the amount of number: ")
number = int(number)
for row in range(number):
    for column in range (row + 1):
        print("1", end= " ")
    print()
