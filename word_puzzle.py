# I have exceeded requirements through adding a variable containing a list of possible words to be randomly selected as a secret word.

import random
print(
    "Welcome to the word puzzle game! This game provides some hints along the way. "
    "When you choose a word, if its letter is at the same position as the magic word, it will appear "
    "as an uppercase letter. If the letter exists but at a different order, it will appear as a lowercase letter. "
    "Good luck!"
)
print('')
possible_words = ['brigadeiro', 'pastel', 'hotdog', 'sorvete', 'chocolate']
secret_word = random.choice(possible_words)
word = "_ " * len(secret_word)
print(f"Your hint is: {word}")
guess = str(input("What is your guess? "))
attempts = 1
while guess.lower() != secret_word:
    attempts = attempts + 1
    if len(guess) != len(secret_word):
        print(
            "Sorry, the guess must have the same number of letters as the secret word."
        )
    else:
        for i, guess_letter in enumerate(guess.lower()):
            if guess_letter == secret_word[i]:
                print(f'{guess_letter.upper()} ', end="")
            elif guess_letter in secret_word:
                print(f'{guess_letter.lower()} ', end="")
            else:
                print("_ ", end="")
    print("")
    guess = str(input("What is your guess? "))
print("Congratulations! you guessed it!")
print(f"It took you {attempts} guesses.")
