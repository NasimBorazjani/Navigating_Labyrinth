
import numpy as np

# Define the city map as a numpy array
city_map = np.array([[17, 9, 11, 5, 19, 4, 18, np.inf, 5, 8, np.inf, np.inf],
                      [6, 13, np.inf, 9, 2, 20, 11, 20, 7, np.inf, np.inf, 3],
                      [4, 17, np.inf, 18, 2, 10, np.inf, 16, np.inf, 18, np.inf, np.inf],
                      [12, 10, 9, 14, np.inf, np.inf, 12, 6, 1, 2, np.inf, np.inf],
                      [5, np.inf, np.inf, 3, np.inf, 4, 9, 14, 8, np.inf, 10, 12],
                      [1, np.inf, 6, 3, 18, 18, 17, 17, 10, np.inf, np.inf, 10],
                      [13, np.inf, np.inf, np.inf, np.inf, np.inf, 14, np.inf, 1, 19, np.inf, 7],
                      [11, np.inf, np.inf, 5, 9, np.inf, 18, 19, 13, 13, np.inf, 10],
                      [np.inf, np.inf, 11, np.inf, 17, np.inf, np.inf, np.inf, 14, 17, np.inf, 13],
                      [19, np.inf, np.inf, np.inf, np.inf, 19, 12, 7, 3, 14, np.inf, 9],
                      [np.inf, 12, 7, 15, 1, np.inf, 16, 11, 9, 17, np.inf, np.inf],
                      [np.inf, np.inf, np.inf, 10, np.inf, 1, 7, np.inf, np.inf, np.inf, 6, 12]])

# Define the districts
districts = {1: [0, 1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9, 10, 11]}

# Define the start and end workshops
start_workshop = (7, 0)
end_workshop = (3, 8)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    n = city_map.shape[0]
    distances = np.full((n, n), np.inf)
    distances[start] = 0
    visited = set()
    path = {}

    while len(visited) < n * n:
        current = min((i, j) for i in range(n) for j in range(n) if (i, j) not in visited)
        visited.add(current)

        neighbors = [(current[0] + 1, current[1]), (current[0] - 1, current[1]),
                     (current[0], current[1] + 1), (current[0], current[1] - 1)]

        for neighbor in neighbors:
            if neighbor[0] >= 0 and neighbor[0] < n and neighbor[1] >= 0 and neighbor[1] < n:
                if neighbor not in visited and city_map[neighbor] != np.inf:
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
shortest_path = []
for district in districts.values():
    for workshop in district:
        path = dijkstra(city_map, start_workshop, (workshop // 12, workshop % 12))
        if path[-1] == (workshop // 12, workshop % 12):
            shortest_path += path

shortest_path += dijkstra(city_map, (9, 10), end_workshop)

print(shortest_path)
