import sys

from math import pi, cos, sin, sqrt, atan2
from my_robots import Vehicle


def ang_diff(thetaGoal, theta):
    return (thetaGoal - theta + pi)%(2*pi) - pi

def pureP(x_wp, y_wp):
    dt = 0.01
    delx = 0.1
    K_p = 5
    K_h =30
    x = 0
    y = 0
    theta = 0
    m = (y_wp)/(x_wp)
    x_goal = 0
    check = True
    i = 0
    d = 0
    d_wp = 0
    y_goal = 0
    

    while d > 0.1 or check:

        if d_wp > 0.1:
            x_goal = x_goal + delx
            y_goal = m * (x_goal - x_wp) + y_wp
            goal = [x_goal, y_goal]

        dx = x_goal - x
        dy = y_goal - y
        dx_wp = x_wp - x_goal
        dy_wp = y_wp - y_goal
        d = sqrt(dx**2 + dy**2)
        d_wp = sqrt(dx_wp**2 + dy_wp**2)
        v = K_p * d
        theta_goal = atan2(dy, dx)
        vx = v * cos(theta)
        vy = v * sin(theta)
        x = x + vx*dt
        y = y + vy*dt
        omg = K_h * ang_diff(theta_goal, theta)
        theta = theta + omg*dt

        ve.update_pose(x, y, theta)
        ve.plot(goal=[x_goal,y_goal], x_lim=[-1,21], y_lim=[-10,10])

        if d_wp < 0.2:
            y_wp = 0
            x_wp = 20
            m = (y_wp - y_goal)/(x_wp - x_goal)


        i += 1
        if (i == 30):
            check = False
            

if __name__ == "__main__":
    try:
        x_wp = float(sys.argv[1])
        y_wp = float(sys.argv[2])
    except Exception as e:
        x_wp = 5
        y_wp = 5
    
    ve = Vehicle()
    ve.add_obstacles([10,0,5])
    pureP(x_wp, y_wp)
