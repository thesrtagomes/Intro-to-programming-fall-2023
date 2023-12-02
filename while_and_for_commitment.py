# #como capitalize a letra:

# word = "commitment"
# guess = str(input("What is your guess: "))
# for letter in word:
#     if guess == letter:
#         print(letter.capitalize(), end="")
#     else:
#         print(letter.lower(), end="")


# # como ocultar a letra ao invés de capitalize ela:

# word = "commitment"
# guess = str(input("What is your guess: "))
# for letter in word:
#     if guess.lower() == letter.lower():
#         print("-", end="")
#     else:
#         print(letter, end="")


# ocultando a letra que não é a da palavra:
word = "commitment"
guess_word = list("-" * len(word))  #aqui é para ser a palavra que vai conter os acertos do user

while "".join(guess_word) != word: #o join serve para agrupar os caracteres e as aspas diz que "mao terá espaço entre elas"
    guess = str(input("What is your guess: "))
    for i, letter in enumerate(word):
        if letter.lower() == guess.lower():
            guess_word[i] = letter  #se a letra tiver certa: A posição i vai ser substituida pela letra que foi dada como certa
            print(letter, end="")
        else:
            print('-', end='')
    print('')

