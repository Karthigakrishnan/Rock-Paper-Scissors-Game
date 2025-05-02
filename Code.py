import random
import time

def print_welcome_message():
    print("Welcome to Rock, Paper, Scissors!")
    print("You can type 'rock', 'paper', or 'scissors'.")
    print("Let's see who wins the most rounds!")

def get_user_choice():
    user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def print_winner(user_choice, computer_choice):
    print(f"\nYou chose {user_choice}. Computer chose {computer_choice}.")
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def animate_choice(choice):
    # Fun animation for choices
    animations = {
        'rock': ["   _______", "  |       |", "  |   o   |", "  |_______|"],
        'paper': ["   _______", "  |       |", "  |   P   |", "  |_______|"],
        'scissors': ["   _______", "  |   X   |", "  |   X   |", "  |_______|"]
    }
    print("\nHere comes your choice:")
    for line in animations[choice]:
        print(line)
        time.sleep(0.5)

def play_game():
    print_welcome_message()
    user_score = 0
    computer_score = 0
    rounds = int(input("\nHow many rounds would you like to play? "))

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        animate_choice(user_choice)
        time.sleep(1)  # Pause for dramatic effect

        winner = print_winner(user_choice, computer_choice)
        print(winner)

        if winner == "You win!":
            user_score += 1
        elif winner == "Computer wins!":
            computer_score += 1

        print(f"\nCurrent score - You: {user_score} | Computer: {computer_score}")
        time.sleep(1)

    print("\nFinal Scores:")
    print(f"You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations, you win!")
    elif user_score < computer_score:
        print("Oops, computer wins this time!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    play_game()
