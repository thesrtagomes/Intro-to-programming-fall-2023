print('Please enter the following information:')
print('')

first_name = input(str('First name: '))
last_name = input(str('Last name: '))
email = input(str('Email address: '))
phone_number = input(str('Phone number: '))
job = input(str('Job title: '))
id = input(str('ID Number: '))
hair = input(str('Hair color: '))
eye = input(str('Eyes color: '))
month = input(str('Starting month: '))
training = input(str('Completed additional training? '))


print('The ID card is:')
print('-----------------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()} ')
print(job.title())
print(f'ID: {id}')
print('')
print(email)
print(phone_number)
print(f'Hair: {hair.capitalize():15} Eyes: {eye.capitalize()}')
print(f'Month: {month.capitalize():14} Training: {training.capitalize()}')
print('-----------------------------------------')