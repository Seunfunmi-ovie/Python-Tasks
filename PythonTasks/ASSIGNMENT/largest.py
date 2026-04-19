largest = None
smallest = None
total = 0 
product = 1
for number in range(3):
    numbertwo = input("Enter number: ")
    numbertwo = float(numbertwo)
    if largest is None or numbertwo > largest:
       largest = numbertwo
    if smallest is None or numbertwo < smallest:
      smallest = numbertwo
    total += numbertwo
    product *= numbertwo
average_score = total/3
print (f"Largest: {largest}")
print (f"Smallest:{smallest} ")
print (f"The Average is : {average_score}")
print (f"Sum: {total}")
print (f"Product: {product}")
