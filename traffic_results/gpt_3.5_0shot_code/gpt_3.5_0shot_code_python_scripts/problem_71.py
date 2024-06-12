
import numpy as np

# Define the matrix map of the city
city_map = [
    ['x', 12, 'x', 'x', 'x', 5, 9, 14, 6, 'x', 3, 14, 'x'],
    ['x', 'x', 3, 'x', 11, 'x', 13, 'x', 'x', 'x', 'x', 9, 8],
    ['x', 18, 'x', 'x', 'x', 13, 4, 5, 'x', 'x', 'x', 13, 'x'],
    [10, 4, 'x', 'x', 'x', 'x', 'x', 18, 'x', 15, 'x', 'x', 'x'],
    ['x', 1, 7, 'x', 7, 6, 'x', 3, 'x', 2, 'x', 'x', 5],
    ['x', 15, 5, 'x', 'x', 10, 'x', 19, 'x', 'x', 'x', 10, 6],
    ['x', 18, 1, 2, 'x', 7, 16, 19, 'x', 'x', 10, 8, 8],
    [8, 'x', 'x', 6, 2, 'x', 'x', 'x', 7, 11, 5, 11, 2],
    ['x', 4, 1, 1, 5, 12, 3, 6, 2, 1, 'x', 3, 8],
    ['x', 'x', 5, 5, 14, 15, 7, 'x', 'x', 11, 'x', 7, 9],
    ['x', 6, 12, 16, 17, 'x', 'x', 4, 'x', 19, 9, 5, 'x'],
    [12, 'x', 4, 'x', 8, 4, 'x', 5, 'x', 'x', 'x', 5, 'x'],
    ['x', 5, 'x', 'x', 'x', 'x', 'x', 7, 'x', 'x', 11, 'x', 'x']
]

# Convert 'x' to a large number to represent closed workshops
city_map = [[1000 if x == 'x' else x for x in row] for row in city_map]

# Define the districts
districts = {
    1: (0, 4),
    2: (5, 5),
    3: (6, 12)
}

# Define the start and end workshops
start_workshop = (6, 12)
end_workshop = (4, 1)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    rows, cols = len(city_map), len(city_map[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = city_map[start[0]][start[1]]
    visited = set()
    path = {}

    while True:
        min_distance = float('inf')
        min_node = None
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and distances[i][j] < min_distance:
                    min_distance = distances[i][j]
                    min_node = (i, j)

        if min_node is None:
            break

        visited.add(min_node)

        neighbors = [(min_node[0] + 1, min_node[1]), (min_node[0] - 1, min_node[1]),
                     (min_node[0], min_node[1] + 1), (min_node[0], min_node[1] - 1)]

        for neighbor in neighbors:
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                new_distance = distances[min_node[0]][min_node[1]] + city_map[neighbor[0]][neighbor[1]]
                if new_distance < distances[neighbor[0]][neighbor[1]]:
                    distances[neighbor[0]][neighbor[1]] = new_distance
                    path[neighbor] = min_node

    shortest_path = []
    current = end
    while current != start:
        shortest_path.append(current)
        current = path[current]
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path

# Find the shortest path from start to end visiting at least one workshop in each district
shortest_path = []
for district in districts.values():
    district_path = dijkstra(city_map, start_workshop, end_workshop)
    shortest_path.extend(district_path)
    start_workshop = district_path[-1]

print(shortest_path)
