import random

user_wins = 0
computer_wins = 0

rock_responses = ["rock", "r"]
scissors_responses = ["scissors", "s"]
paper_responses = ["paper", "p"]

acceptable_responses = rock_responses + scissors_responses + paper_responses

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input in ["q", "quit"]:
        quit()

    if user_input not in acceptable_responses:
        continue

    computer_choice = random.randint(1, 3)
    # rock: 1, paper: 2, scissors: 3
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    elif computer_choice == 3:
        computer_choice = "scissors"
    else:
        print("Unexpected error occured. Computer couldn't make a decision.")
        continue

# game result will be represented by -1 = loss, 0 = draw, 1 = win. From the players perspective.

    if user_input.lower() == "r":
        user_input = "rock"

    elif user_input.lower() == "s":
        user_input = "scissors"

    elif user_input.lower() == "p":
        user_input = "paper"

    if user_input in rock_responses:
        if computer_choice == "rock":
            result = 0

        elif computer_choice == "paper":
            result = -1

        elif computer_choice == "scissors":
            result = 1

    elif user_input in paper_responses:
        if computer_choice == "rock":
            result = 1
        
        elif computer_choice == "paper":
            result = 0

        elif computer_choice == "scissors":
            result = -1

    elif user_input in scissors_responses:
        if computer_choice == "rock":
            result = -1

        elif computer_choice == "paper":
            result = 1

        elif computer_choice == "scissors":
            result = 0

    else:
        print("Unexpected error occured. Comparing player and computer choices raised an error.")
        continue

    if result == -1:
        print(f"Loss! You chose {user_input.title()} CPU chose {computer_choice.title()}")
        computer_wins += 1

    elif result == 0:
        print(f"Draw! You both chose {user_input.title()}")

    elif result == 1:
        print(f"Win! You chose {user_input.title()} CPU chose {computer_choice.title()}")
        user_wins += 1

    print(f"Player Wins: {user_wins}\nCPU Wins: {computer_wins}")
        

