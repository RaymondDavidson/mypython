import math

# input
length = (raw_input("what is the length: "))
width = (raw_input("what is the width: "))
if type(length) == int:
    condt1 = 0
    if type(width) == int:
        condt2 = 0
    else:
        print "width not valid"
        condt2 = 1
else:
    print "length not valid input"
    condt1 = 1
# calcs
if condt1 == condt2 == true:
    area = ((float(length))*(float(width)))
    paintraw = (float(area)/350)
    painttotal = (math.ceil(paintraw))
else:
    print "input not valid"
#check input type
