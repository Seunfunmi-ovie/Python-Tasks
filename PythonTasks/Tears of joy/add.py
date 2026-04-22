number = input("Enter the number: ")
number = int (number)
for row in range(number):
    for column in range(row +1):
        print(column + 1, end= " ")
    print ()

