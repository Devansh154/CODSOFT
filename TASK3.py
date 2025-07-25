import random

# Initial scores
user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors Game!")
print("Instructions: Type rock, paper or scissors to play.")

while True:
    # User input
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    # Valid choices
    choices = ['rock', 'paper', 'scissors']

    # Check if user's input is valid
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # Computer's random choice
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    # Game logic to determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Display scores
    print("Your Score:", user_score, "| Computer Score:", computer_score)

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
