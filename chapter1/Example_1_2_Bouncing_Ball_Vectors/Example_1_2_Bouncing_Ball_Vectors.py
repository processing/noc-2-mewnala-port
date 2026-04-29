# Example 1-2: Bouncing Ball, with PVector!
# Instead of a bunch of floats, we now just have two variables.

from mewnala import *
from mewnala.math import *

def setup():
    size(640, 360)

    global position, velocity
    # Note how the position & velocity has to be called inside of setup() as list.
    position = vec2(100, 100)
    velocity = vec2(2.5, 2)  
   
def draw():
    global position, velocity

    background(255)

    # Move the ball according to its speed.
    position += velocity

    # We still sometimes need to refer to the individual components of a PVector and can do so using the dot syntax: position.x, velocity.y, etc.
    if (position[0] > width or position[0] < 0):
      velocity[0] = velocity[0] * -1;
    if (position[1] > height or position[1] < 0):
      velocity[1] = velocity[1] * -1;

    stroke(0);
    fill(127);
    stroke_weight(2);
    circle(position[0], position[1], 48);

run()
