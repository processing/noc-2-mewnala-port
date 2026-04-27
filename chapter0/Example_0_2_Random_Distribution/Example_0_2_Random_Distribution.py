# An array to keep track of how often random numbers are picked

from mewnala import *
import random

randomCounts = None
total = 20

def setup():
    global randomCounts
    size(640, 360)
    randomCounts = [0] * total
    
def draw():
    background(255)
    index = random.randint(0, total - 1)
    randomCounts[index] += 1

    # Draw a rectangle to graph results
    stroke(0)
    stroke_weight(2)
    fill(127)
    w = width / len(randomCounts)

    for x in range(len(randomCounts)):
        rect(x * w, height - randomCounts[x], w - 1, randomCounts[x])

run()
