import random

ourmove = input("Rock, Paper or Scissors? ").lower()


opponentsmoveint = random.randint(1, 3)

def pick():
    global opponentsmove  
    if opponentsmoveint == 1:
        opponentsmove = "rock"
    elif opponentsmoveint == 2:
        opponentsmove = "paper"
    else:
        opponentsmove = "scissors"

pick()

print("Opponent chose: " + opponentsmove)

def check():
    
    if ourmove not in ["rock", "paper", "scissors"] or ourmove == "":
        print("Answer correctly (choose rock, paper, or scissors)")
        return  
    
    # Check the answer for win/lose/tie outcome
    if opponentsmove == "rock" and ourmove == "scissors":
        print("You Lose!")
    elif opponentsmove == "scissors" and ourmove == "paper":
        print("You Lose!")
    elif opponentsmove == "paper" and ourmove == "rock":
        print("You Lose!")
    elif opponentsmove == ourmove:  
        print("It's a tie!")
    else:
        print("You win!")

check()

input("Game is finished Press Enter to close!")
