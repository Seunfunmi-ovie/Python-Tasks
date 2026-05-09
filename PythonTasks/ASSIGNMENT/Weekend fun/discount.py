total_bill = input("Enter bill: ")
total_bill = int(total_bill)
is_member = input("Enter Yes or No: ")
if(total_bill >= 1000 and is_member == "yes"):
    print("10% Off")
elif(total_bill >= 1000 and not is_member ):
    print("5% Off")
else:
    print("No discount")        
    
