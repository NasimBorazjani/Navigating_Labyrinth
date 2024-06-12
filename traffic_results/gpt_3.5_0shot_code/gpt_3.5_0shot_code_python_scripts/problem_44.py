
import numpy as np

# Define the matrix map of the city
city_map = [
    ['x', 16, 5, 13, 'x', 'x', 2, 'x', 6, 'x', 'x'],
    ['x', 'x', 17, 'x', 15, 'x', 10, 'x', 5, 17, 'x'],
    ['x', 'x', 'x', 'x', 15, 3, 10, 2, 4, 13, 14],
    ['x', 'x', 'x', 'x', 17, 2, 4, 'x', 1, 4, 5],
    [2, 'x', 'x', 2, 6, 17, 'x', 'x', 'x', 4, 19],
    [19, 5, 'x', 'x', 'x', 'x', 10, 12, 1, 18, 10],
    ['x', 3, 'x', 12, 'x', 10, 15, 11, 'x', 4, 15],
    [2, 'x', 11, 9, 'x', 12, 11, 'x', 15, 10, 6],
    [19, 'x', 16, 5, 'x', 'x', 'x', 11, 'x', 11, 8],
    [12, 2, 'x', 3, 'x', 4, 'x', 'x', 15, 'x', 'x'],
    ['x', 'x', 18, 16, 'x', 'x', 4, 'x', 12, 13, 'x']
]

# Define the districts
districts = {
    1: (0, 2),
    2: (3, 7),
    3: (8, 10)
}

# Define the start and end workshops
start_workshop = (8, 10)
end_workshop = (3, 4)

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
            if 0 <= new_i < rows and 0 <= new_j < cols and city_map[new_i][new_j] != 'x':
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
shortest_path = None
for i in range(districts[1][0], districts[1][1] + 1):
    for j in range(districts[2][0], districts[2][1] + 1):
        for k in range(districts[3][0], districts[3][1] + 1):
            path1 = dijkstra(city_map, start_workshop, (i, j))
            path2 = dijkstra(city_map, (i, j), (k, j))
            path3 = dijkstra(city_map, (k, j), end_workshop)
            if path1 and path2 and path3:
                if shortest_path is None or len(path1) + len(path2) + len(path3) < len(shortest_path):
                    shortest_path = path1 + path2[1:] + path3

# Print the shortest path
print(shortest_path)
