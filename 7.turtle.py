import turtle
import colorsys
turtle.Screen().bgcolor('black')
t=turtle.pen()
h=0
t.speed(0)
turtle.tracer(50)
for i in range(200):
    t.width(i/100+1)
    c=colorsys.hsv_to_rgb(h,1,0.8)
    t.pencolor(c)
    t.left(1000)
    t.p

