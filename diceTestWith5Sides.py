Web VPython 3.2
import random

scene = canvas(width = 600, height = 400)
scene.userzoom = False

menu(choices = ['5 sides', '6 sides'], bind = numOfSides)
inp = int(input("How many dice would you like? (1–10): "))
cutInp = input("Cut? Enter y/n")

numOfDice = 0

if inp > 10:
    numOfDice = 10
else:
    numOfDice = inp

numOfDice = max(1, min(numOfDice, 10))

dice_list = []

start_x = -2 * (numOfDice - 1) / 2
y = 0

def numOfSides(sides) :
    if sides == 5: (print("hi"))
    else if sides == 6: (print("hello"))

for i in range(numOfDice):
    x = start_x + 2 * i
    d = compound([pyramid(axis = vector(0, 1, 0), pos = vector(0, -0.15, 0)),
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
    d.pos = vector(x, y, 0)
    dice_list.append(d)

axes = [vector(random.uniform(-1, 1),
               random.uniform(-1, 1),
               random.uniform(-1, 1)).norm() for _ in range(numOfDice)]

spinTime = 0

while spinTime < 1.5:
    rate(60)
    spinTime += 0.02
    # enumerate() in Python is a built-in function that adds a counter to an iterable (like a list, tuple, or string) and returns an enumerate object.
    for i, d in enumerate(dice_list):
        d.rotate(angle = 0.3, axis = axes[i])

def randOr(d):
    # random.uniform(a, b) ensures that any number between a and b is equally likely to be generated.
    d.rotate(angle = random.uniform(0, 2 * pi), axis = vector(1, 0, 0))
    d.rotate(angle = random.uniform(0, 2 * pi), axis = vector(0, 1, 0))
    d.rotate(angle = random.uniform(0, 2 * pi), axis = vector(0, 0, 1))

for d in dice_list:
    randOr(d)

results = [random.randint(1, 5) for i in range(inp)]
print(results)

counterOne = 1
counterTwo = 1
counterThree = 1
counterFour = 1
counterFive = 1
counterSix = 1

gbar = graph(title = "Dice Roll Frequencies", xtitle = "Possible Sides", ytitle = "Times Rolled")
bar_graph = gvbars(delta = 1, color = color.red)
for i in range(len(results)):
    if results[i] == 1: bar_graph.plot(pos = (1, counterOne)); counterOne += 1
    if results[i] == 2: bar_graph.plot(pos = (2, counterTwo)); counterTwo += 1
    if results[i] == 3: bar_graph.plot(pos = (3, counterThree)); counterThree += 1
    if results[i] == 4: bar_graph.plot(pos = (4, counterFour)); counterFour += 1
    if results[i] == 5: bar_graph.plot(pos = (5, counterFive)); counterFive += 1
    if results[i] == 6: bar_graph.plot(pos = (6, counterSix)); counterSix += 1
