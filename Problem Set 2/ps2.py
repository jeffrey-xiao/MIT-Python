# Name: Jeffrey Xiao
import math
""" Given the outstanding balance on the credit card, the annual interest rate of the debt and the monthly payment rate:
    Calculate the balance of the credit card after one year if the person only pays the minimum monthly payment each month
"""

balance = int(input())
annualInterestRate = float(input())/12
monthlyPaymentRate = float(input())
total = 0.0
for i in range(1, 13) :
    print "Month:", i
    paid = balance*monthlyPaymentRate
    print "Minimum monthly payment: %.2f" %(paid)
    total += paid
    balance = max(balance - paid, 0)
    balance += balance * annualInterestRate
    print "Remaining balance: %.2f" %(balance)
print "Total paid: %.2f" %(total)
print "Remaining balance: %.2f" %(balance)

""" Given the outstanding balance on the credit card, and the annual interest rate of the debt
    Find the lowest monthly payment to pay off the debt in 12 months
    Let x = balance, y is monthly payment, and z is the monthly interest rate
    (((x-y)*(1+z)-y)*(1+z)-y)*...)
    = x*(1+z)^12 - y*(1+z)^12 - y*(1+z)^11 - ... - y*(1+z)^1
    = x*(1+z)^12 - yz*(1 - z^12)/(1-z)
    y = x*(1+z)^12 / z*(1 - z^12)/(1-z)
"""

balance = int(input())
annualInterestRate = 1+ float(input())/12

# Using annuities to compute answer: Runs in O(1) time
ans = balance*math.pow(annualInterestRate, 12) / (annualInterestRate * (1 - math.pow(annualInterestRate, 12))/(1 - annualInterestRate))
ans = int(math.ceil(ans/10)*10)
print "Lowest Payment: %d" %(ans)


# Bisection Search: Runs in log (balance) time
def getRemaining (b, rate, pay) :
    for i in range(12) :
        b = max(0, b - pay)
        b *= rate
    return b == 0
lo = 0.0
hi = float(balance)
while hi-lo > 0.00001 :
    mid = lo + (hi - lo) / 2.0
    if getRemaining (balance, annualInterestRate, mid) :
        hi = mid
    else :
        lo = mid
print "Lowest Payment: %.2f" %(lo)