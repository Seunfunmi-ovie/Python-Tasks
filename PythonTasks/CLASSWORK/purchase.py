#start by entering the total spending in the store
# if the purchase is between 1000 and 10000 then the customer is to have a 5% discount
#else if the purchase is 10000 and 500000 then the customer get 10% discount
# else if above 50000 receive a 20 discount



customer = input("Customer total spending:  ")
customer = float (customer)
if customer <= 10000:
    discount = customer * 0.05
    print("Discount: ", discount)
elif customer <= 50000:
     discount = customer * 0.10
     print("Discount: ", discount)
elif customer <= 5000:
     discount = customer * 0.20
     print("Discount: ", discount)

   
