def to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def to_celsius(fahrenheit):
    return (fahrenheit -32) / 1.8

def calculate_windchill(temperature, unit, speed):
    if unit == "C":
        temperature = to_fahrenheit(temperature)

    windchill = 35.74 + 0.6215 * temperature - 35.75 * speed ** 0.16 + 0.4275 * temperature * speed ** 0.16

    if unit == "C":
        return to_celsius(windchill)
    else:
        return windchill
temperature = float(input("What is the temperature?"))
unit = ""

while unit != "C" and unit != "F":
    unit = input('Fahrenheit or Celsius (F/C)?').upper()

for speed in range(5, 61, 5):
    windchill = calculate_windchill(temperature, unit, speed)
    print(f"At temperature {temperature:.2f} {unit}, and wind speed {speed} mph, the windchill is {windchill:.2f} {unit}")