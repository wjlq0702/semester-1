# Week 1.5, Session 2: Task 4
from geometry import Point, Circle
#Add a program here that demonstrates use of the __contains__()
p = Point(20,5)
c = Circle(15)

if p in c:
    print("The point is within the circle")
else: 
    print("Point is not within the circle")
# method that you implemented in the Circle class
