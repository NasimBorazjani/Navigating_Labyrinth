
import numpy as np

# Define the matrix map of the city
city_map = [
    ['x', 11, 5, 18, 'x', 14, 7, 'x', 15, 11, 14],
    ['x', 'x', 'x', 'x', 13, 13, 11, 17, 8, 13, 'x'],
    [8, 1, 5, 17, 'x', 4, 8, 20, 7, 4],
    [10, 'x', 'x', 'x', 18, 1, 'x', 'x', 20, 'x', 'x'],
    [18, 15, 'x', 6, 'x', 4, 3, 4, 3, 13, 'x'],
    [5, 1, 'x', 4, 'x', 'x', 'x', 11, 'x', 14, 18],
    [19, 19, 'x', 'x', 'x', 'x', 15, 'x', 10, 'x', 'x'],
    [15, 5, 7, 'x', 14, 6, 'x', 'x', 'x', 13, 'x'],
    [18, 7, 'x', 19, 'x', 12, 'x', 'x', 15, 'x', 'x'],
    [10, 9, 'x', 1, 'x', 'x', 15, 'x', 11, 'x', 2],
    ['x', 'x', 8, 'x', 19, 'x', 1, 3, 'x', 'x', 8]
]

# Convert 'x' to a large number to represent closed workshops
for i in range(len(city_map)):
    for j in range(len(city_map[0])):
        if city_map[i][j] == 'x':
            city_map[i][j] = 999

# Define the districts
districts = {
    1: [(0, 0), (0, 1), (1, 0), (1, 1)],
    2: [(2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1), (5, 0), (5, 1), (6, 0), (6, 1)],
    3: [(7, 0), (7, 1), (8, 0), (8, 1), (9, 0), (9, 1), (10, 0), (10, 1)]
}

# Define the starting and ending workshops
start_workshop = (7, 0)
end_workshop = (3, 8)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    rows, cols = len(city_map), len(city_map[0])
    distances = np.full((rows, cols), np.inf)
    distances[start[0]][start[1]] = 0
    visited = set()
    path = {}

    while len(visited) < rows * cols:
        min_dist = np.inf
        current = None
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and distances[i][j] < min_dist:
                    min_dist = distances[i][j]
                    current = (i, j)

        if current == end:
            break

        visited.add(current)

        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = current[0] + i, current[1] + j
            if 0 <= new_i < rows and 0 <= new_j < cols and (new_i, new_j) not in visited:
                new_dist = distances[current[0]][current[1]] + city_map[new_i][new_j]
                if new_dist < distances[new_i][new_j]:
                    distances[new_i][new_j] = new_dist
                    path[(new_i, new_j)] = current

    shortest_path = []
    current = end
    while current is not None:
        shortest_path.append(current)
        current = path.get(current)

    return shortest_path[::-1]

# Find the shortest path that satisfies the conditions
path = []
for district in districts.values():
    for workshop in district:
        if workshop != start_workshop and workshop != end_workshop:
            path1 = dijkstra(city_map, start_workshop, workshop)
            path2 = dijkstra(city_map, workshop, end_workshop)
            if path1 and path2:
                path = path1[:-1] + path2

# Print the result
print(path)
