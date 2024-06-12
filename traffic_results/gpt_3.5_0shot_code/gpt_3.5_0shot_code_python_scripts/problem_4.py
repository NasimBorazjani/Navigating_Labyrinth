
import numpy as np

# Define the city map as a numpy array
city_map = np.array([[18, 9, 2, np.inf, 9, 14, np.inf, 1, np.inf],
                      [3, 14, 18, 7, np.inf, 3, np.inf, 2, 19],
                      [6, 18, 20, 3, 13, np.inf, 6, 10, np.inf],
                      [20, np.inf, 12, 4, 14, 6, np.inf, np.inf, np.inf],
                      [7, 18, 8, 5, 19, 3, np.inf, np.inf, 7],
                      [15, 9, 14, 16, 5, 14, 6, np.inf, np.inf],
                      [np.inf, 5, 13, np.inf, np.inf, 19, np.inf, np.inf, 2],
                      [np.inf, np.inf, 8, np.inf, np.inf, np.inf, np.inf, 17, 12],
                      [np.inf, 1, np.inf, np.inf, 3, 19, np.inf, 2, 18]])

# Define the districts
districts = {1: [0, 1, 2], 2: [3, 4], 3: [5, 6, 7, 8]}

# Define the start and end workshops
start = (2, 0)
end = (5, 6)

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

        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i, new_j = current[0] + i, current[1] + j
            if 0 <= new_i < rows and 0 <= new_j < cols and city_map[new_i, new_j] != np.inf:
                if distances[current] + city_map[new_i, new_j] < distances[new_i, new_j]:
                    distances[new_i, new_j] = distances[current] + city_map[new_i, new_j]
                    path[new_i, new_j] = current

    shortest_path = []
    current = end
    while current != start:
        shortest_path.append(current)
        current = path[current]
    shortest_path.append(start)

    return shortest_path[::-1]

# Find the shortest path that satisfies the conditions
path = dijkstra(city_map, start, end)
path_districts = [district for district, workshops in districts.items() if any(workshop in path for workshop in workshops)]

print(path)
print(path_districts)
