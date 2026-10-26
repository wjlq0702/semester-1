# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x,y,x1,y1):
        self.x =x 
        self.y =y
        self.x1 = x1
        self.y1 = y1
    # Add distance() method here
    def distance(self):
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    def distance_to(self):
        return math.sqrt(((self.x1-self.x)**2)+((self.y1-self.y)**2))
        

    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
d1 = Point(1,3,4,5)
print(d1.distance_to())

