
import numpy as np

# Create the matrix map of the city
city_map = np.array([[7, 6, 11, np.inf, np.inf, np.inf, 19, np.inf, 9, 15, 12, 8, 10, 15, 5],
                     [9, 14, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 18, 2, 11, np.inf, 10],
                     [14, 5, np.inf, np.inf, 4, 4, 12, np.inf, 18, np.inf, 17, 11, 3, 18, 19],
                     [18, 17, np.inf, 8, np.inf, np.inf, 9, np.inf, np.inf, 8, 19, 10, np.inf, np.inf, np.inf],
                     [7, np.inf, np.inf, 11, 4, np.inf, np.inf, 10, 1, 2, 3, 12, 8, 12, 15],
                     [np.inf, 3, 7, 8, np.inf, np.inf, np.inf, np.inf, 4, 16, 13, 19, 14, 10, 13],
                     [18, 1, 2, np.inf, 16, 20, 5, np.inf, 2, 4, 20, 12, 14, 18, 16],
                     [1, np.inf, 1, np.inf, 15, 19, 11, 9, 19, 16, np.inf, np.inf, np.inf, np.inf, 19],
                     [np.inf, 8, np.inf, 1, 7, np.inf, 2, 3, np.inf, np.inf, np.inf, 1, 3, np.inf, np.inf],
                     [6, 16, np.inf, 3, np.inf, 18, np.inf, 2, 18, np.inf, np.inf, 16, np.inf, np.inf, 8],
                     [np.inf, 9, np.inf, 5, 2, np.inf, np.inf, np.inf, np.inf, 17, np.inf, 6, 18, 14, np.inf],
                     [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 18, np.inf, np.inf, 3, np.inf, 10, np.inf, np.inf],
                     [np.inf, 2, 15, np.inf, 5, 15, 18, 8, 19, np.inf, np.inf, np.inf, np.inf, np.inf, 10],
                     [np.inf, np.inf, 4, np.inf, 7, 2, 2, np.inf, 19, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
                     [17, np.inf, np.inf, np.inf, 5, np.inf, np.inf, np.inf, 4, 1, 18, np.inf, 9, 2, 8]])

# Define the districts
districts = {1: range(0, 5), 2: range(5, 8), 3: range(8, 15)}

# Define the start and end workshops
start_workshop = (4, 14)
end_workshop = (8, 3)

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

        for neighbor in nodes - set(path for path, time in enumerate(graph[current]) if time == np.inf):
            alt = dist[current] + graph[current][neighbor]
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current

    return None

# Find the shortest path that satisfies the conditions
shortest_path = None
for district1_workshop in districts[1]:
    for district2_workshop in districts[2]:
        for district3_workshop in districts[3]:
            path1 = dijkstra_shortest_path(city_map, start_workshop[0]*15 + start_workshop[1], district1_workshop)
            path2 = dijkstra_shortest_path(city_map, district1_workshop, district2_workshop)
            path3 = dijkstra_shortest_path(city_map, district2_workshop, district3_workshop)
            path4 = dijkstra_shortest_path(city_map, district3_workshop, end_workshop[0]*15 + end_workshop[1])

            if path1 and path2 and path3 and path4:
                path = path1[:-1] + path2[:-1] + path3[:-1] + path4
                if shortest_path is None or len(path) < len(shortest_path):
                    shortest_path = path

# Convert the indices to coordinates
shortest_path_coords = [(index // 15, index % 15) for index in shortest_path]

print(shortest_path_coords)
