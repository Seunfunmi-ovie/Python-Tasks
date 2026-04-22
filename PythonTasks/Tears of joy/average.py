number = input("Enter amount of number: ")
number = int(number)
total = 0
for i in range(number):
    score =  input("Enter the number: ")
    score = int(score)
    total += score
average_score = total/number
print(f"The average score is {average_score}")
