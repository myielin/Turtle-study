# this code creates random trucks in the screen
import turtle
import random

t = turtle.Turtle()
screen = t.getscreen()
screen.setworldcoordinates(-500, -500, 500, 500)
t.pen(fillcolor="black")

# these two paralel lists create the truck drawing
commands = ["wheel", "sety", "wheel", "left", "left", "right", "left", "left", "right", "left", "left"]
args = [None, 120, 1, 0, None, 60, 90, 50, 90, 40, 55, 70, 55, 40, 90, 57, 90, 120, 90, 50, 90, 54]

def draw():
    rand = random.Random()
    rvalue =  rand.randint(1, 700)/400

    t.penup()
    yc = rand.randint(-400, 400)
    t.goto(rand.randint(-400, 400), yc)
    t.pendown()

    def wheel():
        t.begin_fill()
        t.circle(20*rvalue)
        t.end_fill()
        t.sety(yc+20*rvalue)

    for i in range(len(args)):
        if i % 2 != 0:
            t.forward(args[i]*rvalue)
        else:
             if commands[i//2] == "sety":
                  t.sety(rvalue+yc)
             if commands[i//2] == "wheel":
                 wheel()
             elif commands[i//2] == "left":
                 t.left(args[i])
             elif commands[i//2] == "right":
                 t.right(args[i])

def main():
    try:
        v = screen.textinput("value", "how many trucks: ")
        for p in range(int(v)):
            draw()
    except:
        print("integer value expected")

main()
screen.exitonclick()
