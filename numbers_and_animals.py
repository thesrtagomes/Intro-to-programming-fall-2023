first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))
print("")

if first_number > second_number:
    print("The first number is greater")
    print("The numbers are not equal")
    print("The second number is not greater")
elif first_number < second_number:
    print("The first number is not greater")
    print("The numbers are not equal")
    print("The second number is greater")
else:
    print("The first number is not greater")
    print("The numbers are equal")
    print("The second number is not greater")
print("")

favorite_animal = "fancy rat"
users_favorite_animal = str(input("What is your favorite animal?"))
if users_favorite_animal.lower() == favorite_animal.lower():
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
