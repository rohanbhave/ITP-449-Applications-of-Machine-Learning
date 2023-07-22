# Rohan Bhave
# ITP 449
# HW2
# Question 3

# printing requirements
print("Please enter a password. Follow these requirements")
print("\ta.\tMust be at least 8 characters long")
print("\tb.\tMust contain both uppercase and lowercase letters")
print("\tc.\tMust contain at least one number between 0-9")
print("\td.\tMust contain a special character: !, @, #, $")

# while loop to get valid input
valid = False
while valid == False:
    # user input
    password = input("\t\tPassword: ")
    if len(password) >= 8:  # requirement a
        upper = False
        lower = False
        number = False
        special = False
        for x in password:
            if x.isupper():     # upper case letter
                upper = True
            if x.islower():     # lower case letter
                lower = True
            if x.isnumeric():   # number
                number = True
            if x in ["!", "@", "#", "$"]:   # special
                special = True

        if upper and lower and number and special:
            print("\t\tAccess Granted!")
            valid = True
        else:
            print("\t\tInvalid password. Try again!")


