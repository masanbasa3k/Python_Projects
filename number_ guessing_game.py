import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    user_guess = None
    attempts = 0

    while user_guess != target_number:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if user_guess < target_number:
            print("The target number is higher.")
        elif user_guess > target_number:
            print("The target number is lower.")
    print(f"Congratulations, you found the number in {attempts} attempts!")

number_guessing_game()
