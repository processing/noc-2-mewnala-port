
from mewnala import *
import random

width = 640
height = 360

def setup():
    size(width, height)
    background(255)

def draw():
    # A normal distribution with mean 320 and standard deviation 60
    x = random.gauss(320, 60)
    no_stroke()
    fill(0, 10)
    circle(x, 120, 16)
    
run()


