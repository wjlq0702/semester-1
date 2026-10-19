
# function implementation
height = int(input("Enter the height:"))
width = int(input("Enter the width:"))

def rectangle_area( x,y): # define suitable input data
    """returns the height and width of a rectangle given two inputs"""
    area = height*width              # implement the function
    return area        # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(height,width)}")   # provide suitable data matching your inputs
