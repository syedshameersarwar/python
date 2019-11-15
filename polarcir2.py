from graphics import *
import time
from numpy import *
import math
win=GraphWin("circle polar 2",640,480)
def drawsympoints(a,b,x,y):
	time.sleep(0.3)
	win.plotPixel( x+a, y+b, "yellow")
	win.plotPixel( y+a, x+b, "green")
	win.plotPixel( y+a,-x+b, "red")
	win.plotPixel( x+a,-y+b, "blue")
	win.plotPixel(-x+a,-y+b, "black")
	win.plotPixel(-y+a,-x+b, "green")
	win.plotPixel(-y+a, x+b, "black")
	win.plotPixel(-x+a, y+b, "green")
	
def circle(a,b,r):
	for q in arange(0,(math.pi/4),1/r):
		x=r*math.cos(q)
		y=r*math.sin(q)
		drawsympoints(a,b,x,y)
		
circle(100,100,100)
