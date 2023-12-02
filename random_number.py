# import random
# number = random.randint(1, 12)
# print("Let's play!")
# print(f"What is the magic number: ")
# hint = 1
# guess = int(input("What is your guess?"))
# while guess != number:
#     if guess < number:
#          print("Hint: Higher.")
#     elif guess > number:
#          print("Hint: Lower.")
#     guess = int(input("What is your guess?"))
#     hint = hint + 1
# print(f"Congratulations! You got it. It took you {hint} hints!")


# usando randint importado do random eu digo que quero um número aleatório
# entre primero numero e segundo numero.

import random
guesses = 1
magic_number = random.randint(1,15)
guess = int(input("What is your guess? "))
while magic_number != guess:
     if magic_number < guess:
          print("Lower")
     else:
          print("Higher")
     guess = int(input("What is your guess? "))
     guesses = guesses + 1
print("You guessed it!")
print (f'You have tried {guesses} times!')
