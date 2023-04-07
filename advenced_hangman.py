import random
WORDLIST_FILENAME = "words.txt"

def load_words():
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "Words.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    tempC = 0
    for letter in secret_word:
        if letter in letters_guessed:
            tempC += 1

    if tempC == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word


def get_available_letters(letters_guessed):
    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z', 'x', 'w', 'q']
    for letter in letters_guessed:
        if letter in alfabe:
            alfabe.remove(letter)
    print("You life use this latters: " + "".join(alfabe))

def Hangman(secret_word):
    life = 6
    penal = 3
    letters_guessed = []

    print(f"word has {len(secret_word)} letters, and you have 6 life \nLets start !")
    get_guessed_word(secret_word, letters_guessed)

    run = True
    while run:
        if is_word_guessed(secret_word, letters_guessed):
            print("You Win !!")
            run = False
            break
        if life <= 0:
            run = False
            break
        print(f"You have {life} life !!")
        print(f"You have {penal} penal")
        get_available_letters(letters_guessed)
        letter = input("Guess a letter:")
        if type(letter) != str or len(letter) != 1:
            print("Please enter only letter!")
            continue
        else:
            if letter in letters_guessed:
                if penal == 1:
                    run = False
                    break
                else:
                    penal -= 1
                    print("Already guessed!!")
                get_guessed_word(secret_word, letters_guessed)
            else:
                letters_guessed.append(letter)
                if letter in secret_word:
                    get_guessed_word(secret_word, letters_guessed)
                else:
                    get_guessed_word(secret_word, letters_guessed)
                    life -= 1


def show_possible_matches(my_word):
    global wordlist
    if my_word == len(my_word)*"_":
        print("Guess a letter first!")
    else:
        for letter in wordlist:
            if len(my_word) != len(letter):
                continue
            match = True
            for i in range(len(my_word)):
                if my_word[i] != "_" and my_word[i] != letter[i]:
                    match = False
                    break
            if match:
                print(letter)
    

def Hangman_With_Clue(secret_word):
    life = 6
    penal = 3
    letters_guessed = []

    print(f"word has {len(secret_word)} letters, and you have 6 life \nLets start !")
    print(get_guessed_word(secret_word, letters_guessed))

    run = True
    while run:
        if is_word_guessed(secret_word, letters_guessed):
            print("You Win !!")
            run = False
            break
        if life <= 0:
            run = False
            print(secret_word)
            break
        print(f"You have {life} life !!")
        print(f"You have {penal} penal")
        get_available_letters(letters_guessed)
        letter = input("Guess a letter:")
        if type(letter) != str or len(letter) != 1:
            print("Please enter one letter or enter * for take a clue")
            continue
        elif letter == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            if letter in letters_guessed:
                if penal == 1:
                    run = False
                    break
                else:
                    penal -= 1
                    print("Already guessed!!")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(letter)
                if letter in secret_word:
                    print(get_guessed_word(secret_word, letters_guessed))
                else:
                    print(get_guessed_word(secret_word, letters_guessed))
                    life -= 1

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    Hangman_With_Clue(secret_word)
