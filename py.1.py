#python turtle code 10 
#beautiful design in python
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.width(3)
t.speed(25)
col=('orange','white','green')
for i in range(500):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)