Web VPython 3.2
import random

inpD = int(input("How many dice would you like? (1–10): "))
inpS = int(input("How many sides for each die? (4, 6): "))

numOfDice = 0

if inpD > 10:
    numOfDice = 10
else:
    numOfDice = inpD

numOfDice = max(1, min(numOfDice, 10))

dice_list = []

start_x = -2 * (numOfDice - 1) / 2
y = 0

for i in range(numOfDice):
    x = start_x + 2 * i
    if inpS == 4:
        d = pyramid(pos = vector(x, y, 0), size = vector(1, 1, 1), color = color.white)
    else if inpS == 6:
        d = box(pos = vector(x, y, 0), size = vector(1, 1, 1), color = color.white)
    else:
        print("Error: Only enter 4 or 6")
    dice_list.append(d)

spinTime = 0

while spinTime < 1.5:
    rate(60)
    spinTime += 0.02
    # enumerate() in Python is a built-in function that adds a counter to an iterable (like a list, tuple, or string) and returns an enumerate object.
    for i, d in enumerate(dice_list):
        d.rotate(angle = 0.3, axis = vector(random.random(), random.random(), random.random()))

def randOr(dice):
    # random.uniform(a, b) ensures that any number between a and b is equally likely to be generated.
    dice.rotate(angle = random.uniform(0, 2 * pi), axis = vector(1, 0, 0))
    dice.rotate(angle = random.uniform(0, 2 * pi), axis = vector(0, 1, 0))
    dice.rotate(angle = random.uniform(0, 2 * pi), axis = vector(0, 0, 1))

for d in dice_list:
    randOr(d)

results = [random.randint(1, 6) for i in range(inpD)]
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
    if results[i] == 1: bar_graph.plot(pos = (1, counterOne)) counterOne += 1
    if results[i] == 2: bar_graph.plot(pos = (2, counterTwo)) counterTwo += 1
    if results[i] == 3: bar_graph.plot(pos = (3, counterThree)) counterThree += 1
    if results[i] == 4: bar_graph.plot(pos = (4, counterFour)) counterFour += 1
    if results[i] == 5: bar_graph.plot(pos = (5, counterFive)) counterFive += 1
    if results[i] == 6: bar_graph.plot(pos = (6, counterSix)) counterSix += 1
