# Example 1-4: Vector multiplication

from mewnala import *
from mewnala.math import *

def setup():
    size(640, 360)
       
def draw():
    background(255)

    global mouse, center
     # Two vectors, one for the mouse position and one for the center of the window
    mouse = vec2(mouse_x, mouse_y)
    center = vec2(width / 2, height / 2)

    # Draw the original two vectors
    stroke_weight(2)
    stroke(200)
    line(0, 0, mouse[0], mouse[1])

   # Multiplying a vector!  The vector is now half its original size (multiplied by 0.5).
    mouse *= 0.5

    stroke(0)
    stroke_weight(4)
    line(0, 0, mouse[0], mouse[1])

run()
