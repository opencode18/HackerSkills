import math
import turtle

ans = turtle.Screen()
ans.bgcolor("lightblue")
fred = turtle.Turtle()
for angle in range(360):
    y = math.sin(math.radians(angle))
    fred.goto(angle, y * 80)

ans.exitonclick()
