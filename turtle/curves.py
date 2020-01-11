import turtle


def draw_circle(pen, incr, angle):
    num_steps = round(360 / angle)
    for i in range(num_steps):
        pen.fd(incr)
        pen.rt(angle)


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
    # pen.penup()
    #pen.goto(start_x, start_y)
    # pen.pendown()
    draw_spiral(pen, 5, 20)

    input("press any key to continue")
