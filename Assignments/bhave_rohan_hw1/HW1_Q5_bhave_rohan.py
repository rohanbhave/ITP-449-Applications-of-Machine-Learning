# Rohan Bhave
# ITP 449
# HW1
# Question 5

# user input
user_name = input("What is your name? ")

# splicing name forwards and backwards
name_forward = user_name.lower()[::1]
name_backwards = user_name.lower()[::-1]

# comparing forwards and backward names and printing output
if name_forward == name_backwards:
    print(user_name + ", your name is a palindrome!")
else:
    print(user_name + ", your name is not a palindrome!")


