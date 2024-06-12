
import numpy as np

# Define the matrix map of the city
city_map = np.array([[8, -1, -1, 9, 15, 13, 11, 2, -1, -1],
                      [13, -1, -1, -1, 5, -1, -1, 7, -1, -1],
                      [12, 3, -1, -1, -1, -1, -1, 10, -1, -1],
                      [12, -1, -1, 9, 15, 9, 11, 5, 17, -1],
                      [3, 5, 12, -1, 11, 5, -1, 15, 1, 18],
                      [14, 3, -1, -1, 18, 14, 19, 19, 12, 15],
                      [-1, 20, 17, 15, 11, -1, -1, -1, -1, -1],
                      [12, 13, 18, -1, -1, 5, -1, 2, -1, 13],
                      [-1, -1, 13, 19, 4, -1, 12, -1, -1, 8],
                      [-1, -1, 10, -1, -1, -1, 15, -1, 4, 16]])

# Define the districts
districts = {1: [0, 1, 2, 3], 2: [4, 5], 3: [6, 7, 8, 9]}

# Define the start and end workshops
start_workshop = (4, 9)
end_workshop = (6, 1)

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
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and city_map[neighbor] != -1:
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

# Find the shortest path that satisfies the conditions
path = []
for district in districts.values():
    for workshop in district:
        if city_map[start_workshop] != -1 and city_map[workshop] != -1:
            path1 = dijkstra(city_map, start_workshop, (workshop // 10, workshop % 10))
            path2 = dijkstra(city_map, (workshop // 10, workshop % 10), end_workshop)
            if path1 and path2:
                path = path1[:-1] + path2

print(path)
