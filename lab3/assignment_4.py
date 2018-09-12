import sys
import matplotlib.pyplot as plt
import numpy as np

from math import cos, sin, pi, sqrt, atan2
from my_robots import Vehicle
from assignment_3 import TrajectoryGenerator

def ang_diff(theta_goal, theta):
    return (theta_goal - theta + pi)%(2*pi) - pi

def pureP(xWp, yWp):

    dt = 0.01
    k1 = 10
    k2 =30
    x = 0
    y = 0
    theta = 0
    xGoal = 0
    yGoal = 0
    check = True
    i = 0
    traj.update_states(p_i=[0,0,0], p_f=[xWp, yWp, 0])
    xCo, yCo, zCo = traj.solve()
    time = 0
    q = 0
    dWp = 0
    d = 0

    #loops until vehicle reaches goal
    while d > 0.1 or check:

        #point stops moving when it reaches endpoint
        if dWp > 0.1:
            xGoal = xCo[0] * time**5 + xCo[1] * time**4 + xCo[2] * time**3 + xCo[3] * time**2 + xCo[4] * time + xCo[5]
            yGoal = yCo[0] * time**5 + yCo[1] * time**4 + yCo[2] * time**3 + yCo[3] * time**2 + xCo[4] * time + yCo[5]
            goal = [xGoal, yGoal]
            time += 0.01

        #math for pure pursuit
        delX = xGoal - x
        delY = yGoal - y
        delXwp = xWp - xGoal
        delYwp = yWp - yGoal
        dWp = sqrt(delXwp**2 + delYwp**2)


        d = sqrt(delX**2 + delY**2)
        

        thetaGoal = atan2(delY, delX)
        omega = k2 * ang_diff(thetaGoal, theta)
        
        vMag = k1 * d
        vX = vMag * cos(theta)
        vY = vMag * sin(theta)

        x = x + vX * dt
        y = y + vY * dt
        theta += omega * dt

        v.update_pose(x, y, theta)
        v.place_goal(xGoal, yGoal)
        v.plot()

        #updates wp of point
        if dWp < 0.1 and q == 0:

            traj.update_states(p_i=[xWp, yWp, 0], p_f=[10, 0, 0])
            xCo, yCo, zCo = traj.solve()
            q = 1
            time = 0
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
    