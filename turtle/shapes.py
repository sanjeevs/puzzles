import turtle


def draw_polygon(pen, num_sides, side_length):
    angle = 360.0 / num_sides
    for _ in range(num_sides):
        pen.fd(side_length)
        pen.rt(angle)


def draw_star(pen, side_length, angle=144):
    for _ in range(5):
        pen.fd(side_length)
        pen.rt(angle)


def draw_spiral(pen, side_length):
    for i in range(20):
        pen.fd(i * 10)
        pen.rt(144)


def draw_square(pen, side_length):
    draw_polygon(pen, 4, side_length)
