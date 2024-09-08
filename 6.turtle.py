# import turtle as t
# import colorsys
# t.bgcolor("black")
# t.tracer(677)
# t.pensize(8)
# def draw():
#     h=0.9
#     n=98
#     for i in range(679):
#         c=colorsys.hsv_to_rgb(h,1,0.9)
#         h+=1/n
#         t.color(c)
#         t.rt(i)
#         t.up()
#         t.goto(0,1)
#         t.down()
#         t.goto(0,0)
#         t.down()
#         t.fillcolor("black")
#         t.begin_fill()
#         t.circle(i,98)
#         t.lt(i)
#         t.end_fill()
#     draw()
#     t.done()


# t=int(input())
# while t>0:
#     t-=1
#     n=int(input())
#     s=input()
#     while(s.count('000')):
#         s=s.replace('000','0')
#     p='+'in s
#     q='-'in s
#     if( p|q):
#         print(s.count('-0+')+s.count('+0-'))
#     else:
#         print(n)

