import sys

import numpy as np
import matplotlib.pyplot as plt

from math import cos, sin, pi

plt.ioff()

x0 = 0
y0 = 0
w = 1 # width of robot
dt = 0.01

x_traj = []
y_traj = []
theta = 0
x = 0
y = 0

if __name__ == "__main__":

    velocities = []

    with open("wheel_velocities.txt", "r") as file:
        for line in file:
            data = line.rstrip().split(' ')
            data[0] = float(data[0])
            data[1] = float(data[1])
            velocities.append(data)


for vel in velocities:
    omg = vel[1] - vel[0]
    v = (vel[1] + vel[0]) / 2
    theta = theta + omg*dt
    vx = v*cos(theta)
    vy = v*sin(theta)
    x = x + vx*dt
    y = y + vx*dt
    
    x_traj.append(x)
    y_traj.append(y)
	
plt.ion()
            
for i in range(len(x_traj) - 1):
    plt.cla()
    plt.plot(x_traj[:i], y_traj[:i], 'r--')
    plt.arrow(x_traj[i], y_traj[i], x_traj[i+1]-x_traj[i], y_traj[i+1]-y_traj[i], width=0.05, color='k')
    plt.show()
    plt.pause(dt)