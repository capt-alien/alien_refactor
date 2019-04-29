def life(count, secret_word):
    """Gives life count after guess"""
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

text = [
    "Welcome to the Spaceman's Airlock",
    "I come in peace, GET ME OUT OF THIS AIRLOCK!",
    "Please Help me hack the passcode, by guessing the letters:",
    "The passcode has {} charictors ",
    "You have 7 guesses before the airlock automatically opens.",
    "Guess a Letter HotShot ",
    "So far, you have guessed:{}",
    "Revealed Password: {}",
    "Correct!",
    "Airlock Countdown: {}",
    "incorrect",
    "AIRLOCK ACTIVATED. NooooOOoOooOo00oooo!!! The passcode was {}",
    "Im in!! Thank you human! Take me to your leader!"
]
