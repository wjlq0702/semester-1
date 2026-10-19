# Week 4, Session 1: 

# Inspect the code, run the program and observe the output


def check_vote_eligibility(age):
    """
    Simple Voting Eligibility Checker
    This follows from week2, task_1/activity_1 in session 1
    """
    # Use an if statement to check if the user is 18 or over
    if (age >= 18):
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")


age = int(input("Enter your age: "))
check_vote_eligibility(age)

# what is the return value from check_vote_eligibility?
#The return value from check vot eligiibility is to decicde wether the person is old enough to vote or not.
#If the user is older than 18 the value being returned will include "You are eligiblie to vote"
#If the user is less than 17, the message that is returned will include You are not eligible to vote.