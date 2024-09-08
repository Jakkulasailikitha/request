import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(567)
def draw():
    h=0
    n=10
    for i in range(150):
        c = colorsys.hsv_to_rgb(h,1,1)
        h+=1/n
        t.pencolor("black")
        t.pensize(1)
        t.rt(89)
        t.circle(i,159,steps=1)
        t.fillcolor(c)
        t.begin_fill()
        t.rt(208)
        t.bk(20)
        t.circle(i,296,steps=1)
        t.end_fill()
        for j in range(26):
            t.penup()
            t.goto(0,0)
            t.down()
            t.color(c)
            t.rt(19)
            t.circle(i,346,steps=1)
            t.rt(80)
draw()
t.done           