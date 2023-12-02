# I showed the game to my mom and boyfriend. My mother has no idea of how coding works, so she played (with me translating) and after that I shoed the code.
# My boyfriend is a senior developer, so he took a look and played with me. He always gives me courage to keep learning.

print("Welcome to our Adventure Game!")
print(" ")
print(
    "You are walking in the middle of a dark forest, when you find an old box with two different books:"
)
color = str(
    input("a RED one, and a BLUE one. Which one do you choose? Please type the color: ")
)

if color.lower() == "blue":
    print(
        "Wow! You have discovered the Blue Pearl book from centuries ago. It was lost, and now you found it!"
    )
    blue_do = str(
        input(
            "It teaches how to become a powerful wizard. What will you do? READ a spell or BURY the book?"
        )
    )
    if blue_do.lower() == "read":
        print("which spell do you wanna learn?")
        read_spell = str(input("FIRE control, TIME traveling or to be INVISIBLE?"))
        if read_spell.lower() == "time":
            print("You can visit any era of time. That is insane!")
        elif read_spell.lower() == "invisible":
            print(" Now you can be an invisible witcher! That is awesome.")
        elif read_spell.lower() == "fire":
            print("You are so powerful controlling the fire!")
        else:
            print("I did not understand, please try again...")

    elif blue_do.lower() == "bury":
        print("People are looking for this book and your life is in dangerous!")
        bury_decision = str(input("Will you DESTROY the book or RUN far away with it?"))
        if bury_decision.lower() == "run":
            print(
                "You gotta go faster, because there are people looking for this book. You should hide yourself, now!"
            )
        elif bury_decision.lower() == "destroy":
            print(
                "Oh no! Now that you have destroyed the book, you cannot become a powerful wizard. That is so sad..."
            )
        else:
            print("I did not understand, please try again...")
    else:
        print("I did not understand, please try again...")
elif color.lower() == "red":
    print("You have discovered the red healing book. It was a gift from the Gods!")
    red_do = str(input("Will you READ it or SELL it? "))
    if red_do.lower() == "read":
        print("which healing secret do you wanna learn?")
        healing_book = str(input("eternal BEAUTY, eternal LIFE or eternal WISDOM? "))
        if healing_book.lower() == "beauty":
            print(
                "Now you can learn and teach all the best secrets about beauty for everyone!"
            )
        elif healing_book.lower() == "life":
            print("Look at you! Now you know how to life forever.")
        elif healing_book.lower() == "wisdom":
            print("You have acquired all the knowledge from the Gods. You are so wise!")
        else:
            print("I did not understand, please try again...")
    elif red_do.lower() == "sell":
        print("Are you sure you wanna sell such powerful book?")
        sell_choice = str(input("Type YES or NO: "))
        if sell_choice.lower() == "yes":
            print("That is so sad. You could have learned many wonderful things...")
        elif sell_choice.lower() == "no":
            print(
                "Uff! This book is rare and precious to be sold. You made a good choice!"
            )
        else:
            print("I did not understand, please try again...")
    else:
        print("I did not understand, please try again...")
else:
    print("I did not understand, please try again...")
