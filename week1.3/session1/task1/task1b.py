# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
#This works as the list is set to be a boolean value of true while the list is not empty. When the list becomes empty the boolean becomes false so the while statement does not run indefinitely.
# What features of Python does it rely on?
#It relies that the python is true.