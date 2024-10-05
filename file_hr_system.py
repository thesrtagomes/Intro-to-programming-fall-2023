people = []

with open("hr_system.txt") as hr_system:
    for line in hr_system:
        person = line.strip().split(" ")
        people.append(person)

for person in people:
    name = person[0]
    id = person[1]
    title = person[2]
    salary = float(person[3]) / 24

    if title.lower() == "engineer":
        salary += 1000

    print(f"Name: {name} (ID: {id}), Title: {title} - ${salary:.2f}")
