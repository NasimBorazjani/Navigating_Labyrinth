
import numpy as np

# Define the matrix map of the city
city_map = np.array([
    [0, 0, 17, 7, 0, 0, 11, 4, 5, 15, 17, 6, 6, 2],
    [17, 0, 0, 6, 0, 0, 0, 0, 1, 8, 0, 0, 0, 7],
    [0, 0, 0, 17, 4, 10, 6, 4, 0, 8, 16, 11, 0, 0],
    [0, 4, 0, 0, 10, 0, 8, 10, 0, 11, 0, 0, 1, 0],
    [0, 0, 11, 9, 4, 0, 8, 8, 0, 0, 0, 16, 13, 8],
    [0, 12, 3, 15, 13, 13, 0, 15, 19, 0, 2, 2, 6, 0],
    [15, 1, 0, 0, 0, 0, 5, 4, 0, 5, 12, 2, 5, 0],
    [20, 13, 7, 18, 8, 18, 5, 2, 17, 7, 11, 0, 15, 13],
    [4, 11, 0, 0, 10, 9, 0, 18, 14, 0, 19, 0, 0, 0],
    [19, 0, 2, 0, 18, 17, 10, 0, 0, 0, 13, 15, 0, 10],
    [16, 5, 2, 3, 13, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 17, 9, 0, 0, 0, 0, 0, 6, 0, 0],
    [11, 0, 0, 9, 14, 0, 0, 16, 0, 15, 13, 13, 15, 1],
    [9, 0, 0, 10, 14, 0, 0, 0, 0, 0, 0, 0, 1, 19]
])

# Define the districts
districts = {
    1: range(0, 5),
    2: range(5, 7),
    3: range(7, 14)
}

# Define the start and end workshops
start_workshop = (4, 12)
end_workshop = (7, 0)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    parents = {vertex: None for vertex in graph}
    visited = set()

    while visited != graph:
        current_vertex = None
        current_distance = float('infinity')
        for vertex, distance in distances.items():
            if vertex not in visited and distance < current_distance:
                current_vertex = vertex
                current_distance = distance

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_vertex

    path = []
    while end:
        path.append(end)
        end = parents[end]
    path.reverse()

    return path

# Create a graph representation of the city map
graph = {}
for i in range(city_map.shape[0]):
    for j in range(city_map.shape[1]):
        if city_map[i][j] != 0:
            neighbors = {}
            if i > 0 and city_map[i-1][j] != 0:
                neighbors[(i-1, j)] = city_map[i-1][j]
            if i < city_map.shape[0]-1 and city_map[i+1][j] != 0:
                neighbors[(i+1, j)] = city_map[i+1][j]
            if j > 0 and city_map[i][j-1] != 0:
                neighbors[(i, j-1)] = city_map[i][j-1]
            if j < city_map.shape[1]-1 and city_map[i][j+1] != 0:
                neighbors[(i, j+1)] = city_map[i][j+1]
            graph[(i, j)] = neighbors

# Find the shortest path from start to end workshop
shortest_path = dijkstra_shortest_path(graph, start_workshop, end_workshop)

# Filter the path to include at least one workshop from each district
filtered_path = []
district_workshops = {1: False, 2: False, 3: False}
for workshop in shortest_path:
    for district, rows in districts.items():
        if workshop[0] in rows and not district_workshops[district]:
            filtered_path.append(workshop)
            district_workshops[district] = True
            break

print(filtered_path)
