import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import from_levels_and_colors

plt.ion()

obstacle_prob = 0.2
m, n = 25, 25
start_node = (0, 0)
goal_node = (m-1, n-1)
distance = 0

colors = ['white', 'black', 'red', 'blue', 'green', 'yellow', 'gray']
levels = [0, 1, 2, 3, 4, 5, 6, 7]

cmap, norm = from_levels_and_colors(levels, colors)

grid = np.int8(np.random.random((m, n)) > (1-obstacle_prob))
grid[start_node] = 5
grid[goal_node] = 4

parent_map = [[() for _ in range(n)] for _ in range(m)]
distance_map = np.full((m, n), np.inf)
distance_map[start_node] = 0

distance = 0

while True:
    grid[start_node] = 5
    grid[goal_node] = 4

    current_node = np.unravel_index(np.argmin(distance_map, axis=None), distance_map.shape)
    min_distance = np.min(distance_map)
    if (current_node == goal_node) or np.isinf(min_distance):
        break

    ###Your code goes here###
    distance += 1
    
    if (current_node[0] - 1 >= 0):
        up_node = (current_node[0]-1, current_node[1])
        if (grid[up_node] == 0) or (grid[up_node] == 4):
            grid[up_node] = 3
            distance_map[up_node] = distance
            parent_map[up_node] = current_node
            
    if (current_node[1] - 1 >= 0):
        left_node = (current_node[0], current_node[1]-1)
        if (grid[left_node] == 0) or (grid[left_node] == 4):
            grid[left_node] = 3
            distance_map[left_node] = distance
            parent_map[left_node] = current_node
            
    if (current_node[1] + 1 < n):
        right_node = (current_node[0], current_node[1]+1)
        if (grid[right_node] == 0) or (grid[right_node] == 4):
            grid[right_node] = 3
            distance_map[right_node] = distance
            parent_map[right_node] = current_node
    
    if (current_node[0] + 1 < m):
        down_node = (current_node[0]+1, current_node[1])
        if (grid[down_node] == 0) or (grid[down_node] == 4):
            grid[down_node] = 3
            distance_map[down_node] = distance
            parent_map[down_node] = current_node
            
    if (grid[current_node] == 3):
        grid[current_node] = 2
    
    distance_map[current_node] = np.inf





















    #########################

    plt.cla()
    plt.imshow(grid, cmap=cmap, norm=norm, interpolation=None)
    plt.show()
    plt.pause(0.001)

if np.isinf(distance_map[goal_node]):
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
