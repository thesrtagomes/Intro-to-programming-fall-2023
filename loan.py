loan = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))
can_loan = False
if loan >= 5:
    if credit_history >= 7 and income >= 7:
        can_loan = True
        print("Loan decision: Yes")
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            can_loan = True
            print("Loan decision: Yes")
        else:
            print("Loan decision: No")
    elif credit_history > 7 or income > 7:
        can_loan = False
        print("Loan decision: No")
else:
    if loan < 5:
        if credit_history < 4:
            can_loan = False
            print("Loan decision: No")
        elif income >= 7 or down_payment >= 7:
            can_loan = True
            print("Loan decision: Yes")
        elif income >= 4 and down_payment >= 4:
            can_loan = True
            print("Loan decision: Yes")
        else:
            can_loan = False
            print("Loan decision: No")
print(can_loan)
