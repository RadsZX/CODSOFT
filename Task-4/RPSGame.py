import random

user_score=0
computer_score=0

def get_user_choice():
    while True:
        try:
            user_choice = int(input("Enter your choice (1 for Rock, 2 for Paper, or 3 for Scissors): "))
            if user_choice in [1, 2, 3]:
                return user_choice
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        global user_score
        user_score+=1
        return "You won!"
    else:
        global computer_score
        computer_score+=1
        return "You lost!"

def play_again():
    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            return True
        elif play_again.lower() == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def play_game():
    print("Welcome to Rock Paper Scissors Game!\n")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Computer's choice:", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if not play_again():
            print("Your score:",user_score,"\nComputer score",computer_score)
            break

play_game()
