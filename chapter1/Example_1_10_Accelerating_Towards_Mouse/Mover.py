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
        self.acceleration = vec2()
        self.topSpeed = 5

    def update(self):
        self.mouse = vec2(mouse_x, 2) #TODO cannot access mouse_x and mouse_y in class
        # RuntimeError: TypeError: must be real number, not builtin_function_or_method

        # Step 1: Compute direction
        self.dir = self.mouse - self.position

        # Step 2: Normalize
        mag = math.hypot(self.mouse[0], self.mouse[1])  # magnitude of mouse vector
        self.dir /= mag if mag != 0 else 1 # TODO arithmetic or mewnala fn for normalize()?? We can also implement it manually as dir /= mag, but we need to check if mag is not zero to avoid division by zero error. So it would be something like dir /= mag if mag != 0 else 0.

        # Step 3: Scale
        self.dir *= 0.2; # TODO arithmetic or mewnala fn for setMag()??
        mag = math.hypot(self.dir[0], self.dir[1])  # magnitude of self.dir
        # Steps 2 and 3 could be combined into:
        self.dir *= (0.2 / mag if mag != 0 else 0); # TODO arithmetic or mewnala fn for setMag()??

        # Step 4: Accelerate
        self.acceleration = self.dir;

        self.velocity += self.acceleration # TODO arithmetic or mewnala fn?
        
        # limit the velocity to the top speed
        # TODO ask if we can use math fn or we implement manually or we use mewnala fn? for magnitude and limit
        mag = math.hypot(self.velocity[0], self.velocity[1])  # magnitude of velocity
        if mag > self.topSpeed:
            self.velocity *= self.topSpeed / mag

        self.position += self.velocity # TODO arithmetic or mewnala fn?
    
    def show(self):
        stroke(0)
        stroke_weight(2)
        fill(127)
        circle(self.position[0], self.position[1], 48)
        
mover = Mover()