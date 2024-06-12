
import numpy as np

# Define the matrix map of the city
city_map = np.array([
    [np.inf, np.inf, np.inf, 16, 11, 12, np.inf, np.inf, 17, 3, np.inf, np.inf, 4, 6],
    [4, 17, np.inf, np.inf, 3, np.inf, np.inf, 1, 9, 11, 12, 4, np.inf, np.inf],
    [5, np.inf, np.inf, 7, 14, 4, 5, 7, 13, 4, 7, np.inf, np.inf, np.inf],
    [6, 6, 19, 3, 15, np.inf, np.inf, np.inf, np.inf, 4, 10, 19, 2, 4],
    [3, 16, 8, np.inf, 5, np.inf, 12, 17, 16, np.inf, 9, 5, 6, np.inf],
    [17, 2, np.inf, np.inf, 16, np.inf, 5, np.inf, np.inf, 5, 17, 7, 2, 5],
    [19, np.inf, np.inf, np.inf, np.inf, 2, 15, 15, np.inf, 3, 11, np.inf, 4, np.inf],
    [np.inf, np.inf, 11, np.inf, np.inf, 17, 5, np.inf, 5, np.inf, np.inf, 19, 6, np.inf],
    [16, 17, 16, np.inf, 12, np.inf, 2, 18, 9, 7, np.inf, 13, np.inf, np.inf],
    [18, 11, np.inf, np.inf, 19, 5, np.inf, np.inf, 18, 4, np.inf, np.inf, np.inf, np.inf],
    [np.inf, np.inf, np.inf, np.inf, 2, 5, 4, 12, 3, np.inf, 4, 14, 7, 19],
    [18, np.inf, np.inf, np.inf, 7, 17, np.inf, np.inf, 3, 15, np.inf, 16, np.inf, 10],
    [np.inf, 11, 15, np.inf, np.inf, np.inf, np.inf, np.inf, 2, 13, np.inf, np.inf, np.inf, 3],
    [4, 8, np.inf, np.inf, np.inf, np.inf, 12, 13, np.inf, np.inf, 19, np.inf, 6, np.inf]
])

# Define the districts
districts = {
    1: (0, 2),
    2: (3, 6),
    3: (7, 13)
}

# Define the start and end workshops
start_workshop = (7, 12)
end_workshop = (2, 0)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra_shortest_path(graph, start, end):
    distances = {vertex: np.inf for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    vertices = graph.copy()

    while vertices:
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])
        vertices.remove(current_vertex)
        if distances[current_vertex] == np.inf:
            break
        for neighbor, weight in graph[current_vertex].items():
            alternative_route = distances[current_vertex] + weight
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_vertices[neighbor] = current_vertex

    path, current_vertex = [], end
    while previous_vertices[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]
    if path:
        path.insert(0, start)
    return path

# Create a graph representation of the city map
graph = {}
for i in range(city_map.shape[0]):
    for j in range(city_map.shape[1]):
        if city_map[i, j] != np.inf:
            neighbors = {}
            if i > 0 and city_map[i-1, j] != np.inf:
                neighbors[(i-1, j)] = city_map[i-1, j]
            if i < city_map.shape[0]-1 and city_map[i+1, j] != np.inf:
                neighbors[(i+1, j)] = city_map[i+1, j]
            if j > 0 and city_map[i, j-1] != np.inf:
                neighbors[(i, j-1)] = city_map[i, j-1]
            if j < city_map.shape[1]-1 and city_map[i, j+1] != np.inf:
                neighbors[(i, j+1)] = city_map[i, j+1]
            graph[(i, j)] = neighbors

# Find the shortest path from start to end workshop
shortest_path = dijkstra_shortest_path(graph, start_workshop, end_workshop)

# Filter the path to include at least 1 workshop in each district
filtered_path = []
district_workshops = {1: False, 2: False, 3: False}
for workshop in shortest_path:
    for district, (start, end) in districts.items():
        if start <= workshop[0] <= end:
            district_workshops[district] = True
    if all(district_workshops.values()):
        filtered_path.append(workshop)

print(filtered_path)
