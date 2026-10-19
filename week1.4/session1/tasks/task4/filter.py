# Week 4, Session 1: 

# Your are given the function filter_positive_numbers with a docstring.
# Can you identify the inconsistency between the docstring and the implementation?

# Your task is to update the docstring to reflect what the function does.
numbers = [-1,0,10,-3,2]



def filter_positive_numbers(numbers):
    """
    Filters numbers greater than 0 from the list, keeping only the negative ones and 0.
    The function returns a list of all the number greater than 0 in the input.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        list of int: A list containing all the integers that are greater than 0.
    """
    return [num for num in numbers if num > 0]

print(filter_positive_numbers(numbers))