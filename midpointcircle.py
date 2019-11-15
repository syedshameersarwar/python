from graphics import *
import time
from math import *
win = GraphWin("Mid point circle", 640, 480)

def drawsympoints(a,b,x,y):
	time.sleep(0.3)
	win.plotPixel( x+a, y+b, "black")
	win.plotPixel( y+a, x+b, "black")
	win.plotPixel( y+a,-x+b, "black")
	win.plotPixel( x+a,-y+b, "black")
	win.plotPixel(-x+a,-y+b, "black")
	win.plotPixel(-y+a,-x+b, "black")
	win.plotPixel(-y+a, x+b, "black")
	win.plotPixel(-x+a, y+b, "black")

def circle(a,b,r):
	x=0
	y=r
	h=1-r
	while(y>x):
		drawsympoints(a,b,x,y)
		print(x,y)
		if(h<0):
			h= h+2*x+3
		else:
			z=x-y
			h=h+2*z+5
			y=y-1
		x=x+1
	
		#drawsympoints(a,b,x,y)


circle(10,100,100)
