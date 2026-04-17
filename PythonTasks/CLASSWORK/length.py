# first enter the number of the password if it below 8 digit then the password is very weak
# if it is 8 digit then the password should print weak
# else if it longer user should see very strong
# same as every other number longer than 8 digit

number = input ("Length of password: ")
number = len(number)
if   (number <= 8):
      print ("weak")
elif (number <=16):
     print ("Strong")
elif (number > 16):
     print ("very strong")
