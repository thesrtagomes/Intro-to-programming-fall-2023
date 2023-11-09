#Calculating age next year
age_int = input(('How old are you ?')) #Or age = int(input("How old are you? "))
age = int(age_int)
next_year = age + 1
print(f'On your next birthday, you will be {next_year}!')
print('')
#Calculating number of eggs
eggs_carton_str = input('How many egg catons do you have? ')
eggs_carton =int(eggs_carton_str)
eggs = eggs_carton * 12
print(f'You have {eggs} eggs.')
print('')
#calculating cookies
cookies_str = input('How many cookies do you have? ')
people_str = input('How many people are there? ')
cookies = int(cookies_str)
people = int(people_str)

cookies_per_person = cookies / people
print(f'Each person may have {cookies_per_person} cookies.')
