
import numpy as np

# Define the matrix map of the city
city_map = [
    [np.inf, 2, np.inf, 12, 3, 8, np.inf, 1, 5, np.inf, np.inf, 14, np.inf, 5, np.inf],
    [5, np.inf, np.inf, 9, 19, 10, 10, np.inf, np.inf, 14, 16, np.inf, np.inf, 17, np.inf],
    [7, 4, 7, 18, 2, 7, 16, np.inf, 7, np.inf, 9, np.inf, np.inf, 6, np.inf],
    [9, np.inf, 14, np.inf, np.inf, 14, 7, 9, 18, 11, 14, 8, 13, 14, 15],
    [8, 4, np.inf, 17, np.inf, 7, 15, np.inf, np.inf, 19, np.inf, 10, np.inf, 12, 13],
    [7, 11, 5, 6, np.inf, 13, np.inf, np.inf, 15, 4, 9, 17, 19, 6, 8],
    [13, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 4, 10, np.inf, 7, 7, 17, 9],
    [np.inf, np.inf, 6, np.inf, np.inf, 17, 12, 11, np.inf, np.inf, np.inf, 10, 15, 14, np.inf],
    [16, np.inf, 5, 19, np.inf, 19, np.inf, 4, 11, 16, np.inf, np.inf, 12, np.inf, np.inf],
    [np.inf, np.inf, 14, np.inf, np.inf, 19, np.inf, np.inf, 4, 13, 7, np.inf, np.inf, np.inf, 8],
    [np.inf, 4, np.inf, 13, 7, 14, np.inf, np.inf, 2, 15, 9, 11, np.inf, np.inf, np.inf],
    [np.inf, np.inf, np.inf, np.inf, np.inf, 19, np.inf, 6, 2, np.inf, np.inf, np.inf, 4, 7, np.inf],
    [17, 12, 10, 3, 5, 18, np.inf, np.inf, np.inf, 11, np.inf, 19, 13, np.inf, np.inf],
    [1, np.inf, 5, np.inf, 17, np.inf, 17, np.inf, 7, 18, np.inf, np.inf, 8, np.inf, np.inf],
    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 2, 9, np.inf, 10, 3, np.inf, np.inf, 15, 2]
]

# Define the districts
districts = {
    1: (0, 2),
    2: (3, 6),
    3: (7, 14)
}

# Define the start and end workshops
start_workshop = (3, 2)
end_workshop = (7, 13)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(city_map, start, end):
    n = len(city_map)
    dist = [np.inf] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        u = min((i for i in range(n) if not visited[i]), key=lambda x: dist[x])
        visited[u] = True

        for v in range(n):
            if not visited[v] and city_map[u][v] != np.inf:
                dist[v] = min(dist[v], dist[u] + city_map[u][v])

    path = [end]
    while end != start:
        for i in range(n):
            if city_map[i][end] != np.inf and dist[end] == dist[i] + city_map[i][end]:
                path.append(i)
                end = i
                break

    return path[::-1]

# Find the shortest path that satisfies the conditions
shortest_path = []
for district in districts.values():
    path = dijkstra(city_map, start_workshop[0]*15 + start_workshop[1], end_workshop[0]*15 + end_workshop[1])
    shortest_path.extend(path)
    start_workshop = (path[-1] // 15, path[-1] % 15)

print([(workshop // 15, workshop % 15) for workshop in shortest_path])
