import time
import turtle as t

t.speed(0)


# turtle.forward(50)
# turtle.left(45)
#
# turtle.forward(50)
# turtle.left(45)
#
# turtle.forward(50)
# turtle.left(45)
#
# turtle.forward(50)


# def rectangle(width, height):
#     for _ in range(2):
#         turtle.forward(height)
#         turtle.left(90)
#         turtle.forward(width)
#         turtle.left(90)
#
# rectangle(10, 20)


# def triangle(side):
#     for i in range(3):
#         turtle.forward(side)
#         turtle.left(120)
#
# triangle(90)


# def square(side):
#     tmp = 75
#     for _ in range(3):
#         turtle.setheading(tmp)
#         tmp -= 30
#         for i in range(4):
#             turtle.forward(side)
#             turtle.left(90)
#
# square(50)


# def square(side):
#     tmp = 45
#     for _ in range(8):
#         turtle.setheading(tmp)
#         tmp -= 45
#         for i in range(4):
#             turtle.forward(side)
#             turtle.left(90)
#
# square(50)


# def hexagon(side):
#     for _ in range(6):
#         turtle.forward(side)
#         turtle.right(60)
#
# hexagon(50)

# def sote(side):


# def hexagon(side):
#     for _ in range(6):
#         turtle.forward(side)
#         turtle.right(60)
# for _ in range(7):
#     turtle.forward(50)
#     turtle.left(60)
#     hexagon(50)


# def romb(side):
#     for _ in range(2):
#         turtle.forward(side)
#         turtle.left(120)
#         turtle.forward(side)
#         turtle.left(60)
#
# romb(60)

# def rombus_star(side, romb_sum):
#     for _ in range(romb_sum):
#         start_romb = 360 / romb_sum
#         turtle.left(start_romb)
#         for i in range(2):
#             # turtle.forward(side)
#             # turtle.left(120 - 60 * (i % 2))
#             turtle.forward(side)
#             turtle.left(60)
#             turtle.forward(side)
#             turtle.left(120)
#
# rombus_star(100, 100)


# def line_star(side, line_sum):
#     for _ in range(line_sum):
#         start_line = 360 / line_sum
#         turtle.left(start_line)
#         turtle.forward(side)
#         turtle.back(side)
#
# line_star(100, 120)


# def star(side):
#     for _ in range(5):
#         turtle.forward(side)
#         turtle.right(144)
#
#
# star(100)

# def square(side):
#     for i in range(4):
#         turtle.forward(side)
#         turtle.right(90)
#
# def figure(side, sum, step):
#     turtle.left(180)
#     for _ in range(sum):
#         side = side + step
#         square(side)
#
# figure(10, 100, 2)


# def figure(side, sum_side, step):
#     for _ in range(sum_side):
#         t.left(90)
#         t.forward(side)
#         side += step
#
# figure(5, 33, 5)


# def punctir_line(num):
#     for _ in range(num):
#         turtle.dot(10)
#         turtle.penup()
#         turtle.forward(15)
#         turtle.pendown()
#
# punctir_line(10)

# def rectangle(width, height):
#     for _ in range(2):
#         turtle.dot(10)
#         turtle.forward(height)
#         turtle.left(90)
#         turtle.dot(10)
#         turtle.forward(width)
#         turtle.left(90)
#
# rectangle(50, 80)


# def line_star(side, line_sum):
#     turtle.dot(25)
#     start_line = 360 / line_sum
#     for _ in range(line_sum):
#         turtle.left(start_line)
#         turtle.forward(side)
#         turtle.shape('triangle')
#         turtle.stamp()
#         turtle.back(side)
#
#
# line_star(100, 9)


# def turtle_circle(side, line_sum):
#     turtle.shape('turtle')
#     start_line = 360 / line_sum
#     for _ in range(line_sum):
#         turtle.left(start_line)
#         turtle.penup()
#         turtle.forward(side)
#         turtle.stamp()
#         turtle.back(side)
#
# turtle_circle(100, 10)


# def turtle_circle(side, line_sum):
#     turtle.bgcolor('CadetBlue')
#     turtle.shape('turtle')
#     turtle.pensize(3)
#     start_line = 360 / line_sum
#     for _ in range(line_sum):
#         turtle.left(start_line)
#         turtle.penup()
#         turtle.forward(side - 30)
#         turtle.pendown()
#         turtle.forward(15)
#         turtle.penup()
#         turtle.forward(15)
#         turtle.stamp()
#         turtle.back(side)
#
# turtle_circle(100, 10)



# def turtle_spiral(sum_turtle):
#     t.Screen().bgcolor('DarkSeaGreen3')
#     t.shape('turtle')
#     t.penup()
#     turtle_sum = 360 / sum_turtle
#     side = 10
#     for _ in range(sum_turtle):
#         t.stamp()
#         t.right(25)
#         t.forward(side)
#         side += 2
#
#
# turtle_spiral(330)


import random


# def spiral(side, sum_side, step):
#   t.Screen().colormode(255)
#   tmp = 1
#   for i in range(1, sum_side):
#       t.pensize(tmp)
#       colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
#       #color = random.sample(range(255), 3)
#       t.pencolor(colors[i % 6])
#       t.left(45)
#       t.forward(side)
#       side += step
#       tmp += 0.1
#
#
# spiral(5, 45, 1)

# def david_star(side):
#     for i in range(3):
#         t.forward(side)
#         t.right(120)
#     t.penup()
#     t.setposition(0, -120)
#     t.pendown()
#     for i in range(3):
#         t.forward(side)
#         t.left(120)
#
# david_star(200)

# def rays():
#     t.hideturtle()
#     t.dot(8, 'orange')
#     t.color('green')
#     for i in range(-100, 100, 20):
#         t.goto(i, -100)
#         t.dot(5, 'blue')
#         t.goto(0, 0)
#
# rays()

# def olimp_circle():
#     t.hideturtle()
#     t.pensize(5)
#     circles = {'blue': (-100, -100),
#                'black': (0, -100),
#                'red': (100, -100),
#                'yellow': (-50, -150),
#                'green': (50, -150)}
#     for color in circles:
#         t.penup()
#         t.goto(circles[color])
#         t.color(color)
#         t.pendown()
#         t.circle(50)

    # for i in range(-100, 101, 100):
    #     t.penup()
    #     t.goto(i, -100)
    #     t.pendown()
    #     t.circle(50, )
    #     t.penup()
    #     t.goto(0, 0)
    # for i in range(-50, 51, 100):
    #     t.penup()
    #     t.goto(i, -150)
    #     t.pendown()
    #     t.circle(50)
    #     t.penup()
    #     t.goto(0, 0)

#olimp_circle()






















time.sleep(5)
