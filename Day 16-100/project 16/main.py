from turtle import Turtle, Screen

maeve = Turtle()
print(maeve)
maeve.shape("turtle")
maeve.showturtle()
maeve.color("DeepPink4")
maeve.shapesize(5, 5, 2)
maeve.forward(100)

view_screen = Screen()
print(view_screen.canvheight)
view_screen.exitonclick()
