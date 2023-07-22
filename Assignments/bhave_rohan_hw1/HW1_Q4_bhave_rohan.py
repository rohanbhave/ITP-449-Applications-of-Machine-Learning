# Rohan Bhave
# ITP 449
# HW1
# Question 4

# input loan details
loan_amount = float(input("Loan Amount: "))
interest_rate = float(input("Annual Interest Rate: "))
years = float(input("Years: "))

# converted interest rate to per month
interest_per_month = interest_rate/100/12

# converting years to months
months = years*12

# calculating monthly payment
monthly_payment = (loan_amount*interest_per_month*(1 + interest_per_month)**months)/((1 + interest_per_month)**months - 1)

# printing output
print("your monthly payment is: $%.2f" % monthly_payment)

