"""import sys

import numpy as np
import matplotlib.pyplot as plt

from math import cos, sin, pi

plt.ion()

x0 = 0
y0 = 0
w = 1 # width of robot
dt = 0.01

x_traj = []
y_traj = []
theta = 0
x = 0
y = 0
vx = 0
vy = 0
omg = 0
v = 0
vs = []
omega = []
thetas = []

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
    omega.append(omg)
    vs.append(v)

for item in omega:
    theta += item*dt
    thetas.append(theta)

for i in range(0, 2050):
    vx = vs[i]*cos(thetas[i])
    vy = vs[i]*sin(thetas[i])
    x += vx*dt
    y += vx*dt
    
    x_traj.append(x)
    y_traj.append(y)


print(x, y)
            
for i in range(len(omega) - 1):
    plt.cla()
    plt.plot(x_traj[:i], y_traj[:i], 'r--')
    plt.arrow(x_traj[i], y_traj[i], x_traj[i+1]-x_traj[i], y_traj[i+1]-y_traj[i], width=0.05, color='k')
    plt.show()
    plt.pause(dt)"""

import numpy as np
import matplotlib.pyplot as plt

from math import pi, cos, sin, ceil

velocities = []
v_mag = []
omega = []
points = []
x_data = []
y_data = []
theta_list = []
theta = 0
xPos = 0
yPos = 0
v_x = 0
v_y = 0
dt = 0.01

plt.ion()

with open("wheel_velocities.txt", "r") as file:
    for line in file:
        data = line.rstrip().split(' ')
        data[1] = float(data[1])
        data[0] = float(data[0])
        velocities.append(data)
        
for point in velocities:
    omega.append(point[1] - point[0])
    v_mag.append((point[0] + point[1])/2)
    
for point in omega:
    theta += point*dt
    theta_list.append(theta)
    
for i in range(0, 2050):
    v_x = v_mag[i]*cos(theta_list[i])
    v_y = v_mag[i]*sin(theta_list[i])
    xPos += v_x*dt
    yPos += v_y*dt
    x_data.append(xPos)
    y_data.append(yPos)
    
print(xPos, yPos)

for i in range(len(omega)-1):
    plt.cla()
    plt.plot(x_data[:i], y_data[:i], 'r--')
    
    plt.arrow(x_data[i], y_data[i], x_data[i+1]-x_data[i], y_data[i+1]-y_data[i], width=0.05, color='k')
    plt.show()
    plt.pause(dt)
