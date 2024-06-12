
import numpy as np

# Define the matrix map of the city
city_map = np.array([[16, 2, 16, np.inf, 4, np.inf, np.inf, 1, 16, np.inf],
                      [np.inf, np.inf, 19, np.inf, 3, np.inf, 5, np.inf, np.inf, np.inf],
                      [np.inf, np.inf, np.inf, 3, np.inf, np.inf, 2, np.inf, 10, np.inf],
                      [11, 5, 20, np.inf, 1, 3, 1, np.inf, 9, np.inf],
                      [np.inf, np.inf, 8, 19, np.inf, 16, 9, np.inf, 16, 15],
                      [np.inf, 3, 5, 10, np.inf, np.inf, np.inf, 4, 1, np.inf],
                      [9, 18, 10, 17, 5, 6, np.inf, np.inf, np.inf, 5],
                      [np.inf, np.inf, 14, 5, 18, np.inf, np.inf, 1, 15, 1],
                      [13, np.inf, 13, 13, 14, 2, 19, 12, np.inf, 1],
                      [9, 6, np.inf, 4, 12, 1, 13, 8, 2, 13]])

# Define the districts
districts = {1: range(0, 4), 2: range(4, 7), 3: range(7, 10)}

# Define the start and end workshops
start_workshop = (7, 9)
end_workshop = (3, 2)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    n = len(graph)
    dist = [np.inf] * n
    dist[start] = 0
    prev = [None] * n
    visited = [False] * n

    for _ in range(n):
        u = min((i for i in range(n) if not visited[i]), key=lambda i: dist[i])
        visited[u] = True

        for v in range(n):
            if graph[u][v] + dist[u] < dist[v]:
                dist[v] = graph[u][v] + dist[u]
                prev[v] = u

    path = []
    while end is not None:
        path.insert(0, end)
        end = prev[end]

    return path

# Find the shortest path that satisfies the conditions
shortest_path = None
for district in districts.values():
    for workshop in district:
        path1 = dijkstra_shortest_path(city_map, start_workshop[0]*10 + start_workshop[1], workshop)
        path2 = dijkstra_shortest_path(city_map, workshop, end_workshop[0]*10 + end_workshop[1])
        if shortest_path is None or len(path1) + len(path2) - 1 < len(shortest_path):
            shortest_path = path1[:-1] + path2

# Convert the indices to tuples
shortest_path = [(index // 10, index % 10) for index in shortest_path]

print(shortest_path)
