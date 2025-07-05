#########################################
# John Zetterman
# Assignment 1, Problem 2A
# June 6, 2025
#
# Description: This program draws two isosceles triangles by calculating
#              the lengths and angles using some basic trigonometry.
# Inputs: None
# Outputs: Draws two triangles, one is filled in blue.
# Sources: https://docs.python.org/3/library/turtle.html
#########################################

import turtle, math

t1 = turtle.Turtle()
t2 = turtle.Turtle()

# Triangle A:
# Calculate the lengths and angles using a bit of trigonometry
height_a = 250
base = 2 * height_a
equal_side_a = math.sqrt((2 * height_a) ** 2 + (base / 2) ** 2)
angle_a = math.degrees(math.atan(2 * height_a / (base / 2)))


# Hide the turtle, set the speed, and center in the box.
t1.hideturtle()
t1.speed(10)
t1.penup()
t1.goto(-base / 2, 0)
t1.pendown()

# Draw the triangle
t1.forward(base)
t1.left(180 - angle_a)
t1.forward(equal_side_a)
t1.left(2 * angle_a)
t1.forward(equal_side_a)

# Triangle B:
# Calculate the lengths and angles using a bit of trigonometry
height_b = 125
equal_side_b = math.sqrt((2 * height_b) ** 2 + (base / 2) ** 2)
angle_b = math.degrees(math.atan(2 * height_b / (base / 2)))

# Hide the turtle, set the speed, and center in the box.
t2.hideturtle()
t2.speed(10)
t2.penup()
t2.goto(-base / 2, 0)
t2.pendown()

# Draw the second triangle
t2.fillcolor("blue")
t2.begin_fill()
t2.forward(base)
t2.left(180 - angle_b)
t2.forward(equal_side_b)
t2.left(2 * angle_b)
t2.forward(equal_side_b)
t2.end_fill()

turtle.done()
