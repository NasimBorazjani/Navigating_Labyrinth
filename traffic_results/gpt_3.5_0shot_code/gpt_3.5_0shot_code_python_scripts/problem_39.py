
import numpy as np

# Define the matrix map of the city
city_map = np.array([[15, 8, 18, 3, 19, np.inf, 17, np.inf, np.inf, np.inf, np.inf],
                      [19, 16, np.inf, 18, 20, 2, 5, 7, 11, 12, 3],
                      [18, np.inf, 18, 1, 2, np.inf, np.inf, np.inf, 12, 16, 4],
                      [9, 20, 4, 19, 5, 15, np.inf, np.inf, np.inf, 6, 4],
                      [np.inf, 18, 8, 1, np.inf, 7, 1, 7, 10, 1, 4],
                      [np.inf, 18, np.inf, 18, 19, 9, 18, 5, 15, 1, 7],
                      [3, np.inf, 12, 14, np.inf, np.inf, np.inf, np.inf, 1, np.inf, np.inf],
                      [np.inf, 12, 6, np.inf, 6, np.inf, 1, np.inf, 1, 7, np.inf],
                      [np.inf, 5, 10, 14, 2, np.inf, np.inf, 7, 11, 3, np.inf],
                      [6, 9, 13, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 3],
                      [19, 12, np.inf, 15, np.inf, 14, np.inf, 9, np.inf, np.inf, 19]])

# Define the districts
districts = {1: [0, 1, 2], 2: [3, 4], 3: [5, 6, 7, 8, 9, 10]}

# Define the starting and destination workshops
start = (3, 1)
destination = (5, 10)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, destination):
    rows, cols = city_map.shape
    distances = np.full((rows, cols), np.inf)
    distances[start] = city_map[start]
    visited = set()
    path = {}

    while len(visited) < rows * cols:
        current = min((x, y) for x in range(rows) for y in range(cols) if (x, y) not in visited)[1]
        visited.add((current[0], current[1]))

        neighbors = [(current[0] + 1, current[1]), (current[0] - 1, current[1]),
                     (current[0], current[1] + 1), (current[0], current[1] - 1)]

        for neighbor in neighbors:
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and neighbor not in visited:
                new_distance = distances[current] + city_map[neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    path[neighbor] = current

    shortest_path = []
    current = destination
    while current != start:
        shortest_path.append(current)
        current = path[current]
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path

# Find the shortest path that satisfies the conditions
shortest_path = []
for district in districts.values():
    for workshop in district:
        path = dijkstra(city_map, start, (district, workshop))
        if path[-1] == (district, workshop):
            shortest_path.extend(path)
            start = (district, workshop)
            break

print(shortest_path)
