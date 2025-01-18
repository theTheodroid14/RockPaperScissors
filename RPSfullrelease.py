import random
import sys  

version = 1.0
stats = [0, 0, 0]
def game():
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
        if opponentsmove == "rock" and ourmove == "scissors":
            print("You Lose!")
            stats[2] += 1
        elif opponentsmove == "scissors" and ourmove == "paper":
            print("You Lose!")
            stats[2] += 1
        elif opponentsmove == "paper" and ourmove == "rock":
            print("You Lose!")
            stats[2] += 1
        elif opponentsmove == ourmove:
            print("It's a tie!")
            stats[1] += 1
        else:
            print("You win!")
            stats[0] += 1

    check()

    def finishing():
        command = input("Game is finished. Press Enter to restart, type 'x' or 'close' to exit, or 'stats' to see stats: ").lower()
        if command == "":
            game()
        elif command == "x" or command == "close":
            sys.exit(1)
        elif command == "stats":
            print("Wins:", stats[0])
            print("Ties:", stats[1])
            print("Loses:", stats[2])
            game()   
        else:
            game()

    finishing()

game()
