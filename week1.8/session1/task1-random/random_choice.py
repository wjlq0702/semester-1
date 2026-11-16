import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]
    names = list(set(names))

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
number = int(input("Enter a nummber of how many users you want:"))
number_of_names = random.sample(names, k=number)
# Display the chosen names, one per line
print(number_of_names)
