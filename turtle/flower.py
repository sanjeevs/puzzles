import turtle
import curves
import random


def draw_petal(pen, len=15):
    curves.draw_qcircle(pen, len, 5)
    pen.rt(90)
    curves.draw_qcircle(pen, len, 5)
    pen.rt(90)


def draw_flower(pen, len, num_petals):
    for _ in range(num_petals):
        draw_petal(pen, len)
        pen.rt(360 / num_petals)


def draw_plant(pen, len=15):
    draw_flower(pen, len, 10)
    pen.rt(90)
    pen.fd(200)
    pen.lt(90)
    draw_petal(pen, len)
    pen.rt(90)
    pen.fd(100)
    pen.lt(90)  # Return to original heading.


def slide(pen, shift):
    pen.penup()
    pen.fd(shift)
    pen.pendown()


def draw_garden(pen, num_plants):
    for _ in range(num_plants):
        draw_plant(pen, len=random.randint(5, 15))
        slide(pen, shift=random.randint(50, 200))
        draw_plant(pen, random.randint(5, 25))


if __name__ == "__main__":
    pen = turtle.Turtle()
    pen.speed(0)
    pen.goto(0, 100)
    draw_garden(pen, 10)

    input("Pause any key to continue")
