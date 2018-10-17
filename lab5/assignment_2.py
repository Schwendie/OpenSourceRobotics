from my_robots import NLinkArm
import matplotlib.pyplot as plt
from math import pi, cos, sin, sqrt, atan2, acos

#plt.ion()

arm = NLinkArm()
dt = 0.01
K_h = 30
theta1, theta2 = 0, 0
theta_goal1, theta_goal2 = 0, 0
l1 = arm.length[0]
l2 = arm.length[1]

def ang_diff(theta_goal, theta):
    return (theta_goal - theta + pi)%(2*pi) - pi

while True:
    x_g = arm.goal[0]
    y_g = arm.goal[1]

    print(x_g)
    print(y_g)

    print("I got here")

    if (sqrt(x_g**2 + y_g**2) > (l1 + l2)):
        d = sqrt(x_g**2 + y_g**2)
        x_g = (x_g * 2) / d
        y_g = (y_g * 2) / d
    try:
        theta_goal2 = acos((x_g**2 + y_g**2 - l1**2 - l2**2)/(2*l1*l2))
        theta_goal1 = atan2(y_g, x_g) - atan2((l2*sin(theta_goal2)), (l1+l2*cos(theta_goal2)))
    except:
        theta_goal1 = 0
        theta_goal2 = 0

    if theta_goal1 < 0:
        theta_goal2 *= -1
        theta_goal1 = atan2(y_g, x_g) - atan2((l2*sin(theta_goal2)), (l1+l2*cos(theta_goal2)))

    omega1 = K_h * ang_diff(theta_goal1, theta1)
    omega2 = K_h * ang_diff(theta_goal2, theta2)

    theta1 += omega1*dt
    theta2 += omega2*dt

    arm.update_joints([theta1, theta2])
    arm.plot()

"""
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
        print(theta_list)
        arm.update_joints(theta_list)
        #plt.cla()
        arm.plot()


pure_pursuit(arm.goal[0], arm.goal[1])"""