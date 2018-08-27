import sys

import numpy as np
import matplotlib.pyplot as plt

from math import cos, sin, pi

plt.ion()

x0 = 0
y0 = 0
w = 1 # width of robot
dt = 0.01

x_traj = []
theta = 0

for vel in velocities:
    omg = vel[0] - vel[1]
    v = omg / 2
    theta = theta + omg*dt

if __name__ == "__main__":

    velocities = []

    with open("wheel_velocities.txt", "r") as file:
        for line in file:
            data = line.rstrip().split(' ')
            data[0] = float(data[0])
            data[1] = float(data[1])
            velocities.append(data)