
import numpy as np

# Define the matrix map of the city
city_map = np.array([[17, np.inf, np.inf, np.inf, 5, np.inf, np.inf, 12, 16, np.inf, np.inf, 5, 16],
                     [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 12, 4, 6],
                     [9, np.inf, np.inf, np.inf, np.inf, np.inf, 19, np.inf, np.inf, 13, 6, 11, 19],
                     [1, np.inf, np.inf, np.inf, 13, np.inf, np.inf, np.inf, 3, 2, 7, 4, 3],
                     [np.inf, np.inf, np.inf, 14, 19, 20, 10, 13, 14, 2, np.inf, 9, 3],
                     [15, np.inf, 11, 7, np.inf, 11, 6, 16, np.inf, np.inf, np.inf, 8, 19],
                     [19, 16, 4, 8, 5, 5, 5, 11, 10, 17, 9, np.inf, 5],
                     [np.inf, 3, 17, np.inf, np.inf, 6, 17, 19, np.inf, np.inf, 14, np.inf, np.inf],
                     [np.inf, np.inf, np.inf, np.inf, np.inf, 14, np.inf, 10, 14, 13, np.inf, 13, np.inf],
                     [15, 5, 4, np.inf, np.inf, np.inf, np.inf, 2, 12, 6, np.inf, 16, 14],
                     [10, np.inf, np.inf, np.inf, 9, np.inf, np.inf, np.inf, np.inf, np.inf, 13, 2, np.inf],
                     [np.inf, np.inf, 17, np.inf, np.inf, np.inf, np.inf, 7, np.inf, np.inf, 16, np.inf, np.inf],
                     [12, 10, np.inf, 15, 16, np.inf, np.inf, 7, 11, 7, np.inf, 17, np.inf]])

# Define the districts
districts = {1: [0, 1], 2: [2, 3, 4, 5], 3: [6, 7, 8, 9, 10, 11, 12]}

# Define the start and end workshops
start_workshop = (1, 12)
end_workshop = (6, 3)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    nodes = set(range(len(graph)))
    dist = {node: np.inf for node in nodes}
    dist[start] = 0
    prev = {node: None for node in nodes}
    unvisited = nodes.copy()

    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)

        if dist[current] == np.inf:
            break

        for neighbor, weight in enumerate(graph[current]):
            if weight != np.inf:
                new_dist = dist[current] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    prev[neighbor] = current

    path = []
    current = end
    while prev[current] is not None:
        path.insert(0, current)
        current = prev[current]
    path.insert(0, start)

    return path

# Find the shortest path that satisfies the conditions
shortest_path = None
for workshop1 in districts[1]:
    for workshop2 in districts[2]:
        for workshop3 in districts[3]:
            path1 = dijkstra_shortest_path(city_map, start_workshop[0]*13 + start_workshop[1], workshop1)
            path2 = dijkstra_shortest_path(city_map, workshop1, workshop2)
            path3 = dijkstra_shortest_path(city_map, workshop2, workshop3)
            path4 = dijkstra_shortest_path(city_map, workshop3, end_workshop[0]*13 + end_workshop[1])
            
            if path1[-1] == workshop1 and path2[-1] == workshop2 and path3[-1] == workshop3 and path4[-1] == end_workshop[0]*13 + end_workshop[1]:
                shortest_path = path1[:-1] + path2[:-1] + path3[:-1] + path4
                break

# Convert the indices to coordinates
shortest_path_coords = [(index // 13, index % 13) for index in shortest_path]

print(shortest_path_coords)
