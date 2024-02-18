import turtle
import math

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.tracer(0)
alan = turtle.Turtle()
alan.shape("turtle")
alan.color("green")
alan.fillcolor("tan")
alan.speed(0)

def drawSquare(t, size):
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def drawApple(t, position, size):
    t.color("red")
    t.fillcolor("red")

    # Draw the apple
    t.penup()
    t.goto(position[0], position[1] - 8)  # Adjust the vertical position of the apple
    t.pendown()
    t.begin_fill()
    t.circle(size)
    t.end_fill()

def drawNode(t, size, level):
    if level < 1:
        return
    else:
        drawSquare(t, size)

        leftSize = size * math.sqrt(3) / 2
        t.forward(size)
        t.right(90)
        t.forward(size)
        t.left(150)
        t.forward(leftSize)
        t.right(90)
        drawNode(t, leftSize, level - 1)

        rightSize = size / 2
        t.left(180)
        t.forward(rightSize)
        t.right(90)
        drawNode(t, rightSize, level - 1)
        t.right(60)
        t.back(size)

def drawScene():
    alan.penup()
    alan.goto(90, -150)
    alan.left(90)
    alan.pendown()

    drawNode(alan, 80, 8)

    alan.hideturtle()

    # Calculate the position for the apple to the right
    apple_position = (-20, 40)  # Adjust the horizontal position of the apple
    # Draw an apple at the calculated position
    drawApple(alan, apple_position, 20)

    # Write "Cherry on top" below the drawn apple
    alan.penup()
    alan.goto(apple_position[0], apple_position[1] - 20)  # Adjust the vertical position of the text
    alan.pendown()
    alan.color("black")
    alan.write("Cherry on top", align="center", font=("Arial", 12, "normal"))

    # Write "get it?" at the bottom right of the entire screen
    alan.penup()
    alan.goto(screen.window_width() / 2 - 60, -screen.window_height() / 2 + 20)
    alan.pendown()
    alan.write("get it?", align="right", font=("Arial", 8, "normal"))

    screen.update()

drawScene()

screen.exitonclick()
