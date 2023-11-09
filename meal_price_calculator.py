childs_meal = float(input("What is the price of a child's meal? "))
adults_meal = float(input("What is the price of an adult's meal? "))
number_children = int(input('How many children are there? '))
number_adults = int(input('How many adults are there? '))  
print('')

subtotal = float(adults_meal * number_adults) + (childs_meal * number_children)
print(f'Subtotal: ${subtotal:.2f}')
print('')

tax_rate = float(input('What is the sales tax rate? '))
tax_rate_number = tax_rate / 100
sales_tax = tax_rate_number * subtotal
print(f'Sales Tax: ${sales_tax:.2f}')
total = subtotal + sales_tax
print(f'Total: ${total:.2f}')
print('')

#challenge
donate = str(input('Would you like to donate an amount for charity? (Y for yes or N for no)'))
if donate == 'Y':
    amount = float(input('How much would you like to contribute? '))
    new_total = total + amount
    print(f'The new Total is: ${new_total:.2f}')
    print('')
    payment_amount = float(input('What is the payment amount? '))
    change = payment_amount - new_total
    print(f'Change: ${change:.2f}')
    print('')
elif donate == "N":
    payment_amount = float(input('What is the payment amount? '))
    change = payment_amount - total
    print(f'Change: ${change:.2f}')
    print('')
else:
    print('Error. Try again')
    


