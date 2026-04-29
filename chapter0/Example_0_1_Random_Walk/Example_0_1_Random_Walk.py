from mewnala import *
import random

class Walker:
    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def show(self):
        stroke(0)
        point(self.x, self.y)
    
    def step(self):
        choice = random.randint(0, 3)
        if (choice == 0):
            self.x += 1
        elif (choice == 1):
            self.x -= 1
        elif (choice == 2):
            self.y += 1
        else:            
            self.y -= 1
        
def setup():
    size(640, 360)
    background(255)
    global walker
    walker = Walker()

def draw():
    walker.step()
    walker.show()

run()
