from turtle import Turtle, Screen
import random

is_race_on = False
# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win, choose a color")
colors: list[str] = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create the turtles
for turtle_index in range(0, 6):
    racer = Turtle(shape = "turtle")
    racer.penup()
    racer.color(colors[turtle_index])
    racer.goto(x=-230, y = y_positions[turtle_index])
    all_turtles.append(racer)
    #my_turtle.speed(0)  # Fastest speed

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost - the {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward((rand_distance))


# Keep the window open
screen.exitonclick()

"""
# Define functions for direction and movement
def go_north():
    my_turtle.setheading(90)
    my_turtle.forward(20)

def go_south():
    my_turtle.setheading(270)
    my_turtle.forward(20)

def go_east():
    my_turtle.setheading(0)
    my_turtle.forward(20)

def go_west():
    my_turtle.setheading(180)
    my_turtle.forward(20)

# Bind the functions to arrow keys
screen.onkey(go_north, "Up")
screen.onkey(go_south, "Down")
screen.onkey(go_east, "Right")
screen.onkey(go_west, "Left")

# Start listening for key presses
screen.listen()

# Keep the window open
turtle.done()





from turtle import Turtle, Screen
import keyboard


pen = Turtle()
screen = Screen()


def go_forward():
    pen.forward(10)
def go_right():
    pen.setheading(90)
    pen.forward(10)
def go_left():
    pen.setheading(180)
    pen.forward(10)

def go_up():
    pen.setheading(0)
    pen.forward(10)


def go_down():
    pen.setheading(270)
    pen.forward(10)


screen.listen()
screen.onkey(key="space", fun=go_forward)
#screen.onkey(key="right", fun=go_right)
screen.exitonclick()
"""