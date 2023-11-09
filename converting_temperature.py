#Converting Fahrenheit into Celsius
temperature = float(input('What is the temperature in Fahrenheit? '))
celsius = (temperature - 32) * 5/9 
print(f'The temperature is Celsius is {celsius:.1f} degrees.')

#Converting Celsius into Fahrenheit
temperature = float(input('What is the temperature in Celsius? '))
fahrenheit = (temperature * 9/5) + 32
print(f'The temperature in Fahrenheit is {fahrenheit:.1f} degrees.')