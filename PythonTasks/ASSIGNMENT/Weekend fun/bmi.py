weight = input("Enter weight: ")
weight = int(weight)
height = input("Enter height: ")
height = int(height)
bmi = (weight/(height * height))
if(bmi < 18.5):
    print("Underweight")
elif(bmi == 18.5 or bmi <= 24.8):
    print("Normal")
elif(bmi == 25 or bmi <= 29.9):
    print("Overweight")
else:
    print("Obese")
            

