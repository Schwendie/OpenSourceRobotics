import sys

from my_robots import Vehicle

v = Vehicle()
v.add_obstacles([10,0,5])
print(v.obstacles)
while True:
    v.plot()

if __name__ == "__main__":
    try:
        x_wp = float(sys.argv[1])
        y_wp = float(sys.argv[2])
    except:
        print("Please enter a numerical value for the waypoints")

