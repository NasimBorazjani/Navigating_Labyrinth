
import numpy as np

# Define the matrix map of the city
city_map = [
    [np.inf, np.inf, 7, 18, 11, 4, 9, np.inf, 15, np.inf, np.inf, np.inf, 1, np.inf, np.inf],
    [np.inf, np.inf, 14, np.inf, 10, np.inf, np.inf, np.inf, 8, np.inf, np.inf, 16, 1, np.inf, np.inf],
    [17, 17, np.inf, np.inf, np.inf, np.inf, np.inf, 7, 6, 12, np.inf, np.inf, np.inf, 7, np.inf],
    [np.inf, np.inf, np.inf, np.inf, 10, np.inf, np.inf, 18, 1, 11, 4, np.inf, 13, 10, 16],
    [np.inf, np.inf, np.inf, 12, 1, np.inf, np.inf, np.inf, 2, 7, 1, np.inf, 2, np.inf, 5],
    [np.inf, np.inf, 8, np.inf, 12, np.inf, np.inf, 5, 17, np.inf, 2, np.inf, 4, 10, 18],
    [np.inf, np.inf, 4, 19, 1, np.inf, 18, 7, np.inf, 10, 3, np.inf, 19, 16, 19],
    [6, 12, 15, 16, 5, 9, 16, 18, 10, 15, 5, np.inf, 5, 14, np.inf],
    [np.inf, 16, 8, 17, 12, 11, 16, 8, 9, 9, 7, 4, 5, 20, 3],
    [19, 17, 15, np.inf, np.inf, 17, np.inf, 3, 2, 2, 11, 7, 8, 16, 1],
    [13, 4, 17, np.inf, np.inf, np.inf, np.inf, 5, np.inf, 18, 16, 15, 19, 4, np.inf],
    [11, np.inf, np.inf, np.inf, np.inf, 12, np.inf, np.inf, np.inf, np.inf, np.inf, 19, np.inf, np.inf, np.inf],
    [18, np.inf, np.inf, np.inf, 9, 19, np.inf, 16, 6, np.inf, 9, 3, 16, 15, np.inf],
    [np.inf, np.inf, np.inf, 10, np.inf, np.inf, 4, 3, np.inf, 3, np.inf, 16, 18, np.inf, 12],
    [np.inf, 13, np.inf, np.inf, np.inf, np.inf, np.inf, 10, 5, np.inf, 17, np.inf, np.inf, 7, np.inf]
]

# Define the districts
districts = {
    1: [0, 1, 2, 3, 4],
    2: [5, 6, 7, 8],
    3: [9, 10, 11, 12, 13, 14]
}

# Define the start and end workshops
start_workshop = (7, 2)
end_workshop = (4, 14)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    n = len(graph)
    dist = [np.inf] * n
    dist[start] = 0
    prev = [None] * n
    unvisited = set(range(n))

    while unvisited:
        u = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(u)

        for v in range(n):
            if graph[u][v] + dist[u] < dist[v]:
                dist[v] = graph[u][v] + dist[u]
                prev[v] = u

    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = prev[current]

    return path

# Find the shortest path from start to end visiting at least one workshop in each district
shortest_path = []
for district in districts.values():
    for workshop in district:
        path_to_workshop = dijkstra_shortest_path(city_map, start_workshop[0]*15 + start_workshop[1], workshop)
        if path_to_workshop:
            for next_workshop in district:
                if next_workshop != workshop:
                    path_to_end = dijkstra_shortest_path(city_map, workshop, end_workshop[0]*15 + end_workshop[1])
                    if path_to_end:
                        shortest_path = path_to_workshop + path_to_end[1:]
                        break
        if shortest_path:
            break
    if shortest_path:
        break

# Convert the indices to coordinates
shortest_path_coords = [(workshop // 15, workshop % 15) for workshop in shortest_path]

print(shortest_path_coords)
