# Demonstration of normalizing a vector.
# Normalizing a vector sets its length to 1.

from mewnala import *
from mewnala.math import *
import math

def setup():
    size(640, 360)
       
def draw():
    background(255)

    global mouse, center

    # A vector that points to the mouse position
    mouse = vec2(mouse_x, mouse_y)
    # A vector that points to the center of the window
    center = vec2(width / 2, height / 2)
    # Subtract center from mouse which results in a vector that points from center to mouse
    mouse -= center
   

    translate(width / 2, height / 2)
    stroke(200)
    stroke_weight(2)
    line(0, 0, mouse[0], mouse[1])

    # Normalize the vector
    mouse.normalize()

    # Multiply its length by 50
    mouse *= 50

    # Draw the resulting vector
    stroke(0)
    stroke_weight(8)
    line(0, 0, mouse[0], mouse[1])

run()