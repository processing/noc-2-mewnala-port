# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Demonstration of the basics of motion with vector.
# A "Mover" object stores position, velocity, and acceleration as vectors
# The motion is controlled by affecting the acceleration (in this case towards the mouse)

from mewnala import *
from Mover import *

def setup(): 
  size(640, 360)
  global mover
  mover = Mover()


def draw():
  background(255)

  mover.update()
  mover.show()

run()