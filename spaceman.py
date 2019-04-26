import random

#I got help From Marrianna Campbel on this one. Our code may be simular.
def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close() #Closes file

##creates a secrete word object from the wordslist
   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word
   print(load_word()) #Test the load_word function by printing it



def is_word_guessed(secret_word, letters_guessed):
    for l in secret_word:
        if l not in letters_guessed:  #Cannot use not (!=) Because it is searching for each letter in the word
            return True
    return False


def is_given_guess_correct(guessed_letter, secret_word):
    if guessed_letter in secret_word:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    word = ""  #Declare a variable with an empty string
    for letter in secret_word:  #Starts a for loop for letters get_guessed_word
        if letter in letters_guessed:
            word += letter + ""  # Could I rewrite this with .append?
    else:
        word += "_"
    return word



def get_available_letters(letters_guessed):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    for letter in letters_guessed: #starts a for loop
        alpha.remove(letter) #removes chosen letter from alpha list
    return alpha


def user_input (prompt):
    user_input = input(prompt)
    return user_input

def life(count):
    if count == 7:
        print("V")
        print("O")
    if count == 6:
        print("V")
        print("O")
        print("|")
    if count == 5:
        print(" V")
        print(" O")
        print(" |")
        print("/")
    if count == 4:
        print(" V")
        print(" O")
        print(" |")
        print("/ \ ")
    if count == 3:
        print(" V")
        print(" O")
        print("-|")
        print("/ \ ")
    if count == 2:
        print("|  V  |")
        print("|  O  |")
        print("| -|- |")
        print("| / \ |")
    if count == 1:
        print("  ___   ")
        print(" /   \ ")
        print("|  V  |")
        print("|  O  |")
        print("| -|- |")
        print("| / \ |")
        print(" \___/")
    if count == 0:
        print("Ahhhhh NOoooooOoooOOo!!!!")
        print("***___***   ")
        print("**/***\**")
        print("*|**V**|*")
        print("*|**O**|*")
        print("*|*-|-*|*")
        print("*|*/*\*|*")
        print("**\___/**")
        print("*********")
        print("AIRLOCK ACTIVATED! YOU LOSE")
        print(" NooooOOoOooOo00oooo!!!\n The passcode was {}".format(secret_word))


def spaceman(secret_word):
    secret_word_ln = len(secret_word)  #saves lenght of string to objects
    letters_guessed = []
    count = 8
    print("Welcome to the Spaceman's Airlock")
    print("I come in peace, GET ME OUT OF THIS AIRLOCK!")
    print("Please Help me hack the passcode, by guessing the letters: ")
    print("The passcode has %s charictors " % secret_word_ln)
    print("You have 7 guesses before the airlock automatically opens.")

    while is_word_guessed(secret_word, letters_guessed) and count > 0:
        guessed_letter = input("Guess a Letter HotShot ")
        if guessed_letter not in letters_guessed:
            letters_guessed.append(guessed_letter)
            print("So far, you have guessed:{}".format(letters_guessed)) #shows word with underscores for tcorrect letters in order
            print("Revealed Password: {}".format(get_guessed_word(secret_word, letters_guessed)))
            #Create if statement to determine if letters are correctly

            if is_given_guess_correct(guessed_letter, secret_word):
                print("Correct!")
                life(count)
                print(f"\nAirlock Countdown: {count}")
            else:
                print("incorrect")
                count -=1
                life(count)
                print(f"\nAirlock Countdown: {count}")

        elif count == 0:
            print("AIRLOCK ACTIVATED. NooooOOoOooOo00oooo!!! The passcode was {}".format(secret_word))

    if count > 0:
        print("Im in!! Thank you human! Take me to your leader!")



secret_word = load_word()
spaceman(secret_word)
