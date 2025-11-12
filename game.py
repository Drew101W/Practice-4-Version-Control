#Welcome message
print("Welcome to Rock-Paper-Scissors!")

# Get player's choice
player = input("Choose rock, paper, or scissors: ").strip().lower()
while player not in ("rock", "paper", "scissors"):
    player = input("Invalid choice. Choose rock, paper, or scissors: ").strip().lower()

print("Player chose:", player)
