from graphics import *
import time
def line(x1,y1,x2,y2):
    win = GraphWin("Line Bresenham", 640, 480)
    dx=x2-x1
    dy=y2-y1
    D=2*dy-dx
    y=y1
    for x in range(x1,x2):
        print(D)
        win.plotPixel(x,y,"black")
        if D>0:
            y=y+1
            D=D+2*(dy-dx)
        else:
            D=D+2*dy
line(100,100,300,400)
