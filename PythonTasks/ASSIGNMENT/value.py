# Enter a number between 1 and 2
# if the number is not 1 or 2 
# repeat loop as invalid input until you press 1 or 2 
# then the loop becomes false
# then it breaks
number = input("Enter number between 1 and  2: ")
number = int (number)
while number != 1 and number != 2:
    print ("invalid input ")
    number = input("Enter number between 1 and 2: ")
    number = int (number)
