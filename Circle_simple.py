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

def getRound(n):
    return (math.ceil(n) if (n%1)>0.5 else math.floor(n))

def Circle(Xc,Yc,r):
    for x in range(Xc-r,Xc+r+1):
        y = getRound(Yc+math.sqrt(r**2 -(x-Xc)**2))
        drawPixel(x,y)
        y = getRound(Yc-math.sqrt(r**2 -(x-Xc)**2))
        drawPixel(x,y)

if __name__=='__main__':
    screen = pygame_intializer()
    Circle(640,390,110)
