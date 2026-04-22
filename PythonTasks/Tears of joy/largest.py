def largest(number_one, number_two, number_three):
    largest = number_one
    if number_two > largest:
        largest = number_two
    if number_three > largest:
        largest = number_three
    return largest
print (largest(number_three = 50, number_two = 60, number_one = 20))

# using the keyword argument we give name to the variable so it is easily readable
# using positional argument means not defining the actually value to the variable

