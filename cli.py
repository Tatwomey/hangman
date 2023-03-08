import random
import time
import copy
from animalsdb import AnimalsDB
from lighthousesdb import LightHousesDB
from programmersdb import ProgrammersDB
from citiesdb import CitiesDB
from usersdb import UsersDB

if __name__ == '__main__':
    animalsdb = AnimalsDB('database.db')
    programmersdb = ProgrammersDB('database.db')
    lighthousesdb = LightHousesDB('database.db')
    citiesdb = CitiesDB('database.db')
    usersdb = UsersDB('database.db')


# The parameters we require to execute the game:

# # choose a category to play and later to add a new word to.
#

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
# choose a category to play and later to add a new word to.
def user_login_signup():
    global username
    global password
    global add_username
    global add_password
    has_username = input('Do you have a username? "y" = yes "n" = no \n ')
    if has_username == 'y':
        print('Log in: \n')
        username = input('Enter your username: \n')
        password = input(f'Enter the password for {username} \n')
        pick_catgory()
        main()
        hangman()
    elif has_username == 'n':
        create_user = input(
            'Would you like to signup? "y" = yes "n" = no \n  ')
        if create_user == 'y':
            add_username = input('Pick a username: \n')
            add_password = input(f'Pick a password for {username} \n')


def user_login_signup():
    global username
    global password
    global add_username
    global add_password
    has_username = input('Do you have a username? "y" = yes "n" = no \n')
    if has_username == 'y':
        print('Log in: \n')
        username = input('Enter your username: \n')
        if usersdb.search_user(f'{username}') == True:
            password = input(f'Enter the password for {username} \n')
            if usersdb.search_password(f'{password}') == True:
                print('Welcome back!')
                pick_category()
                main()
                hangman()
    elif has_username == 'n':
        create_user = input(
            'Would you like to signup? "y" = yes "n" = no \n')
        if create_user == 'y':
            add_username = input('Pick a username: \n')
            add_password = input(f'Pick a password for {add_username} \n')
            usersdb.new_user(add_username, add_password, 0)
            pick_category()
            main()
            hangman()


def pick_category():
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
    global word_random
    word = random.choice(category_picked.list_words())
    word = word.upper()
    word_random = copy.copy(word)
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
        add_word_input = input('Do you want to add a new word? \n')
        while add_word_input not in ['y', 'n', 'Y', 'N']:
            add_word_input = input(
                'Do you want to add a new word? y = yes n = no \n')
        if add_word_input == 'y':
            pick_category()
            word_picked = input('Type your word: \n')
            add_word = category_picked.new_word(word_picked)
            print("Thanks for Playing")
        else:
            print("Thanks For Playing!")
            exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " +
                  display + " Enter your guess: \n")
    guess = guess.strip().upper()
    # if the len of the guess is = 0 or = or more than 2 or its a number
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        # print invalid input and restart the game
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
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
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", word_random)
            play_loop()

    if word == '_' * length:
        print("""

  __     __            __          __ _         _
  \ \   / /            \ \        / /(_)       | |
   \ \_/ /___   _   _   \ \  /\  / /  _  _ __  | |
    \   // _ \ | | | |   \ \/  \/ /  | || '_ \ | |
     | || (_) || |_| |    \  /\  /   | || | | ||_|
     |_| \___/  \__,_|     \/  \/    |_||_| |_|(_)


        """)
        username = input('What is your username?')
        if usersdb.search_user(f'{username}') == True:
            current_score = usersdb.search_score(f'{username}')
            print(current_score)
            new_score = int(current_score)
            new_score += 1
            usersdb.add_score(new_score, username)
            play_loop()

    elif count != limit:
        hangman()


user_login_signup()
# pick_category()
# main()
# hangman()
