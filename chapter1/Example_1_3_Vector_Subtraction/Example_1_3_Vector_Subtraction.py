# Example 1-3: Vector subtraction

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
    stroke_weight(4);
    stroke(200);
    line(0, 0, mouse[0], mouse[1]);
    line(0, 0, center[0], center[1]);

    # Vector subtraction!
    mouse -= center

    # Draw a line to represent the result of subtraction.
    # Notice how I move the origin with translate() to place the vector
    stroke(0)
    fill(127)
    translate(width / 2, height / 2)
    line(0, 0, mouse[0], mouse[1])

run()
