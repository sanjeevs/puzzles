import turtle
import shapes

pen = turtle.Turtle()
for _ in range(6):
    shapes.draw_square(pen, 100)
    pen.left(30)

input("Press any key to continue")
