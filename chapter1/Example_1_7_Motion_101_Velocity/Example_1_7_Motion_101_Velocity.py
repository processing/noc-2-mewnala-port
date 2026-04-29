from mewnala import *
from Mover import *

def setup():
    size(640, 360)
    global mover
    mover = Mover()
       
def draw():
    background(255)
    mover.update()
    mover.checkEdges()
    mover.show()

run()