import turtle


def draw_pattern1(pen):
    for i in range(180):
        pen.fd(100)
        pen.right(30)
        pen.fd(20)
        pen.left(60)
        pen.fd(50)
        pen.right(30)

        pen.penup()
        pen.setposition(0, 0)
        pen.pendown()

        pen.right(2)
