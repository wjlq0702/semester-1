# Worksheet 1.2: Task 2 Solution 
from util import read_numbers
import sys 
numbers = read_numbers()
if numbers == []:
    sys.exit("Error: no numbers provided")

print(f"Minimum = {min(numbers)}")
print(f"Maximum = {max(numbers)}")
print(f"Mean = {(sum(numbers)/len(numbers))}")
if (len(numbers)%2) ==0:
    index = ((len(numbers)//2) - 1)
    numbers.sort() 
    value = (numbers[index] + numbers[index+1])/2
    print(f"Median = {value}")
else:
    numbers.sort()
    print(f"Median = {numbers[(len(numbers)//2)]}" )

