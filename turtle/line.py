import turtle
import math


def line(pen, len):
    pen.fd(len)
    pen.bk(len)


def draw_axes(pen):
    for _ in range(4):
        line(pen, 100)
        pen.rt(90)


def draw_y_4x(pen):
    """ draw line with starting turle facing east."""
    xcord = 10
    ycord = 40
    dx = 1
    len = 0
    while xcord != 40:
        dy = 4 * dx
        ycord += dy
        pen.fd(dx)
        pen.lt(90)
        pen.fd(dy)
        pen.rt(90)
        xcord += dx
        len += math.sqrt(dx**2 + dy**2)
    print("Draw line ended with xcord=", xcord, " ycord=", ycord)
    print("Length of arc=", len)


if __name__ == "__main__":
    pen = turtle.Turtle()
    pen.speed(0)
    draw_axes(pen)
    draw_y_4x(pen)
    input("Press any key to continue")
