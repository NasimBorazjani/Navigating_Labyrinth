
import numpy as np

# Define the matrix map of the city
city_map = np.array([[x x x x 9 x 14 17 x 13 3 x 13 10 18],
                     [1 x 11 12 14 13 8 x 5 7 x x x x x],
                     [3 x x 18 11 16 x x x x 1 x 15 12 10],
                     [x 10 x 3 2 15 14 x x x 17 x 6 1 x],
                     [8 10 x x x x 1 19 6 x 17 2 x x x],
                     [x 6 15 2 17 2 11 5 9 x 12 15 x x 16],
                     [x x 8 x 14 x 13 20 17 12 19 9 x x x],
                     [13 10 1 4 11 3 15 x x 3 14 20 x 6 x],
                     [x 11 16 9 19 18 12 2 x x 1 10 x x x],
                     [x 13 18 18 7 x x x x 18 5 6 x 7 3],
                     [x x x 18 6 16 10 18 9 19 x 3 5 3 4],
                     [14 18 4 1 17 x 7 x 3 16 11 x 17 11 1],
                     [x x 12 16 x 14 9 x x x 13 1 x x 19],
                     [19 x 3 x 8 x x x 3 x x x 17 9 8],
                     [15 x 2 8 9 13 x 14 x 6 x 19 x x 5]])

# Define the districts
districts = {1: range(5), 2: range(5, 10), 3: range(10, 15)}

# Define the starting and destination workshops
start = (5, 2)
dest = (9, 13)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, dest):
    rows, cols = city_map.shape
    dist = np.full((rows, cols), np.inf)
    dist[start] = city_map[start]
    visited = np.zeros((rows, cols), dtype=bool)
    prev = np.full((rows, cols), None)

    while True:
        min_dist = np.inf
        current = None
        for r in range(rows):
            for c in range(cols):
                if not visited[r, c] and dist[r, c] < min_dist:
                    min_dist = dist[r, c]
                    current = (r, c)

        if current is None:
            break

        visited[current] = True

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = current[0] + dr, current[1] + dc
            if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r, new_c]:
                new_dist = dist[current] + city_map[new_r, new_c]
                if new_dist < dist[new_r, new_c]:
                    dist[new_r, new_c] = new_dist
                    prev[new_r, new_c] = current

    path = []
    current = dest
    while current is not None:
        path.append(current)
        current = prev[current]

    return path[::-1]

# Find the shortest path from start to dest visiting at least one workshop in each district
path = []
for district in districts.values():
    min_path = None
    min_dist = np.inf
    for r in district:
        for c in range(len(city_map[r])):
            if city_map[r, c] != 'x':
                temp_path = dijkstra(city_map, start, (r, c))
                temp_dist = sum(city_map[pos] for pos in temp_path)
                if temp_dist < min_dist:
                    min_dist = temp_dist
                    min_path = temp_path
    path += min_path

print(path)
