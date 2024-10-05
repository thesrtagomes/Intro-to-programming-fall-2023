people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10",
]

youngest = 0

for i, person in enumerate(people):
    name_and_age = person.split(" ")
    name = name_and_age[0]
    age = int(name_and_age[1])
    print(f"Name: {name}. Age: {age}")

    youngest_name_and_age = people[youngest].split(" ")
    youngest_age = int(youngest_name_and_age[1])
    if age < youngest_age:
        print(f"age {age}, youngest_age {youngest_age}")
        youngest = i

youngest_name_and_age = people[youngest].split(" ")
youngest_name = youngest_name_and_age[0]
youngest_age = int(youngest_name_and_age[1])
print(f"Youngest person: Name: {youngest_name}. Age: {youngest_age}")
