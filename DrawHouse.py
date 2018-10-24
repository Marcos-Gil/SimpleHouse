# By: Marcos Gil

from SimpleGraphics import *

# Requesting input for the X and Y co-ordinate which is used for the starting location of the house
x = int(input("x? "))
y = int(input("y? "))

# Creating the base of the house with half the length and width of the rectangle subtracted from X and Y
# to make it centered on the co-ordinates the user inputs
setFill("burlywood1")
rect(x-100, y-60, 200, 120)

# Creating both windows of the house and changing the colour inside the windows
setFill("deep sky blue")
rect(x-70, y-40, 40, 40)
line(x-70, y-20, x-30, y-20)
line(x-50, y-40, x-50, y)
setFill("deep sky blue")
rect(x+30, y-40, 40, 40)
line(x+69, y-20, x+30, y-20)
line(x+50, y-40, x+50, y)

# Creating the door for the house and making it Brown
setFill("chocolate4")
rect(x-25, y-20, 50, 80)

# Creating the door knob for the door and giving it a Gold color
setFill("goldenrod")
ellipse(x-18, y+15, 10,10)

# Creating the chimney of the house and giving it a Red colour
setFill("firebrick")
rect(x+35, y-130, 35, 60)

# Creating the roof of the house and giving it an Ivory colour
setFill("ivory4")
polygon(x-125, y-60, x+125, y-60, x, y-130, x-125, y-60)