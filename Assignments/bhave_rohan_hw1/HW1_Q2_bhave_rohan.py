# Rohan Bhave
# ITP 449
# HW1
# Question 2

# setting name variable as blank
name = ""

# while loop to make sure user enters something
while len(name) == 0:
    name = input("What is your name? ")
    name_no_space = name.replace(" ", "")

# output statement
print(name, "your name has", len(name_no_space), "characters.")

