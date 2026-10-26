# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x,y):
        self.x =x 
        self.y =y
        
    # Add distance() method here
    def distance(self):
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    def distance_to(self, x1 , y1):
        self.x1 = x1
        self.y1 = y1
        return math.sqrt(((self.x1-self.x)**2)+((self.y1-self.y)**2))

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

class Circle:
    
    """
        This class aims to find areas and perimeters using a 
        given point of the centre or radius
    """
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return math.pi * (2*self.radius)


# Don't add any testing code to this file!
