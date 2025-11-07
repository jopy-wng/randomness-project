Web VPython 3.2
import random


dice = compound([pyramid(axis = vector(0, 1, 0), pos = vector(0, -0.15, 0)),
    # 1 side
    sphere(radius = 0.1, pos = vector(0, 0.25, 0.28), color = color.black),
    # 2 side
    sphere(radius = 0.1, pos = vector(0.28, 0.25, 0.1), color = color.black),
    sphere(radius = 0.1, pos = vector(0.28, 0.25, -0.1), color = color.black),
    # 3 side
    sphere(radius = 0.1, pos = vector(-0.2, 0.4, 0), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.33, 0.13, 0.17), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.33, 0.13, -0.17), color = color.black),
    # 4 side
    sphere(radius = 0.1, pos = vector(0, 0.45, -0.18), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.2, 0, -0.38), color = color.black),
    sphere(radius = 0.1, pos = vector(0.2, 0, -0.38), color = color.black),
    sphere(radius = 0.1, pos = vector(0, 0.18, -0.29), color = color.black),
    
    # 5 side
    sphere(radius = 0.1, pos = vector(-0.2, -0.15, 0.2), color = color.black),
    sphere(radius = 0.1, pos = vector(-0.2, -0.15, -0.2), color = color.black),
    sphere(radius = 0.1, pos = vector(0.2, -0.15, 0.2), color = color.black),
    sphere(radius = 0.1, pos = vector(0.2, -0.15, -0.2), color = color.black),
    sphere(radius = 0.1, pos = vector(0, -0.15, 0), color = color.black)
])
  
spinTime = 0

while True:
    rate(60)
    spinTime = spinTime + 0.02
    dice.rotate(angle = 0.5, axis = vector(random.random(), random.random(), random.random()))