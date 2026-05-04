# Example 1-5: Vector magnitude

from mewnala import *
from mewnala.math import *
import math

def setup():
    size(640, 360)
       
def draw():
    background(255)

    global mouse, center
    mouse = vec2(mouse_x, mouse_y)
    center = vec2(width / 2, height / 2)
    mouse -= center

    # The magnitude (i.e. length) of a vector can be accessed via the mag() function.  Here it is used as the width of a rectangle drawn at the top of the window.
    # m = mouse.mag() 
    #TODO mag is not defined, do we use std python math library or arithmetic logic?
    m = math.hypot(mouse[0], mouse[1])
    fill(0)
    rect(10, 10, m, 10)

    translate(width / 2, height / 2)
    line(0, 0, mouse[0], mouse[1])

run()
