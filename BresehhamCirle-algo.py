from graphics import *
import math
import numpy as np


def drawPixel(x,y):
    global screen
    screen.plotPixel(int(x),int(y),"red")
    

def BresenhamCircle(Xc,Yc,r):
    x = 0
    y  = r
    d=3- (2*r)
    while y > x:
        drawSymmetricPoints(Xc,Yc,x,y)
        if d <0:
            d=d + 4*x +6
        else:
            d=d+ 4*(x-y) +10
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
    BresenhamCircle(500,200,100)
    
