import sys
import matplotlib.pyplot as plt
import numpy as np

from math import cos, sin, pi, sqrt, atan2, isclose
from my_robots import Vehicle
from assignment_3 import TrajectoryGenerator

def pureP(xWp, yWp):
    zeros = lambda n: [0 for _ in range(n)]
    x, y, theta, x_goal, y_goal, T = zeros(6)
    K_p, K_h, dt = 10, 30, 0.01
    check = True
    i = 0
    traj.update_states(p_i=[0,0,0], p_f=[xWp, yWp, 0], v_i=[0,0,0], v_f=[-1,0,0])
    xCo, yCo, zCo = traj.solve(time=10)
    q = 0
    dWp = 0
    d = 0

    #loops until vehicle reaches goal
    #while d > 0.1 or check:
    while not (isclose(x, x_goal, rel_tol=1e-5)) or not (isclose(y, y_goal, rel_tol=1e-5)) or check:

        #point stops moving when it reaches endpoint
        if dWp > 0.1:
            x_goal = xCo[0] * T**5 + xCo[1] * T**4 + xCo[2] * T**3 + xCo[3] * T**2 + xCo[4] * T + xCo[5]
            y_goal = yCo[0] * T**5 + yCo[1] * T**4 + yCo[2] * T**3 + yCo[3] * T**2 + yCo[4] * T + yCo[5]
            goal = [x_goal, y_goal]
            T += 0.1

        #math for pure pursuit
        dx = x_goal - x
        dy = y_goal - y
        delXwp = xWp - x_goal
        delYwp = yWp - y_goal
        dWp = sqrt(delXwp**2 + delYwp**2)


        d = sqrt(dx**2 + dy**2)
        

        theta_goal = atan2(dy, dx)
        omega = K_h * v.ang_diff(theta_goal, theta)
        
        vMag = K_p * d
        vx = vMag * cos(theta)
        vy = vMag * sin(theta)

        x = x + vx*dt
        y = y + vy*dt
        theta += omega * dt
        v.place_goal(x_goal, y_goal)
        v.update_pose(x, y, theta)
        
        #v.plot()

        #updates wp of point
        if dWp < 0.1 and q == 0:

            traj.update_states(p_i=[xWp, yWp, 0], p_f=[10, 0, 0], v_i=[-1,0,0], v_f=[-1,0,0])
            xCo, yCo, zCo = traj.solve(time=10)
            q = 1
            T = 0
            xWp = 10
            yWp = 0
            dWp = sqrt(delXwp**2 + delYwp**2)


        #prevents car from reaching goal early on
        i += 1
        if (i == 30):
            check = False


if __name__ == "__main__":
    x_wp = float(sys.argv[1])
    y_wp = float(sys.argv[2])
    v = Vehicle()
    v.add_obstacles([5,0,1])
    traj = TrajectoryGenerator()
    pureP(x_wp, y_wp)
    