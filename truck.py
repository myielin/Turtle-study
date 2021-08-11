import turtle

t = turtle.Turtle()
screen = t.getscreen()
t.pen(fillcolor="black")
commands = ["wheel", "sety", "wheel", "left", "left", "right", "left", "left", "right", "left", "left"]
args = [None, 120, 0, 0, None, 60, 90, 50, 90, 40, 55, 70, 55, 40, 90, 57, 90, 120, 90, 54, 90, 54]

def wheel():
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.sety(20)

def draw():
    for i in range(len(args)):
        if i % 2 != 0:
            t.forward(args[i])
        else:
             if commands[i//2] == "sety":
                 t.sety(args[i])
             elif commands[i//2] == "wheel":
                 wheel()
             elif commands[i//2] == "left":
                 t.left(args[i])
             elif commands[i//2] == "right":
                 t.right(args[i])


draw()
screen.exitonclick()
