names = []
name = ""

while name != "end":
    name = input("Type the name of a friend: ")
    if name != "end": 
        names.append(name)
print()
print('Your friends are: ')
for name in names:
    print(name)