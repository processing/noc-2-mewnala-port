from mewnala import * 
from Mover import *

def setup():
  size(640, 360)
  global mover
  mover = Mover()

def draw():
  background(255)
  mover.show()
  mover.update()
  mover.checkEdges()

run()

