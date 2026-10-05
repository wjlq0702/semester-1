# Worksheet 1.2: Task 2 Solution 
from util import read_numbers
import sys 
numbers = read_numbers()
if numbers == []:
    sys.exit("Error: no numbers provided")
print("Minimum = ", min(numbers))
print("Maximum = ", max(numbers))
print("Mean = ", (sum(numbers)/len(numbers)))
if (len(numbers)%2) ==0:
    index = ((len(numbers)//2) - 1)
    numbers.sort() 
    value = (numbers[index] + numbers[index+1])/2
    print("Median = ", value)
else:
    numbers.sort()
    print("Median = ", numbers[(len(numbers)//2)] )

