import numpy as np
import matplotlib.pyplot as plt

from math import cos, sin, sqrt, pi, atan2, isclose

class Vehicle:

    obstacles = []

    def __init__(self, x=0, y=0, theta=0, length=1, width=0.5):
        self.p1 = np.array([length/2, 0, 1]).T         # tip of triangle
        self.p2 = np.array([-length/2, width/2, 1]).T  # top base of triangle
        self.p3 = np.array([-length/2, -width/2, 1]).T # bottom base of triangle

        plt.ion()

        self.goal = [x, y]

        fig = plt.figure()
        fig.canvas.mpl_connect('button_press_event', self.click)

        self.update_pose(x, y, theta)

    def update_pose(self, x=0, y=0, theta=0):
        self.x = x
        self.y = y
        self.theta = theta

    def transformation_matrix(self):
        return np.array(
            [[cos(self.theta), -sin(self.theta), self.x],
             [sin(self.theta), cos(self.theta), self.y]]
             )

    def add_obstacles(self, *obstacle):
        for obs in obstacle:
            self.obstacles.append(obs)

    def remove_obstacles(self, *obstacle):
        try:
            for obs in obstacle:
                self.obstacles.remove(obs)
        except ValueError:
            print("No obstacle matching that description found.  Please remove one of these instead:")
            print(self.obstacles)

    def plot(self, goal=[], x_lim=(-10,10), y_lim=(-10,10)):
        T = self.transformation_matrix()

        p1_r = np.matmul(T, self.p1)
        p2_r = np.matmul(T, self.p2)
        p3_r = np.matmul(T, self.p3)

        plt.cla()
        plt.plot([p1_r[0], p2_r[0]], [p1_r[1], p2_r[1]], 'k-')
        plt.plot([p2_r[0], p3_r[0]], [p2_r[1], p3_r[1]], 'k-')
        plt.plot([p3_r[0], p1_r[0]], [p3_r[1], p1_r[1]], 'k-')

        if goal == []:
            plt.plot(self.goal[0], self.goal[1], c='g', marker='*')
        else:
            plt.plot(goal[0], goal[1], c='g', marker='*')

        for obs in self.obstacles:
            circle = plt.Circle((obs[0], obs[1]), radius=0.5*obs[2], fc='r')
            plt.gca().add_patch(circle)

        plt.xlim(x_lim)
        plt.ylim(y_lim)

        plt.show()
        plt.pause(0.001)

    def click(self, event):
        self.goal = [event.xdata, event.ydata]

    def place_goal(self, x_goal, y_goal):
        self.goal = [x_goal, y_goal]

    def ang_diff(self, theta1, theta2):
        return (theta1 - theta2 + pi)%(2*pi) - pi

    """
    def pure_pursuit(self, x_goal, y_goal):
        zeros = lambda n: [0 for _ in range(n)]
        dx, dy, d, v, vx, vy, theta_goal, omg = zeros(8)
        x, y, theta = self.x, self.y, self.theta
        K_p, K_h, dt = 10, 30, 0.01
        #while not (isclose(x, x_goal, rel_tol=1e-2)) or not (isclose(y, y_goal, rel_tol=1e-2)):
        while x < x_goal-0.5:
            dx = x_goal - x
            dy = y_goal - y
            d = sqrt(dx**2 + dy**2)
            v = K_p * d
            theta_goal = atan2(dy, dx)
            vx = v * cos(theta)
            vy = v * sin(theta)
            x = x + vx*dt
            y = y + vy*dt
            omg = K_h * self.ang_diff(theta_goal, theta)
            theta = theta + omg*dt

            self.update_pose(x, y, theta)
            """
