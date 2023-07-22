# Rohan Bhave
# ITP 449
# HW1
# Question 1

# setting blank password variable
password = ""

# running loop until user enters something
while len(password) == 0:
    password = input("Enter your password: ")

# printing password length
print("Your password is", len(password), "characters long.")