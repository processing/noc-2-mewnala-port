from mewnala import *
import random

class Walker:
    def __init__(self):
        self.x = None
        self.y = None
        self.tx = 0
        self.ty = 10000
    
    def step(self):
        # x- and y-position mapped from noise
        self.x = map([random.gauss(self.tx)], 0, 1, 0, width) # TODO: map is still pending to issue #131
        self.y = map([random.gauss(self.ty)], 0, 1, 0, height)

        # Move forward through time.
        self.tx += 0.01
        self.ty += 0.01
    
    def show(self):
        stroke_weight(2) # TODO: undefined
        fill(127)
        stroke(0)
        circle(self.x, self.y, 48)
 
walker = Walker()

def setup():
    size(640, 360)
    background(255)
    print(map)

def draw():
    walker.step()
    walker.show()

run()
