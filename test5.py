from vpython import *
#Web VPython 3.2

#user inputs & making sure no invalid inputs
while True:
    inp_str = input("How many dice would you like? (1–10): ")
    try:
        inp = int(inp_str)
        if 1 <= inp <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid number. Using default 1 die.")
        inp = 1
        break
    except TypeError:
        print("Invalid input. Using default 1 die.")
        inp = 1
        break

#user chooses how many times to iterate
while True:
    itrinp = input("How many logistic iterations before rolling? (1–2000): ")
    try:
        iters = int(itrinp)
        if 1 <= iters <= 2000:
            break
        else:
            print("Please enter a number between 1 and 2000.")
    except ValueError:
        print("Invalid input. Please enter a valid number. Using default 50 iterations.")
        iters = 50
        break
    except TypeError:
        print("Invalid input. Using default 50 iterations.")
        iters = 50
        break

r = 4.0

#limit to minimize effect of tendency towards 0 and 1 0.25 to 0.74
x = 0.25 + 0.49 * random() 

def logistic_rand():
    """Advance logistic map and return its value."""
    global x
    x = r * x * (1 - x)
    return x

def chaotic_die():
    """Convert logistic output to an integer 1–6."""
    val = logistic_rand()
    return int(1 + val * 6) if val < 1 else 6

for _ in range(iters):
    logistic_rand()


numOfDice = max(1, min(inp, 10))
dice_list = []

start_x = -2 * (numOfDice - 1) / 2
y = 0

for i in range(numOfDice):
    x_pos = start_x + 2 * i
    d = box(pos=vector(x_pos, y, 0), size=vector(1, 1, 1), color=color.white)
    dice_list.append(d)

spinTime = 0
while spinTime < 1.5:
    rate(60)
    spinTime += 0.02
    for d in dice_list:
        d.rotate(angle=0.3,
                 axis=vector(logistic_rand(), logistic_rand(), logistic_rand()))

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
    
#ALSO NOTHING SHOULD PRINT IN CONSOLE IN FINAL CODE!!!!!!!!
# Calculate Mean Squared Error vs expected counts
expected = [len(results)/6] * 6  # Expected count per face
mse = sum((counter[i] - expected[i])**2 for i in range(6)) / 6
print("Mean Squared Error (MSE) vs ideal dice:", mse)
#ALSO NOTHING SHOULD PRINT IN CONSOLE IN FINAL CODE!!!!!!!!

gbar = graph(title="Dice Roll Frequencies (Logistic PRNG)",
             xtitle="Die Face", ytitle="Count")
bar_graph = gvbars(delta=1, color=color.red)

for i in range(6):
    if counter[i] > 0:
        bar_graph.plot(pos=(i+1, counter[i]))