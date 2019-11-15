import pygame
import sys
import math
from line_2_differential import *

def getRound(n):
    return (math.ceil(n) if (n%1)>0.5 else math.floor(n))

def calculateIntercept(p1,p2):
    return (((p2[1]-p1[1])*( - p1[0]))/(p2[0]-p1[0]))+p1[1]

def drawPixel(x,y):
    global screen
    pygame.gfxdraw.pixel(screen,int(x),int(y),(0,0,255))
    pygame.display.update()

def drawline(p1,p2):
    b = calculateIntercept(p1,p2)
    slope = (p2[1]-p1[1])/(p2[0]-p1[0])
    X = p1[0]
    Y = p1[1]
    if slope < 1 :
        while X <= p2[0]:
            drawPixel(X,getRound(Y))
            X+=1
            Y = slope*X + b
    else:
        while Y<= p2[1]:
            drawPixel(getRound(X),Y)
            Y+=1
            X = (Y-b)/slope
    
    

if __name__ == '__main__':
    screen = pygame_intializer()
    drawline((100,10),(300,400))
        
            
    
    
    
