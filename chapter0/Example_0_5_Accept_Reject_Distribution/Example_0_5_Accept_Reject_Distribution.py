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

    # Pick a random number and increase the count
    index = int(acceptreject() * len(randomCounts))
    randomCounts[index] += 1

    # Draw a rectangle to graph results
    stroke(0)
    # strokeWeight(2) # TODO: undefined
    fill(127)

    w = width / len(randomCounts)

    for x in range(len(randomCounts)):
      rect(x * w, height - randomCounts[x], w - 1, randomCounts[x])

# // An algorithm for picking a random number based on monte carlo method
# // Here probability is determined by formula y = x
def acceptreject():
  # We do this “forever” until we find a qualifying random value.
  while True:
    # Pick a random value.
    r1 = random()
    # Assign a probability.
    probability = r1
    # Pick a second random value.
    r2 = random()

    # {!3} Does it qualify? If so, we're done!
    if (r2 < probability):
       return r1
    
run()
