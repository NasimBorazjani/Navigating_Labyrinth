
import numpy as np

# Define the matrix map of the city
city_map = np.array([[10, 14, 4, 16, np.inf, 17, 5, np.inf, np.inf],
                      [5, 20, 16, 3, 1, 8, np.inf, 16, 19],
                      [1, np.inf, 5, 13, 3, 15, 19, 15, np.inf],
                      [np.inf, 16, 13, 20, np.inf, 8, np.inf, np.inf, np.inf],
                      [np.inf, 16, np.inf, 17, 11, 1, np.inf, 15, np.inf],
                      [10, np.inf, 14, 11, 5, 7, 12, np.inf, 5],
                      [7, np.inf, 15, np.inf, 15, 8, 3, 6, 7],
                      [np.inf, 12, 14, np.inf, np.inf, np.inf, 16, 3, 13],
                      [19, 5, 10, np.inf, np.inf, np.inf, 9, 7, 14]])

# Define the districts
districts = {1: [0, 1], 2: [2, 6], 3: [7, 8]}

# Define the destination workshop
destination = (1, 2)

# Define a function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    n = city_map.shape[0]
    dist = [np.inf] * n
    dist[start] = 0
    prev = [None] * n
    visited = [False] * n

    while not all(visited):
        min_dist = np.inf
        min_index = None
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i

        visited[min_index] = True

        for i in range(n):
            if city_map[min_index, i] < np.inf:
                if dist[min_index] + city_map[min_index, i] < dist[i]:
                    dist[i] = dist[min_index] + city_map[min_index, i]
                    prev[i] = min_index

    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return path

# Find the shortest path from Ben's current workshop to the destination workshop
start = 7 * city_map.shape[1] + 7
end = 1 * city_map.shape[1] + 2
shortest_path = dijkstra(city_map.flatten(), start, end)

# Filter the path to include at least one workshop from each district
filtered_path = []
for workshop in shortest_path:
    row = workshop // city_map.shape[1]
    for district, indices in districts.items():
        if row in indices:
            filtered_path.append((workshop // city_map.shape[1], workshop % city_map.shape[1]))
            del districts[district]
            break

print(filtered_path)
