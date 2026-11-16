import random

# Get user to input how many random numbers they want
number = int(input("How many random numbers do you want to generate:"))

# Generate this many random numbers
for x in range(number):
# Write the random numbers to a file named random.txt, one number per line
    with open("random.txt","a") as text:
        text.write(f"{(random.randint(0,1000))}\n")

