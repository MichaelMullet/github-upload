balance = 3926
annualInterestRate = 0.2
monthlyPayment = 10
newBalance = balance
while True:
    for month in range(12):
        newBalance -= monthlyPayment
        newBalance += (annualInterestRate/12.0) * newBalance
    if month == 11 and newBalance > 0:
        monthlyPayment += 10
        month = 0
        newBalance = balance
    elif newBalance <= 0:
        break
print('Lowest Payment: ' + str(monthlyPayment))