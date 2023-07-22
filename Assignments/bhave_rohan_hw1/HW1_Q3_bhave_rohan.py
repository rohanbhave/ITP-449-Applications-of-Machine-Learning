# Rohan Bhave
# ITP 449
# HW1
# Question 3

# setting blank variable
month_num = ""

# loop input statement until valid user input
while month_num not in range(1,13):
    month_num = int(input("Enter the month number: "))

# list with months and days in order
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# splicing month and days from lists
month_name = month_list[month_num - 1]
month_day = day_list[month_num - 1]

# print output
print(month_name, "has", int(month_day), "days")
