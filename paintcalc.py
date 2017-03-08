import math
import sys
shape = raw_input("Is the room rectangular or circular? ")
# Challenge 1: Make sure input is an integer


# Challenge 1: Make sure input is an integer
# Challenge 100: Redo as a while loop
if shape == "rectangular":
    try:
        width = int(input("What is the width? "))
    except:
	       print("Value must be an integer.")
	       sys.exit(1)
    try:
    	length = int(input("What is the length? "))
    except:
        print("Value must be an integer.")
        sys.exit(1)
elif shape == "circular":
        try:
            radius = int(input("what is the radius of the room? "))
        except:
            print("value must be an integer.")
            sys.exit(1)

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

if shape == "rectangular":
    rectangle(length, width)
    print("You will need to purchase {} gallons of paint to cover {} square feet.".format(paint_rounded_rectangle, area_of_ceiling))
elif shape == "circular":
    circle(radius)
    print("You will need to purchase {} gallons of paint to cover {} square feet.".format(paint_rounded_circle, area_of_circle))
else:
    print("shape not valid")
    sys.exit(1)
