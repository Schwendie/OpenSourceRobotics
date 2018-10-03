import numpy as np
import matplotlib.pyplot as plt

from math import cos, sin, sqrt, pi, atan2, isclose, radians

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

class NLinkArm:

    end_eff = (0,0)

    def __init__(self, link_lengths, joint_angles):
        if (len(link_lengths) != len(joint_angles)):
            print("The lengths of the two lists don't match")
        self.length = link_lengths
        for i in range(0, len(joint_angles)):
            joint_angles[i] = radians(joint_angles[i])
        self.thetas = joint_angles

        self.points = []
        self.x = []
        self.y = []

        self.update_points()

        self.goal = self.end_eff

        fig = plt.figure()
        fig.canvas.mpl_connect('button_press_event', self.click)

    def click(self, event):
        self.goal = [event.xdata, event.ydata]
        plt.cla()
        self.plot()

    def update_joints(self, thetas):
        self.thetas = thetas
        self.update_points()

    def update_points(self):
        self.points = []
        self.points.append((0, 0))
        self.x = []
        self.x.append(0)
        self.y = []
        self.y.append(0)

        n = len(self.thetas)

        for i in range(0, n):
            p_x = self.points[i][0] + self.length[i] * cos(sum(self.thetas[:i+1]))
            print(p_x)
            self.x.append(p_x)
            p_y = self.points[i][1] + self.length[i] * sin(sum(self.thetas[:i+1]))
            self.y.append(p_y)
            self.points.append((p_x, p_y))

        self.end_eff = (self.points[n])

    def plot(self, obstacles=[], goal=[], xlims=(-10,10), ylims=(-10,10)):
        plt.plot(self.x, self.y, 'bo-')
        
        if goal == []:
            plt.plot(self.goal[0], self.goal[1], c='g', marker='*')
        else:
            plt.plot(goal[0], goal[1], c='g', marker='*')

        for obs in obstacles:
            circle = plt.Circle((obs[0], obs[1]), radius=0.5*obs[2], fc='r')
            plt.gca().add_patch(circle)

        plt.xlim(xlims)
        plt.ylim(ylims)

        plt.show()
        plt.pause(0.001)


