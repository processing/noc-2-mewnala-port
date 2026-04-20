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
        choice = floor(int(random() * 4))
        if (choice == 0):
            self.x += 1
        elif (choice == 1):
            self.x -= 1
        elif (choice == 2):
            self.y += 1
        else:            
            self.y -= 1
        
walker = Walker()

def setup():
    size(width, height)
    background(255)

def draw():
    walker.step()
    walker.show()

run()
