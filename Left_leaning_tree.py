import turtle
import math

screen = turtle.Screen()
screen.bgcolor("skyblue")

alan = turtle.Turtle()
alan.shape("turtle")
alan.color("green")
alan.fillcolor("tan")
alan.speed(0)

def drawSquare(t, size):
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.penup()

def drawApple(t, position, size):
    t.penup()
    t.goto(position)
    t.pendown()

    t.color("red")
    t.fillcolor("red")

    # Draw the apple
    t.begin_fill()
    t.circle(size)
    t.end_fill()

    # Draw a stem
    t.penup()
    t.goto(position[0], position[1] - size)  # Move to the bottom of the apple
    t.pendown()
    t.color("brown")
    t.pensize(2)
    t.left(90)
    t.forward(size * 0.8)  # Adjust the length of the stem

def drawNode(t, size, level):
    if level < 1:
        return
    else:
        drawSquare(t, size)

        leftSize = size * math.sqrt(3) / 2
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(150)
        t.forward(leftSize)
        t.left(90)
        drawNode(t, leftSize, level - 1)
        rightSize = size / 2
        t.right(180)
        t.forward(rightSize)
        t.left(90)
        drawNode(t, rightSize, level - 1)
        t.left(60)
        t.back(size)

def drawCaption(t, position, text):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color("dark red")
    t.write(text, align="left", font=("Arial", 8, "normal"))

def drawScene():
    alan.penup()
    alan.goto(90, -150)
    alan.left(90)
    alan.pendown()

    drawNode(alan, 58, 14)

    # Calculate the position for the higher apple
    apple_size = 10
    top_position = alan.position()
    top_position = (top_position[0], top_position[1] + (58 * 1.5) + 100)  # Adjust based on the tree size and additional height

    # Draw the higher apple
    drawApple(alan, top_position, apple_size)

    # Calculate the position for the caption to the right
    caption_position = (top_position[0] + 40, top_position[1] + 20)  # Adjust the horizontal position of the caption
    drawCaption(alan, caption_position, "You're the apple of my eye ;)")

    alan.hideturtle()

# Turn off animation
screen.tracer(0)
drawScene()
screen.update()
screen.exitonclick()
