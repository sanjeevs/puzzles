import turtle


def is_on_screen(pen):
    win = turtle.Screen()
    max_xcor = win.window_width() / 2
    max_ycor = win.window_height()
    if pen.xcor() > max_xcor:
        return False
    if pen.ycor() > max_ycor:
        return False
    return True


def draw_spi(pen, len=20):
    incr = len
    pen.fd(incr)
    pen.rt(90)
    while(True):
        for _ in range(2):
            incr += 1
            pen.fd(incr)
            pen.rt(90)
            if not is_on_screen(pen):
                break
        pen.rt(5)


if __name__ == "__main__":
    pen = turtle.Turtle()
    pen.rt(30)
    draw_spi(pen)
    input("Press any key to continue")
