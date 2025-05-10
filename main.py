import random

def play_game():
    # Define options for the game
    choices = ['rock', 'paper', 'scissors']
    
    # Prompt the user to enter their choice
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    # Validate user input
    if user_choice not in choices:
        print("Invalid choice, please enter 'rock', 'paper', or 'scissors'.")
        return
    
    # Get the computer's choice (randomly selected)
    computer_choice = random.choice(choices)
    
    # Display choices
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

# Play the game
if __name__ == "__main__":
    play_game()
