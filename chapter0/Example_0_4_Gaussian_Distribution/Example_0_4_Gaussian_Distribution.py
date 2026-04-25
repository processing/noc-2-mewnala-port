
from mewnala import *

width = 640
height = 360

def setup():
    size(width, height)
    background(255)

def draw():
    # A normal distribution with mean 320 and standard deviation 60
    x = random_gaussian() * 60 + 320 # TODO: random_gaussian not determined
    no_stroke()
    fill(0, 10)
    circle(x, 120, 16)
    
run()


