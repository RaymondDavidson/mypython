import math
import sys

# Challenge 1: Make sure input is an integer


# Challenge 1: Make sure input is an integer
# Challenge 100: Redo as a while loop
valid = int(1)
while valid != int(0):
    numvalid = int(1)
    shapevalid = int(1)
    shape = raw_input("Is the room rectangular or circular? ")
    if shape == "rectangular":
        numvalid = int(0)
        try:
            width = int(input("What is the width? "))
        except:
            numvalid= int(1)
            print("Value must be an integer.")
        try:
    	    length = int(input("What is the length? "))
        except:
            print("Value must be an integer.")
            numvalid= int(1)
    elif shape == "circular":
        numvalid = int(0)
        try:
            radius = int(input("what is the radius of the room? "))
        except:
            print("value must be an integer.")
            numvalid= int(1)
    elif shape != "rectangular":
        if shape != "circular":
            print "shape not valid"
            shapevalid = int(1)
        else:
            shapevalid = int(0)
    valid= (int(numvalid) + int(shapevalid))
def rectangle(length, width):
    area_of_ceiling = float(length * width)
    # Constraint 1: USE A CONSTANT to hold the Conversion Rate
    PAINT_NEEDED_RECTANGLE = float(area_of_ceiling / 350)
    # Constraint 2: Ensure that you round up to the next whole number
    paint_rounded_rectangle = int(math.ceil(PAINT_NEEDED_RECTANGLE))
def circle(radius):
    area_of_circle = float(3.14159*radius*radius)
    PAINT_NEEDED_CIRCLE = float(area_of_circle/350)
    paint_rounded_circle = int(math.ceil(PAINT_NEEDED_CIRCLE))
# rectangle print
if shape == "rectangular":
    if valid == 0:
        rectangle(length, width)
        print("You will need to purchase {} gallons of paint to cover {} square feet.".format(paint_rounded_rectangle, area_of_ceiling))
elif shape == "circular":
    if valid == 0:
        circle(radius)
    print("You will need to purchase {} gallons of paint to cover {} square feet.".format(paint_rounded_circle, area_of_circle))
