player1 = input("Enter: rock, paper, scissors: ")
player2 = input("Enter: rock, paper, scissors: ")
if(player1 == player2):
    print("Tie")
if(player1 == "rock"):
    if(player2 == "scissors"):
        print("player1 wins")
else:
    print("player2 wins")
            
