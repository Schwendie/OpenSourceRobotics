import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import from_levels_and_colors

plt.ion()

obstacle_prob = 0.2
m, n = 100, 100
start_node = (0, 0)
goal_node = (m-1, n-1)

colors = ['white', 'black', 'red', 'blue', 'green', 'yellow', 'gray']
levels = [0, 1, 2, 3, 4, 5, 6, 7]

cmap, norm = from_levels_and_colors(levels, colors)

grid = np.int8(np.random.random((m, n)) > (1-obstacle_prob))
grid[start_node] = 5
grid[goal_node] = 4

parent_map = [[() for _ in range(n)] for _ in range(m)]

X, Y = np.meshgrid([i for i in range(n)], [i for i in range(m)])
H = np.abs(X - goal_node[0]) + np.abs(Y - goal_node[1])
f = np.full((m, n), np.inf)
g = np.full((m, n), np.inf)
f[start_node] = H[start_node]
g[start_node] = 0

distance = 0

while True:
    grid[start_node] = 5
    grid[goal_node] = 4

    current_node = np.unravel_index(np.argmin(f, axis=None), f.shape)
    min_distance = np.min(f)
    if (current_node == goal_node) or np.isinf(min_distance):
        break

    ###Your code goes here###
    
    distance += 1

    if (current_node[0]-1 >= 0):
        up_node = (current_node[0]-1, current_node[1])
        if (grid[up_node] == 0) or (grid[up_node] == 4):
            grid[up_node] = 3
            parent_map[up_node[0]][up_node[1]] = current_node
            g[up_node] = distance
            f[up_node] = H[up_node]

    if (current_node[1]-1 >= 0):
        left_node = (current_node[0], current_node[1]-1)
        if (grid[left_node] == 0) or (grid[left_node] == 4):
            grid[left_node] = 3
            parent_map[left_node[0]][left_node[1]] = current_node
            g[left_node] = distance
            f[left_node] = H[left_node]

    if (current_node[1]+1 < n):
        right_node = (current_node[0], current_node[1]+1)
        if (grid[right_node] == 0) or (grid[right_node] == 4):
            grid[right_node] = 3
            parent_map[right_node[0]][right_node[1]] = current_node
            g[right_node] = distance
            f[right_node] = H[right_node]

    if (current_node[0]+1 < m):
        down_node = (current_node[0]+1, current_node[1])
        if (grid[down_node] == 0) or (grid[down_node] == 4):
            grid[down_node] = 3
            parent_map[down_node[0]][down_node[1]] = current_node
            g[down_node] = distance
            f[down_node] = H[down_node]

    if (grid[current_node] == 3):
        grid[current_node] = 2

    f[current_node] = np.inf

    #########################

    plt.cla()
    plt.imshow(grid, cmap=cmap, norm=norm, interpolation=None)
    plt.show()
    plt.pause(0.001)

if np.isinf(f[goal_node]):
    route = []
    print("Cannot reach goal node from start location.")
else:
    route = [goal_node]
    while parent_map[route[0][0]][route[0][1]] is not ():
        route.insert(0, parent_map[route[0][0]][route[0][1]])

    print("The route found covers %d grid cells." % len(route))
    for i in range(1, len(route)):
        grid[route[i]] = 6
        plt.cla()
        plt.imshow(grid, cmap=cmap, norm=norm, interpolation=None)
        plt.show()
        plt.pause(0.1)