from vpython import *
#Web VPython 3.2

inp_str = input("How many dice would you like? (1–10): ")
if inp_str is None or inp_str.strip() == '':
    inp = 1
else:
    try:
        inp = int(inp_str)
    except ValueError:
        inp = 1 

X0_str = input("Random Seed (between 0 and 1): ")
if X0_str is None or X0_str.strip() == '':
    X0 = 0.5  # default seed
else:
    try:
        X0 = float(X0_str)
    except ValueError:
        X0 = 0.5
r = 4.0
N = inp

numOfDice = max(1, min(inp, 10))

dice_list = []

start_x = -2 * (numOfDice - 1) / 2
y = 0

for i in range(numOfDice):
    x = start_x + 2 * i
    d = box(pos=vector(x, y, 0), size=vector(1, 1, 1), color=color.white)
    dice_list.append(d)

x = X0

def logistic_rand():
    global x
    x = r * x * (1 - x)
    return x

def chaotic_die():
    val = logistic_rand()
    return int(1 + val * 6) if val < 1 else 6

spinTime = 0

while spinTime < 1.5:
    rate(60)
    spinTime += 0.02
    for i, d in enumerate(dice_list):
        d.rotate(angle=0.3, axis=vector(logistic_rand(), logistic_rand(), logistic_rand()))

results = []
for d in dice_list:
    d.rotate(angle=2*pi*logistic_rand(), axis=vector(1, 0, 0))
    d.rotate(angle=2*pi*logistic_rand(), axis=vector(0, 1, 0))
    d.rotate(angle=2*pi*logistic_rand(), axis=vector(0, 0, 1))
    results.append(chaotic_die())

print(results)

counter = [0, 0, 0, 0, 0, 0]

for r in results:
    counter[r-1] += 1

gbar = graph(title="Dice Roll Frequencies (Logistic PRNG)",
             xtitle="Die Face", ytitle="Count")
bar_graph = gvbars(delta=1, color=color.red)

for i in range(6):
    if counter[i] > 0:
        bar_graph.plot(pos=(i+1, counter[i]))