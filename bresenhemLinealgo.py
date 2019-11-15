import pygame
import pygame.gfxdraw


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


def drawLine(x1,y1,x2,y2):
    x,y = x1,y1
    dy = y2-y1
    dx = x2-x1
    dS = 2*dy
    dT = 2*(dy-dx)
    d = 2*dy-dx
    drawPixel(x,y)
    while x<=x2:
        x+=1
        if d<=0:
            d += dS
        else:
            y+=1
            d += dT
        drawPixel(x,y)

if __name__=='__main__':
    screen = pygame_intializer()
    drawLine(100,100,300,400)
