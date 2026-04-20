
from mewnala import *
from math import floor
from random import random

width = 640
height = 360

def setup():
    size(width, height)
    background(255)

def draw():
    # A normal distribution with mean 320 and standard deviation 60
    x = randomGaussian() * 60 + 320 # TODO: randomGaussian not determined
    noStroke()
    fill(0, 10)
    circle(x, 120, 16)
    
run()


