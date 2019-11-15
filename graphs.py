import matplotlib.pyplot as plt
import math
import numpy as np


x = np.arange(0,6*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure('Sin and Cos')
plt.clf()
plt.plot(x,y1,'g-',label = "Sin(X)",linewidth = 1.0)
plt.plot(x,y2,'r--',label = "Cos(X)",linewidth = 1.0)
plt.legend(loc='best')
plt.title('Sin(x) & Cos(x)')
plt.xlabel('X')
plt.ylabel('Y')
#plt.ylim(0,1.5)
plt.show()


plt.figure("Sin x and Cos X")
plt.clf()
plt.subplot(211)
plt.plot(x,y1,'g-',label = "Sin(X)",linewidth = 1.0)
plt.title('Sin(x)')
plt.legend(loc='upper right')
plt.subplot(212)
plt.plot(x,y2,'r--',label = "Cos(X)",linewidth = 1.0)
plt.legend(loc='upper right')
plt.title('Cos(x)')
plt.xlabel('X')
plt.ylabel('Y')
#plt.ylim(0,1.5)
plt.show()
