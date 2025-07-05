#########################################
# John Zetterman
# Assignment 1, Problem 2B
# June 6, 2025
#
# Description: This program draws a graph with a circle in the middle of it
# Inputs: None
# Outputs: Draws a graph with a circle in the center.
# Sources: https://docs.python.org/3/library/turtle.html
#########################################

import turtle

# Set text characterics
font_size = 12
font = ("Arial", font_size, "normal")

# Draw the graph
t = turtle.Turtle()

length = 200

# Hide turtle, set speed
t.hideturtle()
t.speed(10)

### Draw X axis elements

# West
t.penup()
text = "West"
char_count = len(text)
width = char_count * (1.5 * font_size)
t.goto(-length + width, -10)
t.pendown()
t.write(text, move=False, align="center", font=font)

# East
t.penup()
text = "East"
char_count = len(text)
width = char_count * (1.5 * font_size)
font = ("Arial", font_size, "normal")
t.goto(length - width, -10)
t.pendown()
t.write(text, move=False, align="center", font=font)

# X Axis Line
t.penup()
t.goto(-length / 2, 0)
t.pendown()
t.forward(length)

### Draw Y axis

# North
t.penup()
text = "North"
t.goto(0, length / 2)
t.pendown()
t.write(text, move=False, align="center", font=font)

# South
t.penup()
text = "South"
t.goto(0, -((length + (font_size * 3)) / 2))
t.pendown()
t.write(text, move=False, align="center", font=font)

# Y Axis Line
t.penup()
t.goto(0, -length / 2)
t.pendown()
t.left(90)
t.forward(length)

# Draw the circle
radius = 25
t.penup()
t.goto(radius, 0)
t.pendown()
t.circle(radius)

turtle.done()
