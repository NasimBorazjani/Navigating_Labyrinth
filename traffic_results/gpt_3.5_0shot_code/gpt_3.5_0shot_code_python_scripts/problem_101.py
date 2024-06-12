
import numpy as np

# Define the city map as a numpy array
city_map = np.array([
    ['x', 3, 1, 19, 8, 1, 4, 18, 15, 17, 4, 3, 'x', 3, 'x'],
    ['x', 11, 'x', 'x', 'x', 12, 'x', 19, 15, 4, 'x', 'x', 'x', 'x', 'x'],
    [4, 1, 'x', 8, 'x', 12, 17, 'x', 14, 4, 9, 11, 13, 6, 19],
    [2, 'x', 6, 14, 15, 'x', 18, 9, 'x', 10, 10, 'x', 'x', 1, 'x'],
    ['x', 11, 'x', 8, 'x', 5, 'x', 8, 7, 6, 'x', 'x', 13, 6, 'x'],
    ['x', 'x', 'x', 17, 'x', 13, 'x', 'x', 'x', 'x', 18, 19, 5, 'x', 'x'],
    ['x', 12, 18, 'x', 'x', 'x', 19, 'x', 12, 'x', 11, 7, 19, 12, 'x'],
    [6, 6, 'x', 6, 4, 'x', 18, 'x', 'x', 15, 18, 'x', 6, 8, 'x'],
    [10, 10, 'x', 'x', 6, 4, 11, 19, 'x', 9, 'x', 2, 'x', 3, 14],
    ['x', 18, 14, 10, 'x', 1, 'x', 6, 'x', 15, 'x', 6, 'x', 14, 'x'],
    ['x', 'x', 7, 10, 'x', 2, 'x', 7, 14, 4, 11, 'x', 'x', 'x', 'x'],
    [12, 'x', 6, 'x', 8, 5, 6, 6, 8, 'x', 'x', 'x', 4, 7],
    ['x', 'x', 1, 8, 10, 4, 10, 17, 19, 11, 2, 'x', 'x', 'x', 16],
    ['x', 'x', 'x', 17, 8, 19, 'x', 14, 'x', 17, 17, 5, 7, 6, 7],
    [1, 'x', 14, 'x', 3, 'x', 18, 6, 18, 8, 'x', 13, 10, 'x', 'x']
])

# Define the districts
districts = {
    1: (0, 4),
    2: (5, 8),
    3: (9, 14)
}

# Define the destination workshop
destination = (4, 13)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    rows, cols = city_map.shape
    distances = np.full((rows, cols), np.inf)
    distances[start] = 0
    visited = set()
    path = {}

    while len(visited) < rows * cols:
        current = min((i, j) for i in range(rows) for j in range(cols) if (i, j) not in visited)
        visited.add(current)

        neighbors = [(current[0] + 1, current[1]), (current[0] - 1, current[1]), 
                     (current[0], current[1] + 1), (current[0], current[1] - 1)]

        for neighbor in neighbors:
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and city_map[neighbor] != 'x':
                new_distance = distances[current] + city_map[neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    path[neighbor] = current

    shortest_path = []
    current = end
    while current != start:
        shortest_path.append(current)
        current = path[current]
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path

# Find the shortest path from Ben's current workshop to the destination
shortest_path = dijkstra(city_map, (7, 0), destination)

print(shortest_path)
