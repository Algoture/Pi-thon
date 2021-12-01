import turtle
loadWindow = turtle.Screen()
turtle.speed(13)
turtle.bgcolor("yellow")
turtle.color("red")
 
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
 
turtle.exitonclick()