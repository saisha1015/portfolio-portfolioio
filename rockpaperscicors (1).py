#Saisha kapoor
#Period 3

#init
import random
wins = 0
losses = 0
ties = 0
#functions

#main
print("Welcome to Rock, Paper, Scissors")
while True: #infinate Loop
    #Player's Choice
    print("Please select one of the three options")
    player = input("Selection: ")
    #Computer's Choice
    computer = random.randint(1,3)
    if computer == 1:
        computer = "rock"
        print("Computer chose rock")
    elif computer == 2:
        computer = "paper"
        print("Computer chose paper")
    elif computer == 3:
        computer = "scissors"
        print("Computer chose scissors")

    #Determine the outcome
    if player == "rock" and computer == "rock":
        print("Tie Game!")
        ties = ties + 1
    elif player == "rock" and computer == "paper":
        print("computer won!")
        losses = losses + 1
    elif player == "rock" and computer == "scissors":
        print("player won!")
        wins = wins + 1
    elif player == "paper" and computer == "paper":
        print("Tie Game!")
        ties = ties + 1
    elif player == "paper" and computer == "rock":
        print("player won!")
        wins = wins + 1
    elif player == "paper" and computer == "scissors":
        print("computer won!")
        losses = losses + 1
    elif player == "scissors" and computer == "scissors":
        print("Tie Game!")
        ties = ties + 1
    elif player == "scissors" and computer == "rock":
        print("Computer won!")
        losses = losses + 1
    elif player == "scissors" and computer == "paper":
        print("player won!")
        wins = wins + 1
    print(wins)
    print(losses)
    print(ties)



    #Ask player if they want to continue
    playagain = input("Would you like to play again")
    if playagain == "yes":
        print("Restarting...")
    elif playagain == "no":
        break

# = gets the value of
# == is equal to
