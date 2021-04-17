balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(12):
    monthlyPayment = balance * monthlyPaymentRate
    balance -= monthlyPayment
    balance += (annualInterestRate/12.0) * balance
print('Remaining balance: ' + str(round(balance, 2)))