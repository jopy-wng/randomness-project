Web VPython 3.2
import random

dice = compound([box(), 
    # 1 side
    sphere(radius = 0.1, pos = vector(0, 0.5, 0), color = color.black),
    # 2 side
    sphere(radius = 0.1, pos = vector(-0.2, 0.2, 0.5), color = color.black),
    sphere(radius = 0.1, pos = vector(0.15, -0.15, 0.5), color = color.black),
    # 3 side
    sphere(radius = 0.1, pos = vector(0.5, 0.23, 0.23), color = color.black),
    sphere(radius = 0.1, pos = vector(0.5, 0, 0), color = color.black),
    sphere(radius = 0.1, pos = vector(0.5, -0.23, -0.23), color = color.black),
    # 4 side
    sphere(radius = 0.1, pos = vector(-0.5, 0.2, -0.2), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.5, -0.2, 0.2), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.5, 0.2, 0.2), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.5, -0.2, -0.2), color = color.black),
    # 5 side
    sphere(radius = 0.1, pos = vector(0, 0, -0.5), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.2, 0.2, -0.5), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.2, -0.2, -0.5), color = color.black),
    sphere(radius = 0.1, pos = vector(0.2, 0.2, -0.5), color = color.black),
    sphere(radius = 0.1, pos = vector(0.2, -0.2, -0.5), color = color.black),
    # 6 side
    sphere(radius = 0.1, pos = vector(-0.15, -0.5, -0.2), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.15, -0.5, 0), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.15, -0.5, 0.2), color = color.black),
    sphere(radius = 0.1, pos = vector(0.15, -0.5, 0.2), color = color.black),
    sphere(radius = 0.1, pos = vector(0.15, -0.5, 0), color = color.black),
    sphere(radius = 0.1, pos = vector(0.15, -0.5, -0.2), color = color.black)])
    
spinTime = 0

while True:
    rate(60)
    spinTime = spinTime + 0.02
    dice.rotate(angle = 0.3, axis = vector(random.random(), random.random(), random.random()))