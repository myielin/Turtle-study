import turtle
import random
import time
t = turtle.Turtle()
s = t.getscreen()
rand = random.Random()
class ball:
    def __init__(self, *a):
        self.a =a
    def show(self, c, r):
        rx = rand.randint(-300, 300)
        ry = rand.randint(-300, 300)

        t.penup()
        t.pen(fillcolor=c)
        t.goto(rx, ry)
        t.pendown()
        t.begin_fill()
        t.circle(r)
        t.end_fill()


def calls():
    cs = ["blue", "red", "pink", "purple", "cyan", "white", "black"]
    for i in range(10):
        rc = rand.randint(0, 6)
        r = rand.randint(10, 50)
        bll = ball()
        bll.show(cs[rc], r)

calls()
s.exitonclick()
