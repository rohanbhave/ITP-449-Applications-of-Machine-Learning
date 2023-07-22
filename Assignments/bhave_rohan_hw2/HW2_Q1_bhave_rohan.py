# Rohan Bhave
# ITP 449
# HW2
# Question 1


total = 100 # target value in cents

# for loop for each denomination
for quarters in range(4+1):
    for dimes in range(10+1):
        for nickels in range(20+1):
            for pennies in range(100+1):
                # checking for total value
                if quarters*25 + dimes*10 + nickels*5 + pennies*1 == total:
                    print(quarters, "quarters,", dimes, "dimes,", nickels, "nickels,", pennies, "pennies")
