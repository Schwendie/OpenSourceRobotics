from math import cos, sin, pi, sqrt, atan2
from assignment_1 import Vehicle

x = 0
y = 0
x_goal = 0
y_goal = 0
dx = 0
dy = 0
d = 0
v = 0
v_x = 0
v_y = 0
theta = 0
theta_goal = 0
omg = 0
K_p = 10
K_h = 30
dt = 0.01
ve = Vehicle()

def ang_diff(theta1, theta2):
    return (theta1 - theta2 + pi)%(2*pi) - pi

while True:
    x_goal = ve.goal[0]
    y_goal = ve.goal[1]
    dx = x_goal - x
    dy = y_goal - y
    d = sqrt(dx**2 + dy**2)
    v = K_p * d
    theta_goal = atan2(dy, dx)
    v_x = v * cos(theta)
    v_y = v * sin(theta)
    x = x + v_x*dt
    y = y + v_y*dt
    omg = K_h * ang_diff(theta_goal, theta)
    theta = theta + omg*dt

    ve.update_pose(x, y, theta)