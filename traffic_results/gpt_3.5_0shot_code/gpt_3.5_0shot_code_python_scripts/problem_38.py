
import numpy as np

# Define the matrix map of the city
city_map = np.array([[0, 0, 0, 3, 0, 0, 16, 0, 2, 16, 3],
                     [8, 0, 8, 5, 0, 0, 10, 0, 19, 4, 0],
                     [0, 0, 18, 1, 16, 0, 9, 15, 0, 0, 11],
                     [0, 0, 17, 16, 4, 19, 2, 0, 1, 11, 0],
                     [9, 0, 5, 16, 18, 0, 0, 7, 0, 18, 6],
                     [0, 15, 7, 0, 0, 0, 19, 8, 9, 17, 0],
                     [0, 15, 19, 0, 0, 0, 6, 2, 6, 0, 5],
                     [0, 12, 11, 3, 11, 4, 0, 0, 0, 3, 0],
                     [18, 12, 4, 0, 3, 10, 0, 3, 0, 7, 14],
                     [15, 11, 12, 0, 13, 2, 0, 0, 5, 14, 0],
                     [0, 0, 15, 0, 16, 4, 10, 13, 0, 0, 4]])

# Define the closed workshops
closed_workshops = set([(0, 0), (1, 1), (1, 9), (2, 0), (2, 1), (2, 5), (2, 8), (2, 9), (3, 0), (3, 1), (3, 6), (3, 8), (4, 0), (4, 2), (4, 4), (4, 9), (5, 3), (5, 4), (5, 5), (5, 9), (6, 3), (6, 4), (6, 5), (6, 9), (7, 6), (7, 7), (7, 8), (7, 10), (8, 3), (8, 6), (8, 10), (9, 3), (9, 5), (9, 6), (9, 10), (10, 0), (10, 1), (10, 3), (10, 5), (10, 9), (10, 10)])

# Define the districts
districts = [(0, 3), (4, 7), (8, 10)]

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    rows, cols = city_map.shape
    distances = np.full((rows, cols), np.inf)
    distances[start] = 0
    visited = set()
    path = {}

    while len(visited) < rows * cols:
        current = min((i, j) for i in range(rows) for j in range(cols) if (i, j) not in visited and city_map[i, j] != 'x', key=lambda x: distances[x[0], x[1]])
        visited.add(current)

        if current == end:
            break

        for i, j in [(current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0], current[1]+1)]:
            if 0 <= i < rows and 0 <= j < cols and city_map[i, j] != 'x' and (i, j) not in visited:
                new_dist = distances[current[0], current[1]] + city_map[i, j]
                if new_dist < distances[i, j]:
                    distances[i, j] = new_dist
                    path[(i, j)] = current

    shortest_path = []
    current = end
    while current != start:
        shortest_path.append(current)
        current = path[current]
    shortest_path.append(start)

    return shortest_path[::-1]

# Find the shortest path that satisfies the conditions
path = []
for i in range(len(districts)-1):
    start_district = districts[i]
    end_district = districts[i+1]
    for start in [(i, j) for i in range(start_district[0], start_district[1]+1) for j in range(cols) if city_map[i, j] != 'x']:
        for end in [(i, j) for i in range(end_district[0], end_district[1]+1) for j in range(cols) if city_map[i, j] != 'x']:
            if start != end:
                temp_path = dijkstra(city_map, start, end)
                if temp_path:
                    path.extend(temp_path[:-1])

# Add the last segment of the path from the last district to the destination
path.extend(dijkstra(city_map, path[-1], (8, 0)))

print(path)
