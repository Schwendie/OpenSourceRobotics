from my_robots import NLinkArm
import matplotlib.pyplot as plt
from math import pi, cos, sin, sqrt, atan2, acos

arm = NLinkArm([2,2], [15, 15])

def ang_diff(theta_goal, theta):
    return (theta_goal - theta + pi)%(2*pi) - pi

# Pure pursuit end effector then update_points
def pure_pursuit(x_wp, y_wp):
    zeros = lambda n: [0 for _ in range(n)]
    dx, dy, x, y, d, theta, theta_goal, v, vx, vy, omg, t = zeros(12)
    x_g = x_wp
    y_g = y_wp
    l1 = arm.length[0]
    l2 = arm.length[1]
    dt = 0.001
    K_p = 5
    K_h = 30
    T = 5

    while t < T:
        dx = x_g - x
        dy = y_g - y
        d = sqrt(dx**2 + dy**2)
        theta_goal = atan2(dy, dx)
        v = K_p * d
        vx = v*cos(theta)
        vy = v*sin(theta)
        x = x + vx*dt
        y = y + vy*dt
        omg = K_h * ang_diff(theta_goal, theta)
        theta = theta + omg*dt

        t = t + dt

        # Inverse kinematics
        theta2 = acos((x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2))
        theta1 = atan2(y, x) - atan2((l2*sin(theta2)), (l1+l2*sin(theta2)))

        theta_list = [theta1, theta2]
        arm.update_joints(theta_list)
        #plt.cla()
        arm.plot()

while True:
    pure_pursuit(arm.goal[0], arm.goal[1])