import turtle
turtle.color("black")
turtle.speed(500)

i = 0
while i <= 36:
    for j in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.left(10)
    i += 1
turtle.exitonclick()