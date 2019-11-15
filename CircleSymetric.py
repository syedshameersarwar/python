import pygame
import pygame.gfxdraw
import math


def pygame_intializer():
    pygame.init()
    screen = pygame.display.set_mode((1280,780))
    white = (255,255,255)
    screen.fill(white)
    pygame.display.update()
    return screen

def drawPixel(x,y):
    global screen
    pygame.gfxdraw.pixel(screen,int(x),int(y),(0,0,255))
    pygame.display.update()



def CircleSymmetric(Xc,Yc,r):
    x = r
    y  = 0
    theta = 0.0
    dtheta = 1.0/r
    drawSymmetricPoints(Xc,Yc,x,y)
    while x>y: #until x==y i.e at 45 degree
        theta += dtheta
        x = round(r*math.cos(theta),1)
        y = round(r*math.sin(theta),1)
        drawSymmetricPoints(Xc,Yc,x,y)
        

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
    screen = pygame_intializer()
    CircleSymmetric(300,300,100)
    
