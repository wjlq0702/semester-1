# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        """
        Checks if values are squares. If height is not equal to the width then will return False or else will return True. 
        """
        if self.width == self.height:
            return True
        else:
            return False
    def area(self):
        """
        Returns the area for the given height and width by multiplying them together
        """
        return self.width*self.height
    def perimeter(self):
        """
        Returns the outside length of the rectangle or square given the widths and heights.
        """
        return (2*self.width) + (2*self.height) 
    # (See README.md for details of what they should do)
