Web VPython 3.2
import random

scene = canvas(width = 600, height = 400)
scene.userzoom = False

menu(choices = ['5 sides', '6 sides'], bind = numOfSides)
inp = int(input("How many dice would you like? (1–10): "))
cutInp = input("Cut? Enter y/n")
run = True

numOfDice = 0

if inp > 10:
    numOfDice = 10
else:
    numOfDice = inp

numOfDice = max(1, min(numOfDice, 10))

dice_list = []

start_x = -2 * (numOfDice - 1) / 2
y = 0

def numOfSides(sides):
    console.log(sides)
    if sides.index is 5: (print("hi"))
    else if sides.index is 6: (print("hello"))

for i in range(numOfDice):
    x = start_x + 2 * i
    d = compound([box(), 
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
    
def faceCamera(dice, num):
    #reset dice to default orientation
    dice.axis = vector(1, 0, 0)
    dice.up = vector(0, 1, 0)
  
    faces = [vector(0, 1, 0), vector(0, 0, 1), vector(1, 0, 0), vector(-1, 0, 0), vector(0, 0, -1), vector(0, -1, 0)]
    
    face = faces[num - 1]
    target = -scene.forward.norm()  #point to camera
    
    #calculate rotation
    angle = diff_angle(face, target)
    axis = cross(face, target)
    
    if mag(axis) > 0.001: #checks there needs to be a rotation as the axis would not be zero
        dice.rotate(angle=angle, axis=axis.norm())
        
def faceCameraFiveSided(dice, num):
    dice.axis = vector(1, 0, 0)
    dice.up = vector(0, 1, 0)
    
    apex_height = 0.5
    base_size = 1.0
    
    face1_normal = vector(0, 0.6, 1).norm()
    face2_normal = vector(1, 0.6, 0).norm()
    face3_normal = vector(-1, 0.6, 0).norm()
    face4_normal = vector(0, 0.6, -1).norm()
    face5_normal = vector(0, -1, 0)
    
    faces = [face1_normal, face2_normal, face3_normal, face4_normal, face5_normal]
    
    face = faces[num - 1]
    target = -scene.forward.norm()
    
    angle = diff_angle(face, target)
    axis = cross(face, target)
    
    if mag(axis) > 0.001:
        dice.rotate(angle=angle, axis=axis.norm())

for d in dice_list:
    randOr(d)

results = [random.randint(1, 6) for i in range(inp)]

for d, result in zip(dice_list, results):
    faceCamera(d, result)

counterOne = 1
counterTwo = 1
counterThree = 1
counterFour = 1
counterFive = 1
counterSix = 1

num = [0, 0, 0, 0, 0, 0]

for i in results:
    if i == 1:
        num[0] += 1
    if i == 2:
        num[1] += 1
    if i == 3:
        num[2] += 1
    if i == 4:
        num[3] += 1
    if i == 5:
        num[4] += 1
    if i == 6:
        num[5] += 1

tableText = "\nDice Roll Results\n"
tableText += "Die | Count\n"
for i in range(6):
    tableText += f" {i+1}   |    {num[i]}\n"

wtext(text=tableText)


gbar = graph(title = "Dice Roll Frequencies", xtitle = "Possible Sides", ytitle = "Times Rolled")
bar_graph = gvbars(delta = 1, color = color.red)
for i in range(len(results)):
    if results[i] == 1: bar_graph.plot(pos = (1, counterOne)); counterOne += 1
    if results[i] == 2: bar_graph.plot(pos = (2, counterTwo)); counterTwo += 1
    if results[i] == 3: bar_graph.plot(pos = (3, counterThree)); counterThree += 1
    if results[i] == 4: bar_graph.plot(pos = (4, counterFour)); counterFour += 1
    if results[i] == 5: bar_graph.plot(pos = (5, counterFive)); counterFive += 1
    if results[i] == 6: bar_graph.plot(pos = (6, counterSix)); counterSix += 1
    
