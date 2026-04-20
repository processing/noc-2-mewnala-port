
from mewnala import *
from math import floor
from random import random

width = 640
height = 360

class Walker:
    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def show(self):
        stroke(0)
        point(self.x, self.y)
    
    def step(self):
        r = random()
        # A 40% of moving to the right!
        if (r < 0.4):
            self.x += 1
        elif (r < 0.6):
            self.x -= 1
        elif (r < 0.8):
            self.y += 1
        else:            
            self.y -= 1

        self.x = max(0, min(self.x, width - 1))
        self.y = max(0, min(self.y, height - 1))

# Creating the Walker object!
walker = Walker()

def setup():
    size(width, height)
    background(255)

def draw():
    walker.step()
    walker.show()


            
run()


