import random
#Welcome message
print("Welcome to Rock-Paper-Scissors!")

# Get player's choice
player = input("Choose rock, paper, or scissors: ").strip().lower()
while player not in ("rock", "paper", "scissors"):
    player = input("Invalid choice. Choose rock, paper, or scissors: ").strip().lower()

print("Player chose:", player)

#Computer's choice 
# ------------------------------------------
computer = random.choice(["rock", "paper", "scissors"])
print("Computer chose:", computer)

#------------------------------------------


# decide winner
if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("Player wins!")
else:
    print("Computer wins!")