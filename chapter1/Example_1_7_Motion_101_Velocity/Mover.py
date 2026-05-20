from mewnala import *
from mewnala.math import *
from random import uniform as random

# width = 640
# height = 360
# TODO ask if width and height from the main sketch file will be ported to the class or has to be defined, as currently it seems unported
class Mover:
    def __init__(self):
        self.position = vec2(random(0, width), random(0, height))
        self.velocity = vec2(random(-2, 2), random(-2, 2))

    def update(self):
        self.position += self.velocity
    
    def show(self):
        stroke(0)
        stroke_weight(2)
        fill(127)
        circle(self.position[0], self.position[1], 48)

    def checkEdges(self):
        if self.position[0] > width:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = width

        if self.position[1] > height:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = height