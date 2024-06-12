
import numpy as np

# Define the matrix map of the city
city_map = [
    ['x', 3, 11, 7, 'x', 'x', 1, 3, 'x', 'x', 'x', 3],
    ['x', 10, 'x', 'x', 3, 9, 7, 8, 'x', 2, 'x', 17],
    [6, 16, 'x', 18, 10, 5, 'x', 6, 'x', 'x', 7, 'x'],
    ['x', 10, 'x', 8, 13, 10, 'x', 'x', 'x', 'x', 6, 13],
    [6, 11, 3, 16, 8, 15, 'x', 'x', 'x', 13, 12, 20],
    [15, 'x', 16, 'x', 17, 13, 'x', 'x', 8, 6, 19, 9],
    [14, 10, 16, 14, 'x', 'x', 10, 11, 19, 15, 17, 'x'],
    ['x', 'x', 'x', 'x', 18, 13, 14, 19, 12, 1, 3, 'x'],
    [15, 1, 3, 17, 4, 18, 'x', 18, 2, 7, 12, 'x'],
    [19, 'x', 13, 17, 2, 14, 8, 'x', 'x', 8, 16, 'x'],
    ['x', 19, 'x', 15, 'x', 18, 'x', 13, 'x', 13, 'x', 'x'],
    [7, 14, 2, 'x', 10, 3, 'x', 'x', 2, 5, 10, 'x']
]

# Convert 'x' to a large number to represent closed workshops
city_map = [[1000 if x == 'x' else x for x in row] for row in city_map]

# Define the districts
districts = {
    1: (0, 4),
    2: (5, 8),
    3: (9, 11)
}

# Define the start and end workshops
start_workshop = (8, 1)
end_workshop = (5, 11)

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    vertices = graph.copy()

    while vertices:
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])
        vertices.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    path = []
    current_vertex = end
    while current_vertex != start:
        path.insert(0, current_vertex)
        for neighbor, weight in graph[current_vertex].items():
            if distances[current_vertex] == distances[neighbor] + weight:
                current_vertex = neighbor
                break
    path.insert(0, start)
    return path

# Create a graph representation of the city map
graph = {}
for i in range(len(city_map)):
    for j in range(len(city_map[0])):
        if city_map[i][j] != 1000:
            graph[(i, j)] = {}
            if i > 0 and city_map[i-1][j] != 1000:
                graph[(i, j)][(i-1, j)] = city_map[i-1][j]
            if i < len(city_map)-1 and city_map[i+1][j] != 1000:
                graph[(i, j)][(i+1, j)] = city_map[i+1][j]
            if j > 0 and city_map[i][j-1] != 1000:
                graph[(i, j)][(i, j-1)] = city_map[i][j-1]
            if j < len(city_map[0])-1 and city_map[i][j+1] != 1000:
                graph[(i, j)][(i, j+1)] = city_map[i][j+1]

# Find the shortest path that satisfies the conditions
shortest_path = []
for district in districts.values():
    for i in range(district[0], district[1]+1):
        for j in range(len(city_map[0])):
            if (i, j) in graph:
                path = dijkstra(graph, start_workshop, (i, j))
                if end_workshop in path:
                    shortest_path += path
                    start_workshop = (i, j)
                    break
        if start_workshop == (i, j):
            break

print(shortest_path)
