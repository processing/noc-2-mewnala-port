
from mewnala import *
import random

def setup():
    size(640, 360)
    background(255)

def draw():
    # A normal distribution with mean 320 and standard deviation 60
    x = random.gauss(320, 60)
    no_stroke()
    fill(0, 10)
    circle(x, 120, 16)
    
run()


