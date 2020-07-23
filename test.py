from math import pi
from boid import *
import matplotlib.pyplot as plt



B1 = boid(1,1,1,(120 * pi /180))
B1_x = []
B1_y = []

i = 0
while(i<100):
    B1.boidMove()
    B1_x.append(B1.get_x())
    B1_y.append(B1.get_y())
    B1.boidPrint()

    B1.boidUpdate()

    i = i+1

plt.plot(B1_x,B1_y)
plt.show()
