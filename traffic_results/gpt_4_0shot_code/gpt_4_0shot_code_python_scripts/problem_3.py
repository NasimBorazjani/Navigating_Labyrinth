
import numpy as np
from heapq import heappop, heappush

# Define the city map
city_map = np.array([
    [10, 14, 4, 16, 'x', 17, 5, 'x', 'x'],
    [5, 20, 16, 3, 1, 8, 'x', 16, 19],
    [1, 'x', 5, 13, 3, 15, 19, 15, 'x'],
    ['x', 16, 13, 20, 'x', 8, 'x', 'x', 'x'],
    ['x', 16, 'x', 17, 11, 1, 'x', 15, 'x'],
    [10, 'x', 14, 11, 5, 7, 12, 'x', 5],
    [7, 'x', 15, 'x', 15, 8, 3, 6, 7],
    ['x', 12, 14, 'x', 'x', 'x', 16, 3, 13],
    [19, 5, 10, 'x', 'x', 'x', 9, 7, 14]
])

# Define the start and end points
start = (7, 7)
end = (1, 2)

# Define the districts
districts = {
    1: range(0, 2),
    2: range(2, 7),
    3: range(7, 9)
}

# Define the directions
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Define the A* search algorithm
def a_star_search(start, end, city_map, districts, directions):
    # Initialize the open and closed lists
    open_list = [(0, start, [start], set([get_district(start, districts)]))]
    closed_list = set()

    while open_list:
        # Pop the node with the lowest cost from the open list
        cost, current, path, visited_districts = heappop(open_list)

        # If the current node is the end node and all districts have been visited, return the path
        if current == end and len(visited_districts) == len(districts):
            return path

        # If the current node has not been visited, add it to the closed list
        if current not in closed_list:
            closed_list.add(current)

            # For each neighbor of the current node
            for direction in directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])

                # If the neighbor is within the city map and is not a closed workshop
                if (0 <= neighbor[0] < city_map.shape[0] and
                    0 <= neighbor[1] < city_map.shape[1] and
                    city_map[neighbor] != 'x'):

                    # Calculate the cost to the neighbor
                    neighbor_cost = cost + city_map[neighbor]

                    # Add the neighbor to the open list
                    heappush(open_list, (neighbor_cost, neighbor, path + [neighbor], visited_districts | set([get_district(neighbor, districts)])))

# Define a function to get the district of a workshop
def get_district(workshop, districts):
    for district, rows in districts.items():
        if workshop[0] in rows:
            return district

# Run the A* search algorithm
path = a_star_search(start, end, city_map, districts, directions)
print(path)
