
import numpy as np
from heapq import heappop, heappush

# Define the city map
city_map = np.array([
    [4, 1, 20, 15, 9, 'x', 8, 6, 'x', 'x', 14, 'x'],
    [5, 11, 9, 12, 10, 4, 15, 18, 7, 'x', 'x', 13],
    [15, 9, 1, 'x', 18, 3, 1, 19, 'x', 'x', 17, 17],
    ['x', 17, 11, 10, 'x', 19, 8, 'x', 'x', 'x', 'x', 7],
    [5, 'x', 1, 'x', 14, 13, 4, 8, 5, 'x', 13, 14],
    [16, 6, 'x', 'x', 'x', 17, 'x', 15, 4, 'x', 'x', 15],
    ['x', 'x', 'x', 15, 'x', 19, 10, 'x', 16, 18, 11, 1],
    [6, 8, 'x', 3, 'x', 5, 5, 'x', 3, 8, 9, 14],
    [10, 14, 'x', 'x', 'x', 'x', 'x', 'x', 6, 2, 'x', 'x'],
    [12, 'x', 'x', 6, 11, 4, 'x', 'x', 12, 'x', 4, 16],
    [4, 'x', 'x', 'x', 11, 'x', 'x', 'x', 18, 16, 'x', 10],
    ['x', 6, 'x', 'x', 11, 'x', 5, 13, 8, 1, 17, 9]
])

# Define the start and end workshops
start = (2, 0)
end = (7, 8)

# Define the districts
districts = [(0, 1), (2, 6), (7, 11)]

# Define the directions that Ben can move in
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Define the A* search algorithm
def a_star_search(start, end, city_map, districts):
    # Initialize the open and closed lists
    open_list = [(0, start, [start])]
    closed_list = set()

    while open_list:
        # Pop the node with the lowest cost from the open list
        cost, current, path = heappop(open_list)

        # If the current node is the end node and we have visited all districts, return the path
        if current == end and all(any(d[0] <= workshop[0] <= d[1] for workshop in path) for d in districts):
            return path

        # If the current node has not been visited yet, visit it
        if current not in closed_list:
            closed_list.add(current)

            # Visit all neighboring nodes
            for dx, dy in directions:
                neighbor = (current[0] + dx, current[1] + dy)

                # If the neighbor is within the city map and is not a closed workshop, add it to the open list
                if (0 <= neighbor[0] < city_map.shape[0] and 0 <= neighbor[1] < city_map.shape[1] and
                        city_map[neighbor] != 'x'):
                    heappush(open_list, (cost + city_map[neighbor], neighbor, path + [neighbor]))

# Print the quickest route
print(a_star_search(start, end, city_map, districts))
