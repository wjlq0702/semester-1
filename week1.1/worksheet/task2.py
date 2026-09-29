"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Nikhil Dhangar
"""
name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")
flag =True
# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
while flag:
    try:
        month = int(input("Enter Enter your monthly savings amount:"))
        flag = False
    except ValueError:
        print("Invalid Amount")
        break 
# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
if flag == False:
        year = month*12
        print(f"You will save £{year} every year")
# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
        interest = 1.008 * year
        rounded_interest = round(interest,2)
        print(f"With interest you will save, £{rounded_interest} a year")
