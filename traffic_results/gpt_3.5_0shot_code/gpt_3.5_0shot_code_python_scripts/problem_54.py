
import numpy as np

# Define the matrix map of the city
city_map = np.array([
    [19, 14, 16, 4, 15, 16, 15, np.inf, 9, np.inf, np.inf, np.inf],
    [np.inf, 7, 12, 6, np.inf, 12, np.inf, 3, np.inf, 14, 5, 9],
    [1, 12, np.inf, np.inf, 12, np.inf, np.inf, np.inf, np.inf, np.inf, 10, 1],
    [np.inf, 1, 15, 14, np.inf, 2, 13, np.inf, np.inf, np.inf, 10, 9],
    [7, np.inf, 13, np.inf, 14, 1, 14, 8, np.inf, np.inf, 8, 5],
    [18, np.inf, 8, 13, 12, 13, np.inf, 12, 3, np.inf, 14, np.inf],
    [np.inf, 15, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 17, 10],
    [np.inf, 5, np.inf, 4, np.inf, np.inf, np.inf, 3, 5, 6, 6, 11],
    [np.inf, 15, 6, np.inf, 4, 18, np.inf, np.inf, 14, 10, 2, 8],
    [13, 10, 13, 7, 3, 6, np.inf, np.inf, 10, 17, 10, 15],
    [4, np.inf, np.inf, 7, 19, 4, 13, 13, 12, np.inf, np.inf, 13],
    [5, np.inf, np.inf, 9, 19, 18, np.inf, np.inf, 16, np.inf, 2, np.inf]
])

# Define the districts
districts = {
    1: (0, 3),
    2: (4, 8),
    3: (9, 11)
}

# Define the start and end workshops
start_workshop = (4, 11)
end_workshop = (9, 2)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    n = len(graph)
    dist = [np.inf] * n
    dist[start] = 0
    prev = [None] * n
    visited = [False] * n

    while not all(visited):
        min_dist = np.inf
        min_index = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i

        visited[min_index] = True

        for i in range(n):
            if not visited[i] and graph[min_index][i] != np.inf:
                new_dist = dist[min_index] + graph[min_index][i]
                if new_dist < dist[i]:
                    dist[i] = new_dist
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
    for i in range(district[0], district[1] + 1):
        for j in range(12):
            if city_map[i][j] != np.inf and city_map[end_workshop] != np.inf:
                path1 = dijkstra_shortest_path(city_map, start_workshop[0]*12 + start_workshop[1], i*12 + j)
                path2 = dijkstra_shortest_path(city_map, i*12 + j, end_workshop[0]*12 + end_workshop[1])
                if shortest_path is None or len(path1) + len(path2) - 1 < len(shortest_path):
                    shortest_path = path1 + path2[1:]

# Convert the indices to tuples
shortest_path = [(index // 12, index % 12) for index in shortest_path]

print(shortest_path)
