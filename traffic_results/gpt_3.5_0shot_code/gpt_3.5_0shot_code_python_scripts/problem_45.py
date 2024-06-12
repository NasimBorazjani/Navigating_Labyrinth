
import numpy as np

# Define the matrix map of the city
city_map = [
    [np.inf, np.inf, 17, 12, 12, 10, 9, 9, 18, np.inf, 1],
    [np.inf, 8, np.inf, 9, np.inf, np.inf, 18, 5, 1, 12, 14],
    [2, 19, 4, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 15, np.inf],
    [17, 8, 6, np.inf, np.inf, 10, 15, np.inf, np.inf, np.inf, 13],
    [np.inf, np.inf, np.inf, 9, 17, np.inf, np.inf, np.inf, np.inf, 12, 17],
    [np.inf, 20, 3, 1, 14, 8, 9, 20, 10, 8, 8],
    [18, 19, 4, 12, 3, 1, np.inf, np.inf, 20, 6, 3],
    [4, 6, 9, np.inf, 8, 10, np.inf, np.inf, 6, 9, 6],
    [15, np.inf, np.inf, np.inf, np.inf, np.inf, 16, np.inf, 15, 4, np.inf],
    [np.inf, np.inf, np.inf, 4, np.inf, np.inf, np.inf, 13, np.inf, np.inf, np.inf],
    [np.inf, 3, np.inf, np.inf, np.inf, np.inf, 1, np.inf, np.inf, 5, 13]
]

# Define the districts
districts = {
    1: (0, 3),
    2: (4, 5),
    3: (6, 10)
}

# Define the start and end workshops
start_workshop = (3, 10)
end_workshop = (6, 1)

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
        for j in range(len(city_map[i])):
            if city_map[i][j] != np.inf and (i, j) != start_workshop and (i, j) != end_workshop:
                path1 = dijkstra(city_map, start_workshop[0]*len(city_map[0]) + start_workshop[1], i*len(city_map[0]) + j)
                path2 = dijkstra(city_map, i*len(city_map[0]) + j, end_workshop[0]*len(city_map[0]) + end_workshop[1])
                if shortest_path is None or len(path1) + len(path2) - 1 < len(shortest_path):
                    shortest_path = path1[:-1] + path2

# Convert the path to a list of tuples
path_tuples = [(p // len(city_map[0]), p % len(city_map[0])) for p in shortest_path]

print(path_tuples)
