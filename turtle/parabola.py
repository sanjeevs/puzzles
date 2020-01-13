import turtle
import math


def draw_arc(pen, start_cord, derivative, endx):
    """ draw line with starting turle facing east."""
    (xcord, ycord) = start_cord
    dx = 1
    len = 0
    while xcord != endx:
        dy = derivative(xcord, dx)
        ycord += dy
        pen.fd(dx)
        pen.lt(90)
        pen.fd(dy)
        pen.rt(90)
        xcord += dx
        len += math.sqrt(dx**2 + dy**2)
    print("Draw arc ended with xcord=", xcord, " ycord=", ycord)
    print("Length of arc=", len)


def line(pen, len):
    pen.fd(len)
    pen.bk(len)


def draw_axes(pen):
    for _ in range(4):
        line(pen, 100)
        pen.rt(90)


def draw_parabola(pen):
    startx = 1
    endx = 40
    draw_arc(pen, (startx, startx ** 2), lambda x, dx: 2 * x * dx, endx)


if __name__ == "__main__":
    pen = turtle.Turtle()
    pen.speed(0)
    draw_axes(pen)
    draw_parabola(pen)
    input("Press any key to continue")
