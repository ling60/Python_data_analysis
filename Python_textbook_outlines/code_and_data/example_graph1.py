# inspired by: https://michael0x2a.com/blog/turtle-examples
import turtle
import random

painter = turtle.Turtle()
painter.speed(30)

def draw(length, step=50, angle=123):
    painter.pencolor(random.random(),random.random(), random.random())
    for i in range(step):
        painter.forward(length)
        painter.left(angle)

for i in range(12):
    draw(150 + i * 20, step=40)
    painter.forward(150 + i * 20)

turtle.done()