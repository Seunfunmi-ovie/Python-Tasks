age = input("Enter your age: ")
age = int(age)
if(age < 5):
    print("Free")
elif(age < 5 or age == 12):
    print("$5")
elif (age == 13 or age <= 64):
    print("$12")
else:
    print("$8")        

    
