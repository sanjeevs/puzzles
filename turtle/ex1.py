import turtle


def draw_line(pen, start, end):
    pen.penup()
    pen.goto(start[0], start[1])
    pen.pendown()
    pen.goto(end[0], end[1])


def draw_pattern(pen, sign):
    for i in range(0, 11):
        draw_line(pen, (0, (10 - i) * 20 * sign[1]), (i * 20 * sign[0], 0))


pen = turtle.Turtle()

pen.color("red")

draw_pattern(pen, (1, 1))
draw_pattern(pen, (-1, 1))
draw_pattern(pen, (-1, -1))
draw_pattern(pen, (1, -1))

input("Press any key to continue")
