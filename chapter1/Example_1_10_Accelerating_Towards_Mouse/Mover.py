from mewnala import *
from mewnala.math import *

width = 640
height = 360
# TODO ask if width and height from the main sketch file will be ported to the class or has to be defined in
class Mover:
    def __init__(self):
        self.position = vec2(width / 2, height / 2)
        self.velocity = vec2()
        self.acceleration = vec2()
        self.topSpeed = 5

    def update(self):
        mouse = vec2(mouse_x, mouse_y)

        # Step 1: Compute direction
        dir = mouse - self.position

        # Step 2: Normalize
        dir.normalize()

        # Step 3: Scale
        dir *= 0.2
        
        # Steps 2 and 3 could be combined into:
        dir.setMag(0.2)

        # Step 4: Accelerate
        self.acceleration = dir;

        self.velocity += self.acceleration
        self.velocity.limit(self.topSpeed)
        self.position += self.velocity
    
    def show(self):
        stroke(0)
        stroke_weight(2)
        fill(127)
        circle(self.position[0], self.position[1], 48)