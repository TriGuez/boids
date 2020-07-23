from math import pi
from boid import *
import numpy as np
import matplotlib.pyplot as plt



B1 = boid(63,22,1,(120 * pi /180))
B1_x = []
B1_y = []

i = 0
while(i<100000):
    B1.boidBehave()
    B1_x.append(B1.get_x())
    B1_y.append(B1.get_y())

    i = i+1

x = np.array([0, 100, 100, 0, 0])
y = np.array([0, 0, 100, 100, 0])
plt.plot(x, y, linewidth = 4, color = 'red',label="Wall")
"""
plt.xlim(-10, 110)
plt.ylim(-10, 110)
"""
#plt.plot(B1_x,B1_y,"-->",label="Boid")

plt.plot(B1_x,B1_y,label="Boid")
plt.legend()
plt.grid()
plt.show()
