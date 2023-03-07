import random
import time
from animalsdb import AnimalsDB
from lighthousesdb import LightHousesDB
from programmersdb import ProgrammersDB
from citiesdb import CitiesDB

if __name__ == '__main__':
    animalsdb = AnimalsDB('database.db')
    programmersdb = ProgrammersDB('database.db')
    lighthousesdb = LightHousesDB('database.db')
    citiesdb = CitiesDB('database.db')
    animalsdb.list_words()

# The parameters we require to execute the game:


print('''                



                        WELCOME TO 
                                                         _____
     ___  ____                   __   ____              / . . \ 
    /  / /   /                  /  \_/   /              \_____/
   /  /_/   /___ _ ____  ____  /        /___ _____         |
  /  ___   / __ `/  __ \/ __ `/  /\_/  / __ `/ __ \       \|/   
 /  /  /  / /_/ / /  / / /_/ /  /  /  / /_/ / / / /        |
/__/  /__/\__,_/_/  /_/\__, /__/  /__/\__,_/_/ /_/       _/ \_
                      /____/


''')


# choose a category to play and later to add a new word to.


def pick_catgory():
    global category_picked
    category = input(
        'Choose a category \n 1)Animals \n 2)Cities \n 3)Programmers by last name \n 4)Light Houses \n')
    if category == "1":
        category_picked = animalsdb
        print('You picked Animals')
    elif category == '2':
        category_picked = citiesdb
        print('You picked Cities')
    elif category == '3':
        category_picked = programmersdb
        print('You Picked Programmers by last name')
    elif category == '4':
        category_picked = lighthousesdb
        print('You picked Light Houses')
    else:
        print('Pick a category by number 1 to 4')
        exit()


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word = random.choice(category_picked.list_words())
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:


def play_loop():
    global word_picked
    global play_game
    global add_word
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        add_word = input('Do you want to add a new word? \n ')
        while add_word not in ['y', 'n', 'Y', 'N']:
            add_word_input = input('Do you want to add a new word? \n')
            if add_word_input == 'y' or 'Y':
                pick_catgory()
                word_picked = input('Type your word: \n')
                add_word = category_picked.new_word(word_picked)
            print("Thanks For Playing!")
        exit()

# Initializing all the conditions required for the game:


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " +
                  display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) +
                  " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


pick_catgory()
main()
hangman()
