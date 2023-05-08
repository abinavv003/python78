import random

# function to get user's choice
def get_user_choice():
    user_choice = input("Choose stone (s), paper (p), or scissors (x): ")
    while user_choice not in ['s', 'p', 'x']:
        user_choice = input("Invalid choice. Choose stone (s), paper (p), or scissors (x): ")
    return user_choice

# function to get computer's choice
def get_computer_choice():
    choices = ['s', 'p', 'x']
    computer_choice = random.choice(choices)
    return computer_choice

# function to determine the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == 's' and computer_choice == 'x':
        return "user"
    elif user_choice == 'p' and computer_choice == 's':
        return "user"
    elif user_choice == 'x' and computer_choice == 'p':
        return "user"
    else:
        return "computer"

# main function to play the game
def play_game():
    print("Let's play Stone-Paper-Scissors!")
    num_rounds = int(input("How many rounds do you want to play? "))
    user_wins = 0
    computer_wins = 0
    ties = 0
    for i in range(num_rounds):
        print(f"\nRound {i+1}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chooses {computer_choice}")
        winner = get_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win!")
            user_wins += 1
        elif winner == "computer":
            print("Computer wins!")
            computer_wins += 1
        else:
            print("It's a tie!")
            ties += 1
    print("\nGame over!")
    print(f"You won {user_wins} rounds.")
    print(f"The computer won {computer_wins} rounds.")
    print(f"There were {ties} ties.")
    if user_wins > computer_wins:
        print("You win the game!")
    elif computer_wins > user_wins:
        print("The computer wins the game!")
    else:
        print("The game is tied!")

# start the game
play_game()
