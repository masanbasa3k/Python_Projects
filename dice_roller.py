import random

def dice_roll(number):
    dice_result = random.randint(1, number)
    print(f"You rolled a {dice_result}.")



number = int(input('Enter dice face number (2,4,6,8,10,12,20,100) : '))
dice_roll(number)
