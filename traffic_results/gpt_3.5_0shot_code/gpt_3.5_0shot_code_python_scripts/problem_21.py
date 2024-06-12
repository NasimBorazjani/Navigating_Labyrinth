
import numpy as np

# Define the matrix map of the city
city_map = np.array([[15, 4, 9, 10, 19, np.inf, 12, 4, np.inf, 15],
                      [12, 19, 11, np.inf, np.inf, np.inf, np.inf, 7, 6, 3],
                      [4, np.inf, 8, np.inf, np.inf, 19, np.inf, 11, 1, 6],
                      [np.inf, np.inf, 5, np.inf, np.inf, np.inf, 12, 6, 6, np.inf],
                      [np.inf, 14, np.inf, np.inf, 14, 11, 2, 9, 6, 14],
                      [8, 8, 5, 17, 7, np.inf, 1, 2, np.inf, 6],
                      [18, np.inf, np.inf, 15, np.inf, 15, 4, np.inf, np.inf, 7],
                      [19, np.inf, 10, 18, 14, np.inf, 14, 9, 8, 6],
                      [19, np.inf, 14, np.inf, 10, 8, 15, np.inf, 15, np.inf],
                      [12, 1, np.inf, 5, 3, 3, np.inf, np.inf, np.inf, np.inf]])

# Define the districts
districts = {1: [0, 1], 2: [2, 6], 3: [7, 9]}

# Define the start and end workshops
start_workshop = (1, 9)
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

        if current == end:
            path = []
            while prev[current] is not None:
                path.insert(0, current)
                current = prev[current]
            path.insert(0, start)
            return path

        for neighbor in nodes - set(path for path, _ in path):
            if graph[current][neighbor] + dist[current] < dist[neighbor]:
                dist[neighbor] = graph[current][neighbor] + dist[current]
                prev[neighbor] = current

    return None

# Find the shortest path that satisfies the conditions
shortest_path = None
for workshop_1 in districts[1]:
    for workshop_2 in districts[2]:
        for workshop_3 in districts[3]:
            path_1 = dijkstra_shortest_path(city_map, start_workshop, workshop_1)
            path_2 = dijkstra_shortest_path(city_map, workshop_1, workshop_2)
            path_3 = dijkstra_shortest_path(city_map, workshop_2, workshop_3)
            path_4 = dijkstra_shortest_path(city_map, workshop_3, end_workshop)

            if path_1 and path_2 and path_3 and path_4:
                path = path_1[:-1] + path_2[:-1] + path_3[:-1] + path_4
                if shortest_path is None or len(path) < len(shortest_path):
                    shortest_path = path

# Print the shortest path
print(shortest_path)
