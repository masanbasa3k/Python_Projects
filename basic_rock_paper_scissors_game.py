print("Rock, Paper, Scissors")

while True:
    # Ask the player to make a choice
    print("Enter choice \n1 for Rock \n2 for Paper \n3 for Scissors")
    player_choice = int(input("Your turn: "))

    # Check if the player's choice is valid
    if player_choice not in [1, 2, 3]:
        print("Invalid input, try again")
        continue

    # Assign a name to the player's choice
    if player_choice == 1:
        player_choice_name = 'rock'
    elif player_choice == 2:
        player_choice_name = 'paper'
    else:
        player_choice_name = 'scissors'

    # Print the player's choice
    print(f"Player chose {player_choice_name}")

    # Computer makes a choice
    import random
    computer_choice = random.randint(1, 3)

    # Assign a name to the computer's choice
    if computer_choice == 1:
        computer_choice_name = 'rock'
    elif computer_choice == 2:
        computer_choice_name = 'paper'
    else:
        computer_choice_name = 'scissors'

    # Print the computer's choice
    print(f"Computer chose {computer_choice_name}")

    # Check who won
    if player_choice == computer_choice:
        print("It's a tie")
    elif player_choice == 1 and computer_choice == 2:
        print("Computer wins")
    elif player_choice == 2 and computer_choice == 1:
        print("Player wins")
    elif player_choice == 1 and computer_choice == 3:
        print("Player wins")
    elif player_choice == 3 and computer_choice == 1:
        print("Computer wins")
    elif player_choice == 2 and computer_choice == 3:
        print("Computer wins")
    elif player_choice == 3 and computer_choice == 2:
        print("Player wins")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (Y/N)").lower()
    if play_again == 'n':
        break