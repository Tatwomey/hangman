import random
import time
from animalsdb import AnimalsDB
from lighthousesdb import LightHousesDB
from programmersdb import ProgrammersDB
from citiesdb import CitiesDB


# class AnimalsDB:
#     def __init__(self, database):
#         self.connect = sqlite3.connect(database)
#         self.cursor = self.connect.cursor()

#     def new_word(self, word):
#         self.cursor.execute(
#             'INSERT OR IGNORE INTO animals (word) VALUES (?)', (word))
#         self.connect.commit()

#     def list_words(self):
#         self.cursor.execute('SELECT word FROM animals')
#         words = self.cursor.fetchall()
#         my_list = [(word[0]) for word in words]
#         return (my_list)

#     def close(self):
#         self.cursor.close()
#         self.connect.close()


if __name__ == '__main__':
    animalsdb = AnimalsDB('database.db')
    programmersdb = ProgrammersDB('database.db')
    lighthousesdb = LightHousesDB('database.db')
    citiesdb = CitiesDB('database.db')
    animalsdb.list_words()

print('''
                                                         _____
     ___  ____                   __   ____              / . . \ 
    /  / /   /                  /  \_/   /              \_____/
   /  /_/   /___ _ ____  ____  /        /___ _____         |
  /  ___   / __ `/  __ \/ __ `/  /\_/  / __ `/ __ \       \|/   
 /  /  /  / /_/ / /  / / /_/ /  /  /  / /_/ / / / /        |
/__/  /__/\__,_/_/  /_/\__, /__/  /__/\__,_/_/ /_/       _/ \_
                      /____/


''')
print("\nWelcome to Hangman game\n")
category = input(
    'Choose a category \n 1)Animals \n 2)Cities \n 3)Programmers by last name \n 4)Light Houses \n')
if category == "1":
    words_to_guess = animalsdb.list_words()
elif category == '2':
    words_to_guess = citiesdb.list_words()
elif category == '3':
    words_to_guess = programmersdb.list_words()
elif category == '4':
    words_to_guess = lighthousesdb.list_words()
else:
    print('Pick a category by number 1 to 4')
    exit()


# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:


def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y" or 'Y':
        main()
    elif play_game == "n" or 'N':
        print("Thanks For Playing! We expect you back again!")
    add_word = input('Do you want to add a new word?')
    while add_word not in ['y', 'n', 'Y', 'N']:
        add_word = input('Do you want to add a new word?')
    # if add_word == 'y' or 'Y':
    #     add_word_category = input('Pick a category to add your word')
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


main()


hangman()
