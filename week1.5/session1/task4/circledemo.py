# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

from geometry import Point
from geometry import Circle

point= Point(1.5,2.5)
c = Circle(15,point)

print(c.area())
print(c.perimeter())
if point in c:
    print("Point is within circle")
# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
