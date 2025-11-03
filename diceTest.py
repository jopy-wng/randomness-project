Web VPython 3.2
import random

numOfDice = int(input("How many dice would you like? (1–10): "))

numOfDice = max(1, min(numOfDice, 10))

dice_list = []

start_x = -2 * (numOfDice - 1) / 2
y = 0

for i in range(numOfDice):
    x = start_x + 2 * i
    d = box(pos = vector(x, y, 0), size = vector(1, 1, 1), color = color.white)
    dice_list.append(d)

spinTime = 0

while spinTime < 1.5:
    rate(60)
    spinTime += 0.02
    # enumerate() function in Python is a built-in function that adds a counter to an iterable (like a list, tuple, or string) and returns an enumerate object.
    for i, d in enumerate(dice_list):
        d.rotate(angle = 0.3, axis = vector(random.random(), random.random(), random.random()))

def randOr(dice):
    # random.uniform(a, b) ensures that any number between a and b is equally likely to be generated.
    dice.rotate(angle = random.uniform(0, 2 * pi), axis = vector(1, 0, 0))
    dice.rotate(angle = random.uniform(0, 2 * pi), axis = vector(0, 1, 0))
    dice.rotate(angle = random.uniform(0, 2 * pi), axis = vector(0, 0, 1))

for d in dice_list:
    randOr(d)

results = [random.randint(1, 6) for i in range(numOfDice)]
print(results)

