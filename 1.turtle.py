import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
n=80
h=0
for i in range(50):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(155)
    t.forward(i)
    for j in range(3):
        t.left(5)
        t.forward(i)