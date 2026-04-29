# Example 1-1: Bouncing Ball, no vectors
# Variables for position and speed of ball.

from mewnala import *

x = 100
y = 100
xspeed = 2.5
yspeed = 2

def setup():
    size(640, 360)
    background(255)

def draw():
    global x, y, xspeed, yspeed

    background(255)

    # Move the ball according to its speed.
    x += xspeed
    y += yspeed

    # Check for bouncing.
    if (x > width or x < 0):
        xspeed = xspeed * -1
    if (y > height or y < 0):
        yspeed = yspeed * -1

    stroke(0)
    fill(127)
    stroke_weight(2)
    # Draw the ball at the position (x,y).
    circle(x, y, 48)

run()
