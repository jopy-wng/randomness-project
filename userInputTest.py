Web Vpython 3.2
import random

fakeDice = box()

def changeSides(input):
    selected = input.selected
    print("Selected:", selected)
    if selected == '5':
        print("hi")
    elif selected == '6':
        print("world")
    else:
        print("Choose sides...")

choiceList = ['Sides', '5', '6']
menu(choices = choiceList, bind = changeSides)

def rollDice(input):
    if input.text == 'roll':
        rollButton.text = 'stop'
        actuallyRollDice()
    else:
        fakeDice.rotate(angle = 0, axis = vector(0, 0, 0))
        rollButton.text = 'roll'

rollButton = button(bind = rollDice, text='roll')

def actuallyRollDice():
    timer = 0
    while timer != 1:
        rate(60)
        fakeDice.rotate(angle = random.uniform(0, 2 * pi), axis = vector(3, 4, 5))
        timer = timer + 0.01
    fakeDice.rotate(angle = 0)