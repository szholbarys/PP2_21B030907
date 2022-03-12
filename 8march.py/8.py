import turtle
import math

def x(t):
    return 16 * math.sin(t) ** 3
def y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)
t = turtle.Turtle()
t.speed(1000)
turtle.colormode(255)
turtle.title("8 march")
turtle.Screen().bgcolor(0,0,0)
for i in range(2550):
    t.goto((x(i) * 20, y(i) * 20))
    t.pencolor('red')
    t.goto(0,0)
t.hideturtle()
turtle.update()
turtle.mainloop()    