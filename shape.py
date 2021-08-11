# drawing a regular polygon
import turtle
import time
t = turtle.Turtle()
screen = t.getscreen()
global x   
x = 1
def shape(x):
    t.reset()
    x = int(screen.textinput("sides","num of sides: "))
    ai = (180*(x-2))/x

    for i in range(x):
        t.forward(30)
        t.left(180 - ai)

    time.sleep(0.5)

def main():
    try:
        while x != 0:
            shape(x)
    except:
        print("exiting...")
        quit()

main()
