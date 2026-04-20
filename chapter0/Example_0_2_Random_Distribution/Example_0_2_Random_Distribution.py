# An array to keep track of how often random numbers are picked

from mewnala import *
from math import floor
from random import random

randomCounts = None
total = 20

width = 640
height = 360

def setup():
    global randomCounts
    size(640, 360)
    randomCounts = [0] * total
    
def draw():
    background(255)
    index = floor(random() * total)
    randomCounts[index] += 1

    # Draw a rectangle to graph results
    stroke(0)
    # strokeWeight(2) # TODO: undefined
    fill(127)
    w = width / len(randomCounts)

    for x in range(len(randomCounts)):
        rect(x * w, height - randomCounts[x], w - 1, randomCounts[x])

run()
