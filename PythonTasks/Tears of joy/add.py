#This is allows the user to collect number then collect the number of row and column to print a right angle.
number = input("Enter the number: ")
number = int (number)
for row in range(number):
    for column in range(row +1):
        print(column + 1, end= " ")
    print ()

