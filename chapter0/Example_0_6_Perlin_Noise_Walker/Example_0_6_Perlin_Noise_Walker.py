from mewnala import *

width = 640
height = 360

class Walker:
    def __init__(self):
        self.x = None
        self.y = None
        self.tx = 0
        self.ty = 10000
    
    def step(self):
        # x- and y-position mapped from noise
        self.x = map(noise(self.tx), 0, 1, 0, width) # TODO: noise not determined
        self.y = map(noise(self.ty), 0, 1, 0, height)

        # Move forward through time.
        self.tx += 0.01
        self.ty += 0.01
    
    def show(self):
        strokeWeight(2) # TODO: undefined
        fill(127)
        stroke(0)
        circle(self.x, self.y, 48)

walker = Walker()

def setup():
    size(width, height)
    background(255)

def draw():
    walker.step()
    walker.show()

run()
