dataset = []

with open("life-expectancy.csv") as life_expectancy:
    for i, line in enumerate(life_expectancy):
        if i > 0:
            data = line.strip().split(",")
            dataset.append(data)

year = int(input("Enter the year of interest: "))

data_in_year = []
for data in dataset:
    data_year = int(data[2])
    if data_year == year:
        data_in_year.append(data)

overall_max = 0
overall_min = 0

for i, data in enumerate(dataset):
    expectancy = float(data[3])
    min_expectancy = float(dataset[overall_min][3])
    max_expectancy = float(dataset[overall_max][3])
    if expectancy < min_expectancy:
        overall_min = i
    if expectancy > max_expectancy:
        overall_max = i

overall_max_expectancy = float(dataset[overall_max][3])
overall_max_country = dataset[overall_max][0]
overall_max_year = dataset[overall_max][2]

overall_min_expectancy = float(dataset[overall_min][3])
overall_min_country = dataset[overall_min][0]
overall_min_year = dataset[overall_min][2]

print(
    f"The overall max life expectancy is: {overall_max_expectancy} from {overall_max_country} in {overall_max_year}"
)
print(
    f"The overall min life expectancy is: {overall_min_expectancy} from {overall_min_country} in {overall_min_year}"
)

max = 0
min = 0
average = 0

for i, data in enumerate(data_in_year):
    expectancy = float(data[3])
    average += expectancy
    min_expectancy = float(data_in_year[min][3])
    max_expectancy = float(data_in_year[max][3])
    if expectancy < min_expectancy:
        min = i
    if expectancy > max_expectancy:
        max = i
average = average / len(data_in_year)

max_expectancy = float(data_in_year[max][3])
max_country = data_in_year[max][0]

min_expectancy = float(data_in_year[min][3])
min_country = data_in_year[min][0]


print(f'For the year {year}:')
print(f'The average life expectancy across all countries was {average:.2f}')
print(f'The max life expectancy was in {max_country} with {max_expectancy}') 
print(f'The min life expectancy was in {min_country} with {min_expectancy}')

