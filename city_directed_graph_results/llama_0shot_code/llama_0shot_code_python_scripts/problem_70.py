
import sys

# Adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Convert the adjacency matrix into a dictionary
graph = {city: [] for city in 'KIEBYJUDFLACXV'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i + ord('A'))].append(chr(j + ord('A')))

# Recursive function for depth-first search
def dfs(city, cities_left, path):
    if not cities_left:
        if city == 'V':
            return path
        else:
            return None
    else:
        shortest_path = None
        for next_city in graph[city]:
            if next_city in cities_left:
                new_path = dfs(next_city, cities_left - {next_city}, path + [next_city])
                if new_path is not None:
                    if shortest_path is None or len(new_path) < len(shortest_path):
                        shortest_path = new_path
        return shortest_path

# Find the quickest route
cities_to_visit = {'E', 'U'}
start_city = 'V'
shortest_path = dfs(start_city, cities_to_visit, [start_city])

# Print the solution
if shortest_path is None:
    print("No solution found.")
else:
    print("Shortest path:", shortest_path)
