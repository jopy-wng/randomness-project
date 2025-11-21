Web VPython 3.2

while True:
    inp_str = input("How many dice would you like? (1–1000000): ")
    try:
        inp = int(inp_str)
        if 1 <= inp <= 1000000:
            break
        else:
            inp = 10
            break
    except:
        inp = 10
        break

while True:
    itrinp = input("How many logistic iterations before rolling? (1–2000): ")
    try:
        iters = int(itrinp)
        if 1 <= iters <= 2000:
            break
        else:
            iters = 1000
            break
    except:
        iters = 1000
        break

r = 4.0
x = random()

def logistic_rand():
    global x
    while True:
        x = r * x * (1 - x)
        if 0.055 <= x <= 0.955:
            return x

def chaotic_die():
    val = logistic_rand()
    return int(1 + val * 6) if val < 1 else 6

for _ in range(iters):
    logistic_rand()

numOfDiceAnimate = min(inp, 10)
numOfDice = inp
dice_list = []
start_x = -2 * (numOfDiceAnimate - 1) / 2
y = 0

def make_die(posx):
    d = compound([
        box(),
        sphere(radius=0.1, pos=vector(0, 0.5, 0), color=color.black),
        sphere(radius=0.1, pos=vector(-0.2, 0.2, 0.5), color=color.black),
        sphere(radius=0.1, pos=vector(0.15, -0.15, 0.5), color=color.black),
        sphere(radius=0.1, pos=vector(0.5, 0.23, 0.23), color=color.black),
        sphere(radius=0.1, pos=vector(0.5, 0, 0), color=color.black),
        sphere(radius=0.1, pos=vector(0.5, -0.23, -0.23), color=color.black),
        sphere(radius=0.1, pos=vector(-0.5, 0.2, -0.2), color=color.black),
        sphere(radius=0.1, pos=vector(-0.5, -0.2, 0.2), color=color.black),
        sphere(radius=0.1, pos=vector(-0.5, 0.2, 0.2), color=color.black),
        sphere(radius=0.1, pos=vector(-0.5, -0.2, -0.2), color=color.black),
        sphere(radius=0.1, pos=vector(0, 0, -0.5), color=color.black),
        sphere(radius=0.1, pos=vector(-0.2, 0.2, -0.5), color=color.black),
        sphere(radius=0.1, pos=vector(-0.2, -0.2, -0.5), color=color.black),
        sphere(radius=0.1, pos=vector(0.2, 0.2, -0.5), color=color.black),
        sphere(radius=0.1, pos=vector(0.2, -0.2, -0.5), color=color.black),
        sphere(radius=0.1, pos=vector(-0.15, -0.5, -0.2), color=color.black),
        sphere(radius=0.1, pos=vector(-0.15, -0.5, 0), color=color.black),
        sphere(radius=0.1, pos=vector(-0.15, -0.5, 0.2), color=color.black),
        sphere(radius=0.1, pos=vector(0.15, -0.5, 0.2), color=color.black),
        sphere(radius=0.1, pos=vector(0.15, -0.5, 0), color=color.black),
        sphere(radius=0.1, pos=vector(0.15, -0.5, -0.2), color=color.black)
    ])
    d.pos = vector(posx, y, 0)
    return d

for i in range(numOfDiceAnimate):
    x_pos = start_x + 2 * i
    dice_list.append(make_die(x_pos))

gbar_sum = graph(title="Sum Frequency", xtitle="Sum", ytitle="Frequency")
bar_graph_sum = gvbars(color=color.red)
gbar_face = graph(title="Dice Face Frequency", xtitle="Face", ytitle="Frequency")
bar_graph_face = gvbars(color=color.blue)
freq_sum = {}
freq_face = {f: 0 for f in range(1,7)}
table_text = wtext(text="")

def faceCamera(dice, num):
    dice.axis = vector(1,0,0)
    dice.up = vector(0,1,0)
    faces = [vector(0,1,0), vector(0,0,1), vector(1,0,0),
             vector(-1,0,0), vector(0,0,-1), vector(0,-1,0)]
    face = faces[num-1]
    target = -scene.forward.norm()
    angle = diff_angle(face, target)
    axis = cross(face, target)
    if mag(axis) > 0.001:
        dice.rotate(angle=angle, axis=axis.norm())

def update_graphs():
    bar_graph_sum.data = []
    for s in sorted(freq_sum):
        bar_graph_sum.plot(pos=(s,freq_sum[s]))
    bar_graph_face.data = []
    for f in freq_face:
        bar_graph_face.plot(pos=(f,freq_face[f]))
    tableText = "\nDice Roll Results\nDie | Count\n"
    for i in range(6):
        tableText += f" {i+1}   |    {freq_face[i+1]}\n"
    table_text.text = tableText

def animate():
    axes = []
    for _ in range(numOfDiceAnimate):
        axes.append(vector(logistic_rand(), logistic_rand(), logistic_rand()).norm())
    t = 0
    while t < 1.5:
        rate(60)
        t += 0.02
        for i, d in enumerate(dice_list):
            d.rotate(angle=0.3, axis=axes[i])
    for d in dice_list:
        d.rotate(angle=2*pi*logistic_rand(), axis=vector(1,0,0))
        d.rotate(angle=2*pi*logistic_rand(), axis=vector(0,1,0))
        d.rotate(angle=2*pi*logistic_rand(), axis=vector(0,0,1))

def reroll(evt=None):
    animate()
    results = []
    for _ in range(numOfDice):
        results.append(chaotic_die())
    total = sum(results)
    freq_sum[total] = freq_sum.get(total,0) + 1
    for r in results:
        freq_face[r] += 1
    update_graphs()
    for i in range(min(numOfDiceAnimate, len(results))):
        faceCamera(dice_list[i], results[i])

reroll()
button(text="Reroll", bind=reroll)