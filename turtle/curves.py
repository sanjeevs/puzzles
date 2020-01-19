import turtle


def draw_circle(pen, incr, angle, total_trip=360):
    num_steps = round(total_trip / angle)
    for i in range(num_steps):
        pen.fd(incr)
        pen.rt(angle)


def draw_qcircle(pen, incr, angle):
    draw_circle(pen, incr, angle, 90)


def draw_spiral(pen, incr, angle):
    for i in range(1024):
        pen.fd(incr)
        pen.rt(angle)
        angle *= 0.99


if __name__ == "__main__":
    pen = turtle.Turtle()
    pen.speed(0)
    win = turtle.Screen()
    print("Screen Width=", win.window_width(), ",Height=", win.window_height())
    print("Pen initial state xcor=", pen.xcor(), ",ycor=", pen.ycor())
    start_x = (win.window_width() / 2 - 30) * -1
    start_y = win.window_height() / 2
    draw_circle(pen, 15, 5, 90)
    #draw_spiral(pen, 5, 20)

    input("press any key to continue")
