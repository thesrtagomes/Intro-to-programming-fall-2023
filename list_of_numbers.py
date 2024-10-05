numbers = []
number = 1


print("Enter a list of numbers, type 0 when finished.")
while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)

sum = 0
for current_number in numbers:
    sum += current_number
average = sum / len(numbers)

ordered_numbers = sorted(numbers)
largest = ordered_numbers[-1]

smallest = largest
for current_number in numbers:
    if current_number > 0 and current_number < smallest:
        smallest = current_number

print(f"The sum is: {sum}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest positive number is {smallest}")

print("The sorted list is:")
for current_number in ordered_numbers:
    print(current_number)
