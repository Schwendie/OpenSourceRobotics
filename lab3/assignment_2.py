import sys

from my_robots import Vehicle
"""
v = Vehicle()
#v.add_obstacles([10,0,5])
#print(v.obstacles)
x_goal, y_goal = 5, 0
v.place_goal(x_goal, y_goal)
print(v.goal)
v.pure_pursuit(x_goal, y_goal)
x_goal = 5
y_goal = 5
v.place_goal(x_goal, y_goal)
v.pure_pursuit(x_goal, y_goal)

"""



if __name__ == "__main__":
    try:
        x_wp = float(sys.argv[1])
        y_wp = float(sys.argv[2])
    except:
        print("Please enter a numerical value for the waypoints")
    v = Vehicle()
    v.add_obstacles([10,0,5])
    v.place_goal(20,0)
    v.pure_pursuit(x_wp, y_wp)
    v.pure_pursuit(v.goal[0], v.goal[1])
