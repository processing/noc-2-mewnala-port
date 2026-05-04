from mewnala import *
from mewnala.math import *
import math

width = 640
height = 360
# TODO ask if width and height from the main sketch file will be ported to the class or has to be defined in
class Mover:
    def __init__(self):
        self.position = vec2(width / 2, height / 2)
        self.velocity = vec2()
        self.acceleration = vec2(-0.001, 0.01)
        self.topSpeed = 10

    def update(self):
        self.velocity += self.acceleration #TODO ask if we can use arithmetic fn, or use mewnala fn
        
        # limit the velocity to the top speed
        # TODO ask if we can use math fn or we implement manually or we use mewnala fn? for magnitude and limit
        mag = math.hypot(self.velocity[0], self.velocity[1])  # magnitude of velocity
        if mag > self.topSpeed:
            self.velocity *= self.topSpeed / mag

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