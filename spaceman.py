import random
from life import life

def load_word():
    """Loads random word from text file"""
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close() #Closes file
##creates a secrete word object from the wordslist
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word
    print(load_word()) #Test the load_word function by printing it

def is_word_guessed(secret_word, letters_guessed):
    """Determines if a letter guesed is in password"""
    for l in secret_word:
        if l not in letters_guessed:  #Cannot use not (!=) Because it is searching for each letter in the word
            return True
    return False

def is_given_guess_correct(guessed_letter, secret_word):
    """Returns boolian if the guessed letter is correct"""
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

def spaceman(secret_word):
    """Runs Program and calls all the other functions"""
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
                life(count, secret_word)
                print(f"\nAirlock Countdown: {count}")
            else:
                print("incorrect")
                count -=1
                life(count, secret_word)
                print(f"\nAirlock Countdown: {count}")
        elif count == 0:
            print("AIRLOCK ACTIVATED. NooooOOoOooOo00oooo!!! The passcode was {}".format(secret_word))
    if count > 0:
        print("Im in!! Thank you human! Take me to your leader!")


if __name__ == '__main__':
    secret_word = load_word()
    spaceman(secret_word)
