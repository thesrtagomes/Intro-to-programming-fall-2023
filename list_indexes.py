items = []
item = ""

print('Please enter the items of the shopping list (type "quit" to finish):')
while item != "quit":
    item = input("Item: ")
    if item != "quit":
        items.append(item)
print()

print("The shopping list is:")
for each_item in items:
    print(f"{each_item}")
print()

print("The shopping list with indexes is: ")
for i, each_item in enumerate(items):
    print(f"{i}. {each_item}")
print()

change_item = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")
items[change_item] = new_item

print("The shopping list with indexes is: ")
for i, each_item in enumerate(items):
    print(f"{i}. {each_item}")
print()
