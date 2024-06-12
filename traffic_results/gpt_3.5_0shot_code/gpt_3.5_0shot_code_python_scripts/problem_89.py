
import numpy as np

# Define the city map as a numpy array
city_map = np.array([
    [np.inf, np.inf, np.inf, 7, 11, 16, 13, 19, 15, np.inf, 19, np.inf, np.inf, 16],
    [9, np.inf, 14, np.inf, 7, 3, np.inf, np.inf, 17, 9, np.inf, np.inf, np.inf, 19],
    [np.inf, 11, 6, 18, np.inf, 19, 4, np.inf, np.inf, np.inf, 19, 12, 4, 17],
    [5, 12, 15, 3, np.inf, np.inf, np.inf, np.inf, 7, np.inf, 11, 17, 20, 20],
    [6, np.inf, 11, 15, 11, 17, 16, 5, np.inf, 3, 4, 20, np.inf, 14],
    [np.inf, 11, np.inf, 6, np.inf, 16, 2, 18, 5, 11, np.inf, 14, 4, 7],
    [np.inf, 6, np.inf, 17, np.inf, np.inf, 15, 7, np.inf, 2, 3, 16, 7, 15],
    [7, np.inf, np.inf, 8, 1, np.inf, np.inf, np.inf, 14, np.inf, np.inf, 18, np.inf, 19],
    [13, np.inf, np.inf, np.inf, np.inf, 2, 9, 19, np.inf, 16, 11, 5, np.inf, 11],
    [np.inf, 17, 15, 18, np.inf, 7, np.inf, 15, 13, np.inf, 14, 2, np.inf, 19],
    [np.inf, np.inf, np.inf, 14, 7, 19, np.inf, np.inf, 9, 9, np.inf, np.inf, np.inf, np.inf],
    [np.inf, 3, 13, 15, 18, 17, np.inf, np.inf, 9, 4, np.inf, 12, 10, 14],
    [15, np.inf, 6, 19, 19, 19, np.inf, 1, 8, 4, 17, 14, np.inf, np.inf],
    [8, np.inf, 14, 7, 12, 6, 8, np.inf, 5, np.inf, 11, 11, np.inf, np.inf]
])

# Define the districts
districts = {
    1: (0, 3),
    2: (4, 5),
    3: (6, 13)
}

# Define the start and end workshops
start_workshop = (3, 13)
end_workshop = (4, 0)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    n = len(graph)
    dist = [np.inf] * n
    dist[start] = 0
    prev = [None] * n
    visited = [False] * n

    while not all(visited):
        min_dist = np.inf
        min_idx = None
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_idx = i

        visited[min_idx] = True

        for i in range(n):
            if not visited[i] and graph[min_idx][i] != np.inf:
                new_dist = dist[min_idx] + graph[min_idx][i]
                if new_dist < dist[i]:
                    dist[i] = new_dist
                    prev[i] = min_idx

    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return path

# Find the shortest path from start to end visiting at least one workshop in each district
shortest_path = None
for district in districts.values():
    for i in range(district[0], district[1] + 1):
        path1 = dijkstra_shortest_path(city_map, start_workshop[0] * city_map.shape[1] + start_workshop[1], i * city_map.shape[1])
        path2 = dijkstra_shortest_path(city_map, i * city_map.shape[1], end_workshop[0] * city_map.shape[1] + end_workshop[1])
        if shortest_path is None or len(path1) + len(path2) - 1 < len(shortest_path):
            shortest_path = path1[:-1] + path2

# Convert the indices to (row, col) tuples
shortest_path = [(idx // city_map.shape[1], idx % city_map.shape[1]) for idx in shortest_path]

print(shortest_path)
