
import numpy as np

# Define the matrix map of the city
city_map = np.array([[15, 1, -1, 3, -1, 9, 15, 8, 17, -1, -1, 6, -1, 12, 3],
                      [-1, -1, -1, 14, -1, 7, 18, 6, 14, 2, 19, 15, -1, -1, -1],
                      [4, 3, -1, 10, 8, 4, 16, 13, 6, -1, 18, 10, 14, -1, -1],
                      [-1, -1, -1, 10, -1, 14, 10, 7, -1, -1, -1, 4, 2, 19, 3],
                      [5, -1, 10, -1, 18, 12, 20, 15, -1, -1, 11, 11, 1, 10, 19],
                      [8, -1, 13, -1, -1, -1, 16, 7, 3, -1, -1, 2, 18, 11, -1],
                      [12, -1, 15, -1, -1, 6, -1, -1, -1, -1, 18, 3, 14, 3, 6],
                      [-1, 6, 13, 19, 19, -1, 7, 12, 18, 5, -1, 1, 4, 18, 11],
                      [5, -1, 18, -1, 12, 4, 3, 7, -1, 16, 1, -1, 16, 2, -1],
                      [-1, -1, -1, -1, 18, -1, -1, 14, 15, 1, -1, -1, 9, -1, -1],
                      [-1, 13, -1, 7, 7, -1, -1, 16, 10, -1, -1, -1, -1, 8, -1],
                      [-1, -1, 19, 18, 8, 18, -1, -1, 12, -1, 13, -1, 17, 12, 7],
                      [-1, -1, -1, -1, 7, 7, 13, 17, -1, -1, -1, -1, -1, 9, 5],
                      [9, -1, 14, -1, 9, -1, 8, -1, -1, -1, 17, 4, 12, 12, 12],
                      [8, 1, 11, -1, -1, -1, -1, -1, 15, -1, -1, 2, 16, -1, 15]])

# Define the districts
districts = {1: [0, 1, 2], 2: [3, 4, 5, 6], 3: [7, 8, 9, 10, 11, 12, 13, 14]}

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    nodes = set(range(len(graph)))
    dist = {node: float('inf') for node in nodes}
    dist[start] = 0
    prev = {node: None for node in nodes}
    unvisited = nodes.copy()

    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)

        if current == end:
            path = []
            while prev[current] is not None:
                path.insert(0, current)
                current = prev[current]
            path.insert(0, start)
            return path

        for neighbor, weight in enumerate(graph[current]):
            if weight > 0 and neighbor in unvisited:
                new_dist = dist[current] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = current

    return None

# Find the shortest path from Ben's current workshop to destination workshop
path = []
for district in districts.values():
    for start in district:
        for end in district:
            if start != end:
                temp_path = dijkstra_shortest_path(city_map, start, end)
                if temp_path is not None:
                    path += temp_path
                    break
    if len(path) == 0:
        break

print([(index // 15, index % 15) for index in path])
