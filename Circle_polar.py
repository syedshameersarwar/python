import pygame
import pygame.gfxdraw
import math
import numpy as np

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

def getRound(n):
    return (math.ceil(n) if (n%1)>0.5 else math.floor(n))


def CirclePolar(Xc,Yc,r):
    #resembles sir version of algorithm
    for theta in np.arange(0.0,2*math.pi,1/r):
        x = Xc+r*math.cos(theta)
        y = Yc+r*math.sin(theta)
        drawPixel(getRound(x),getRound(y))
    ''' more accurate version
    for theta in range(0,360):
        x = Xc + r*math.cos(theta*math.pi/180)
        y = Yc + r*math.sin(theta*math.pi/180)
        drawPixel(x,y)
    '''

if __name__=='__main__':
    screen = pygame_intializer()
    CirclePolar(300,300,100)
