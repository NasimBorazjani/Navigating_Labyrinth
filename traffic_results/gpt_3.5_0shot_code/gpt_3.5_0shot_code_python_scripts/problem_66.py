
import numpy as np

# Define the matrix map of the city
city_map = [
    [np.inf, 17, 14, 18, np.inf, np.inf, 8, 18, 10, 5, 5, np.inf, np.inf],
    [np.inf, np.inf, np.inf, np.inf, 17, 18, 17, 17, 6, 12, np.inf, 7, 16],
    [17, np.inf, 17, 6, 18, np.inf, 10, 13, 10, 19, 15, 4, 13],
    [15, 5, 15, 3, 17, 3, np.inf, np.inf, 18, 15, 19, 3, 2],
    [np.inf, np.inf, np.inf, np.inf, 2, 10, np.inf, np.inf, np.inf, 18, 14, 5, 12],
    [np.inf, 16, np.inf, 12, 4, 7, np.inf, np.inf, 9, np.inf, np.inf, np.inf, np.inf],
    [np.inf, 7, np.inf, np.inf, 16, 2, 9, 1, 3, np.inf, np.inf, 4, np.inf],
    [15, 16, np.inf, 10, 1, 16, np.inf, np.inf, 2, 18, 1, np.inf, np.inf],
    [np.inf, np.inf, 8, 3, np.inf, 19, np.inf, np.inf, np.inf, 5, 9, np.inf, np.inf],
    [np.inf, 8, 12, 14, np.inf, np.inf, np.inf, 16, np.inf, 8, np.inf, 3, 2],
    [8, 1, np.inf, np.inf, np.inf, np.inf, 13, np.inf, np.inf, np.inf, 9, np.inf, 12],
    [np.inf, np.inf, 3, 3, 11, np.inf, np.inf, 16, np.inf, np.inf, 5, np.inf, np.inf],
    [np.inf, 11, 17, np.inf, np.inf, np.inf, 9, np.inf, np.inf, 2, 15, np.inf]
]

# Define the districts
districts = {
    1: (0, 3),
    2: (4, 8),
    3: (9, 12)
}

# Define the start and end workshops
start_workshop = (3, 10)
end_workshop = (9, 2)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    n = len(city_map)
    dist = [np.inf] * n
    dist[start] = 0
    prev = [None] * n
    visited = set()

    while len(visited) < n:
        u = min((v for v in range(n) if v not in visited), key=lambda x: dist[x])
        visited.add(u)

        for v in range(n):
            if city_map[u][v] != np.inf and dist[u] + city_map[u][v] < dist[v]:
                dist[v] = dist[u] + city_map[u][v]
                prev[v] = u

    path = []
    u = end
    while u is not None:
        path.insert(0, u)
        u = prev[u]

    return path

# Find the shortest path that satisfies the conditions
shortest_path = None
for district in districts.values():
    for i in range(district[0], district[1] + 1):
        path1 = dijkstra(city_map, start_workshop[0]*13 + start_workshop[1], i)
        for j in range(district[0], district[1] + 1):
            path2 = dijkstra(city_map, i, j)
            path3 = dijkstra(city_map, j, end_workshop[0]*13 + end_workshop[1])
            if path1 and path2 and path3:
                if shortest_path is None or len(path1) + len(path2) + len(path3) < len(shortest_path):
                    shortest_path = path1 + path2[1:] + path3

# Convert the indices to (row, column) tuples
shortest_path = [(index // 13, index % 13) for index in shortest_path]

print(shortest_path)
