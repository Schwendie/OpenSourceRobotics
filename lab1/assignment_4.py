import sys

import numpy as np
import matplotlib.pyplot as plt

from math import cos, sin, pi

plt.ion()

def rotation_matrix(theta):
	return np.array(
		[[cos(theta), -sin(theta)],
		 [sin(theta), cos(theta)]]
    )

def plot_data(points, step_size):
    theta = 0
    r_points = 4*[0]
    while True:
        plt.cla()
        R = rotation_matrix(theta)
        for i in range(len(points)):
            r_points[i] = np.matmul(R, points[i].T)
            
        plt.plot([r_points[0][0], r_points[1][0]], [r_points[0][1], r_points[1][1]], 'g')
        plt.plot([r_points[1][0], r_points[2][0]], [r_points[1][1], r_points[2][1]], 'r')
        plt.plot([r_points[2][0], r_points[3][0]], [r_points[2][1], r_points[3][1]], 'b')
        plt.plot([r_points[3][0], r_points[0][0]], [r_points[3][1], r_points[0][1]], 'y')
        plt.xlim(-10,10)
        plt.ylim(-10,10)
        plt.show()
        plt.pause(0.01)
        theta+=step_size

if __name__ == "__main__":
    try:
        step_size = float(sys.argv[1])
    except:
        print("Using default step size 0.1")
        step_size = 0.1

    points = [[5,5], [-5,5], [-5,-5], [5,-5]]

    plot_data(np.array(points), step_size)
