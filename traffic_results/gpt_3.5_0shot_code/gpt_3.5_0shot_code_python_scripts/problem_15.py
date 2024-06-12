
import numpy as np

# Define the matrix map of the city
city_map = np.array([[4, 13, np.inf, 9, np.inf, np.inf, np.inf, np.inf, np.inf],
                      [1, 11, np.inf, 16, 5, 7, 12, 16, np.inf],
                      [12, 11, np.inf, 14, np.inf, np.inf, 12, np.inf, 3],
                      [9, 11, np.inf, 9, 10, np.inf, 8, np.inf, np.inf],
                      [20, 2, np.inf, 1, 16, 12, 18, 17, 10],
                      [10, 13, 4, 15, 13, 2, 20, 3, 15],
                      [np.inf, 6, 13, 1, 8, 20, 14, 11, 3],
                      [14, np.inf, 9, np.inf, np.inf, 13, 19, 10, np.inf],
                      [12, np.inf, 18, 1, np.inf, np.inf, 9, np.inf, np.inf]])

# Define the districts
districts = {1: [0, 1, 2], 2: [3, 4], 3: [5, 6, 7, 8]}

# Define the start and end workshops
start_workshop = (3, 1)
end_workshop = (5, 8)

# Function to find the shortest path using Dijkstra's algorithm
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
            if city_map[min_index, i] + dist[min_index] < dist[i]:
                dist[i] = city_map[min_index, i] + dist[min_index]
                prev[i] = min_index

    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return path

# Find the shortest path that satisfies the conditions
shortest_path = None
for district in districts.values():
    for workshop in district:
        path1 = dijkstra(city_map, start_workshop[0]*city_map.shape[1]+start_workshop[1], workshop)
        path2 = dijkstra(city_map, workshop, end_workshop[0]*city_map.shape[1]+end_workshop[1])
        if path1 and path2:
            path = path1[:-1] + path2
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = path

# Convert the path to list of tuples
path_tuples = [(p // city_map.shape[1], p % city_map.shape[1]) for p in shortest_path]

print(path_tuples)
