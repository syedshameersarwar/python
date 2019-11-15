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



def drawLine(p1,p2):
    X,Y = p1[0],p1[1]
    dy = abs(p2[1]-p1[1])
    dx = abs(p2[0]-p1[0])
    if dx >= dy:
        step = dx
    else :
        step = dy
    xIncrement = dx/step
    yIncrement = dy/step
    for i in range(step+1):
        drawPixel(X,Y)
        X += xIncrement
        Y += yIncrement

if __name__ == '__main__':
    screen = pygame_intializer()
    drawLine((100,100),(300,400))
    
