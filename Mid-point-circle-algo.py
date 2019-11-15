from graphics import *
import math
import numpy as np


def drawPixel(x,y):
    global screen
    screen.plotPixel(int(x),int(y),"red")
    

def MidPointCircle(Xc,Yc,r):
    x = 0
    y  = r
    h= 1 - r
    while y > x:
        drawSymmetricPoints(Xc,Yc,x,y)
        if h <0:
            h=h + 2*x +3
        else:
            h=h+ 2*(x-y) +5
            y=y-1
        x=x+1

def drawSymmetricPoints(Xc,Yc,x,y):
    drawPixel(x+Xc,y+Yc)
    drawPixel(y+Xc,x+Yc)
    drawPixel(y+Xc,-x+Yc)
    drawPixel(x+Xc,-y+Yc)
    drawPixel(-x+Xc,-y+Yc)
    drawPixel(-y+Xc,-x+Yc)
    drawPixel(-y+Xc,x+Yc)
    drawPixel(-x+Xc,y+Yc)

if __name__=='__main__':
    screen = GraphWin("Circle Symmetric",800,800)
    MidPointCircle(500,200,100)
    
