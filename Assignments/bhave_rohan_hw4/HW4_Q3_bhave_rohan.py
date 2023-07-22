# Rohan Bhave
# ITP 449
# HW4
# Q3

# importing libraries
import matplotlib.pyplot as plt

# input loan details
loan_amount = float(input("Loan Amount: "))
interest_rate = float(input("Annual Interest Rate: "))
years = int(input("Years: "))

# converted interest rate to per month
interest_per_month = interest_rate/100/12

# converting years to months
months = int(years*12)

# calculating number of total payments
total_payments = years * 12

# calculating monthly payment
monthly_payment = (loan_amount*interest_per_month*(1 + interest_per_month)**months)/((1 + interest_per_month)**months - 1)

# printing output
print("your monthly payment is: $%.2f" % monthly_payment)

# making blank lists
month_list = []
balance_list = []
interest_list = []

# setting principal balance to loan amount
principal_balance = loan_amount

# looping through each month
for month in range(1, total_payments + 1):
    # calculating interest and principal balance
    monthly_interest = principal_balance * interest_per_month
    principal_balance = principal_balance + monthly_interest - monthly_payment

    # appending lists with monthly figures
    month_list.append(month)
    interest_list.append(monthly_interest)
    balance_list.append(principal_balance)


# plotting month vs. interest
plt.subplot(1, 2, 1)
plt.xlabel("Month")
plt.ylabel("Interest Paid")
plt.scatter(month_list, interest_list, s = 10)
plt.plot(month_list, interest_list)

# plotting month vs. balance
plt.subplot(1, 2, 2)
plt.xlabel("Month")
plt.ylabel("Loan Balance")
plt.scatter(month_list, balance_list, s = 10)
plt.plot(month_list, balance_list)

# showing both plots
plt.show()
