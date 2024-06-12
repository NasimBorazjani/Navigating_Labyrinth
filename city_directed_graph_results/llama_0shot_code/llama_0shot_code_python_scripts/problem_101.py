
import sys

# The adjacency matrix
adj_matrix = [
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
]

# The list of cities
cities = ['S', 'Z', 'I', 'R', 'P', 'T', 'X', 'B', 'F', 'A', 'L', 'M', 'G', 'N', 'E']

# The start city
start = 'P'

# The destination cities
destinations = ['I', 'N']

# The minimum time
min_time = sys.maxsize

# The shortest path
shortest_path = []

# The visited cities
visited = {city: 0 for city in cities}

# The current path
current_path = [start]

# The DFS function
def dfs(current_city):
    global min_time, shortest_path
    if current_city in destinations:
        visited[current_city] += 1
        if visited[current_city] == 2:
            current_time = len(current_path)
            if current_time < min_time:
                min_time = current_time
                shortest_path = current_path[:]
    else:
        for i, adj in enumerate(adj_matrix[cities.index(current_city)]):
            if adj == 1 and visited[cities[i]] < 2:
                current_path.append(cities[i])
                dfs(cities[i])
                current_path.pop()

# Start the DFS from the start city
dfs(start)

# Print the shortest path
print(shortest_path)
