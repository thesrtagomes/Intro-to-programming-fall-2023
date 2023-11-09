print('Converting temperatures: Celsius or Fahrenheit!')
print('')
celsius_or_fahrenheit = str(input('Type down the temperature that you want to be converted: C for Celsius or F for Fahrenheit: '))

if celsius_or_fahrenheit == 'F' or celsius_or_fahrenheit == 'f':
    temperature = float(input('What is the temperature in Fahrenheit? '))
    celsius = (temperature - 32) * 5/9 
    print(f'The temperature is Celsius is {celsius:.1f} degrees.')

elif celsius_or_fahrenheit == 'C' or celsius_or_fahrenheit == 'c':
    temperature = float(input('What is the temperature in Celsius? '))
    fahrenheit = (temperature * 9/5) + 32
    print(f'The temperature in Fahrenheit is {fahrenheit:.1f} degrees.')
else:
    if celsius_or_fahrenheit.lower() not in ['c', 'f']:
        print('Error: try again.')
