word = "hangman"

lifeCount = 3
guesses = []

gameDone = False

while not gameDone:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"you have {lifeCount} life, Enter next guess: ")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        lifeCount -= 1
        if lifeCount == 0:
            break
    
    

    gameDone = True
    for letter in word:
        if letter.lower() not in guesses:
            gameDone = False

if gameDone:
    print("yey you win")
else:
    print("sorry mate you lose")
    



