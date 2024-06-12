import math
import turtle as t
from turtle import TurtleScreen, RawTurtle, Shape
from tkinter import *
import textwrap
import time
import sys


def drawArc(t1, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t1, n, step_length, step_angle)


def polyline(t1, n, length, angle):
    for index in range(n):
        t1.fd(length)
        t1.lt(angle)


def flower(n):
    my_turtle.fillcolor("#db4e79")
    my_turtle.begin_fill()
    for x in range(n):
        my_turtle.forward(0.5)
        if x < 80:
            my_turtle.left(1)
        elif x < 120:
            my_turtle.left(2.3)
        else:
            my_turtle.left(1)
    my_turtle.end_fill()


def draw_eyes(x1, y1, heading):
    my_turtle.pensize(5)
    my_turtle.penup()
    my_turtle.goto(x1, y1)
    my_turtle.setheading(heading)
    my_turtle.pendown()
    my_turtle.fillcolor("#000")
    my_turtle.begin_fill()
    step = 0.3

    for i in range(2):
        for j in range(60):
            if j < 30:
                step += 0.02
            else:
                step -= 0.02
            my_turtle.forward(step)
            my_turtle.left(3)
    my_turtle.end_fill()


def draw_nose(x1, y1, heading):
    my_turtle.pensize(5)
    my_turtle.penup()
    my_turtle.goto(x1, y1)
    my_turtle.setheading(heading)
    my_turtle.pendown()
    my_turtle.fillcolor("#e7be04")
    my_turtle.begin_fill()
    step = 0.3

    for i in range(2):
        for j in range(60):
            if j < 30:
                step += 0.02
            else:
                step -= 0.02
            my_turtle.forward(step)
            my_turtle.left(3)
    my_turtle.end_fill()


def draw_text_on_screen(turtle, message, font_path, font_size, color=(0, 0, 0)):
    """
    Draws text on the Turtle graphics canvas.

    Args:
        turtle: The Turtle object where the text will be drawn.
        message: The text to be drawn.
        font_path: Path to the TrueType Font (TTF) file.
        font_size: Size of the font in pixels.
        color: Optional color for the text (defaults to black).
    """
    from PIL import Image, ImageDraw, ImageFont

    # Create an empty image to draw the text
    image_size = (600, 100)  # Adjust size as needed
    image = Image.new("RGB", image_size, (255, 255, 255))  # White canvas
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    image_width = 400
    margin = 20
    available_width = image_width - 2 * margin  # Deducting margin from both sides
    wrap_size = available_width
    wrapped_text = textwrap.fill(message, width=wrap_size)
    # Draw the text directly on the canvas
    draw.text((0, 0), wrapped_text, fill=color, font=font)

    # Save the image as a GIF file
    image.save("text_image.gif", format="GIF")

    # Display the image with Turtle
    screen = turtle.getscreen()
    screen.register_shape("text_image.gif")
    turtle.shape("text_image.gif")


# Create a Turtle object
my_turtle = t.Turtle()

# Setup Turtle window
window = t.Screen()
window.setup(width=600, height=600)

window.screensize(600, 600, "white")
my_turtle.penup()
my_turtle.setpos(175, 175)
my_turtle.pendown()
my_turtle.pensize(8)
my_turtle.pencolor("black")
my_turtle.speed(0)

my_turtle.penup()
my_turtle.goto(-130, 170)
my_turtle.pendown()
my_turtle.setheading(220)

for x in range(580):
    my_turtle.forward(1)
    if x < 250:
        my_turtle.left(0.5)
    elif x < 350:
        my_turtle.left(0.1)
    else:
        my_turtle.left(0.5)

my_turtle.setheading(70)
for y in range(150):
    my_turtle.forward(1)
    if y < 80:
        my_turtle.left(0.2)
    elif y < 90:
        my_turtle.left(10)
    else:
        my_turtle.left(0.2)
my_turtle.setheading(160)
for y1 in range(140):
    my_turtle.forward(1)
    my_turtle.left(0.15)
my_turtle.setheading(140)
for y2 in range(157):
    my_turtle.forward(1)
    if y2 < 65:
        my_turtle.left(0.2)
    elif y2 < 75:
        my_turtle.left(8)
    else:
        my_turtle.left(0.5)


draw_eyes(-100, 60, 350)
draw_eyes(50, 40, 350)
draw_nose(-40, 30, 260)

my_turtle.penup()
my_turtle.goto(20, 180)
my_turtle.pendown()
my_turtle.fillcolor("#dd4a75")
my_turtle.begin_fill()
my_turtle.setheading(175)
flower(200)
my_turtle.setheading(250)
flower(200)
my_turtle.setheading(325)
flower(200)
my_turtle.setheading(40)
flower(200)
my_turtle.setheading(115)
flower(200)
my_turtle.end_fill()
my_turtle.penup()

my_turtle.goto(22, 179)
my_turtle.setheading(270)
my_turtle.pendown()
my_turtle.fillcolor("#e7be04")
my_turtle.begin_fill()
my_turtle.circle(20)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(-150, 65)
my_turtle.pendown()
my_turtle.setheading(170)
my_turtle.pensize(6)
for y in range(40):
    my_turtle.forward(1)
    my_turtle.left(0.3)

my_turtle.penup()
my_turtle.goto(-150, 85)
my_turtle.pendown()
my_turtle.setheading(160)
for y in range(50):
    my_turtle.forward(1)
    my_turtle.left(0.3)

my_turtle.penup()
my_turtle.goto(-150, 45)
my_turtle.pendown()
my_turtle.setheading(180)
for y in range(55):
    my_turtle.forward(1)
    my_turtle.left(0.3)

my_turtle.penup()
my_turtle.goto(110, 10)
my_turtle.setheading(340)
my_turtle.pendown()
for y in range(40):
    my_turtle.forward(1)
    my_turtle.right(0.3)

my_turtle.penup()
my_turtle.goto(120, 30)
my_turtle.setheading(350)
my_turtle.pendown()
for i in range(30):
    my_turtle.forward(1)
    my_turtle.right(0.3)

my_turtle.penup()
my_turtle.goto(115, 50)
my_turtle.setheading(36)
my_turtle.pendown()
for i in range(50):
    my_turtle.forward(1)
    my_turtle.right(0.3)

my_turtle.pensize(8)
my_turtle.penup()
my_turtle.goto(-100, -30)
my_turtle.setheading(230)
my_turtle.pendown()
my_turtle.fillcolor("#efa9c1")
my_turtle.begin_fill()
for i in range(140):
    my_turtle.forward(1)
    my_turtle.left(0.2)
my_turtle.setheading(340)
for z in range(200):
    my_turtle.forward(1)
    my_turtle.left(0.1)
my_turtle.setheading(85)
for j in range(140):
    my_turtle.forward(1)
    my_turtle.left(0.1)
my_turtle.end_fill()
my_turtle.penup()
my_turtle.goto(-73, -33)
my_turtle.pendown()
my_turtle.setheading(250)
my_turtle.fillcolor("#da4b76")
my_turtle.begin_fill()
drawArc(my_turtle, 40, 205)
my_turtle.setheading(170)
my_turtle.pensize(6)
my_turtle.forward(75)
my_turtle.end_fill()

my_turtle.pensize(8)
my_turtle.penup()
my_turtle.goto(-120, -17)
my_turtle.setheading(230)
my_turtle.pendown()
my_turtle.fillcolor("#d64b75")
my_turtle.begin_fill()
my_turtle.forward(50)
my_turtle.setheading(320)
for k in range(27):
    my_turtle.forward(1)
    my_turtle.left(1)
my_turtle.setheading(55)
for i in range(50):
    my_turtle.forward(1)
    my_turtle.right(0.1)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(-125, -15)
my_turtle.setheading(140)
my_turtle.pendown()
my_turtle.fillcolor("#fff")
my_turtle.begin_fill()
my_turtle.forward(8)
my_turtle.setheading(50)
drawArc(my_turtle, 10, 190)
my_turtle.setheading(150)
for j in range(80):
    my_turtle.forward(1)
    my_turtle.left(2.2)
my_turtle.forward(24)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(27, -45)
my_turtle.pendown()
my_turtle.fillcolor("#db4e79")
my_turtle.setheading(350)
my_turtle.begin_fill()
for x in range(50):
    my_turtle.forward(1)
    my_turtle.right(1)

my_turtle.setheading(220)
my_turtle.forward(40)
my_turtle.setheading(100)
for x in range(50):
    my_turtle.forward(1)
    my_turtle.left(0.2)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(70, -75)
my_turtle.pendown()
my_turtle.setheading(300)
my_turtle.forward(8)
my_turtle.setheading(30)
for x in range(40):
    my_turtle.forward(1)
    my_turtle.right(5)
my_turtle.setheading(280)
for x in range(70):
    my_turtle.forward(1)
    my_turtle.right(2)

my_turtle.penup()
my_turtle.goto(-70, -180)
my_turtle.pendown()
my_turtle.setheading(250)
for x in range(30):
    my_turtle.forward(1)
    my_turtle.left(0.3)
for x in range(160):
    my_turtle.forward(1)
    if x < 30:
        my_turtle.left(3)
    elif x < 65:
        my_turtle.left(0.1)
    else:
        my_turtle.left(1)

my_turtle.penup()
my_turtle.goto(-150, -210)
my_turtle.setheading(340)
my_turtle.pendown()
my_turtle.fillcolor("#fff")
my_turtle.begin_fill()
step = 1.5
for i in range(2):
    for j in range(60):
        if j < 30:
            step += 0.1
        else:
            step -= 0.1
        my_turtle.forward(step)
        my_turtle.left(3)
my_turtle.end_fill()


message = sys.argv[1]
my_turtle.penup()
my_turtle.setpos(40, -325)
draw_text_on_screen(
    my_turtle,
    f"{message}",
    "/System/Library/Fonts/Supplemental/Brush Script.ttf",
    75,
    color=(248, 200, 220),
)

t.done()
