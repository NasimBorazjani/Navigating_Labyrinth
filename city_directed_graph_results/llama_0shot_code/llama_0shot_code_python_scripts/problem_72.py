
import itertools

# Adjacency matrix
matrix = [
    "0111000101000",
    "0000100000110",
    "0100000111011",
    "0000001000100",
    "0000000010010",
    "1000000100010",
    "0100010000000",
    "0011100011100",
    "0101000100000",
    "1000111000110",
    "0000000111000",
    "1111101100110",
    "0011011100010",
]

# Convert the adjacency matrix into a dictionary
graph = {city: [] for city in 'FZMQLIVJDNBEO'}
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == '1':
            graph[chr(i + ord('A'))].append(chr(j + ord('A')))

# Recursive function for depth-first search
def dfs(city, visited, path):
    visited[city] += 1
    path.append(city)
    
    # Check if we have visited 'M' or 'L' twice
    if (city in ('M', 'L') and visited[city] == 2) or len(path) == len(graph):
        # Record the time it takes to reach this solution
        times.append((path.copy(), visited.copy()))
    else:
        # Visit each neighbor that has not been visited yet
        for neighbor in graph[city]:
            if neighbor not in visited or visited[neighbor] < 2:
                dfs(neighbor, visited, path)
    
    # Backtrack
    path.pop()
    visited[city] -= 1

# Initialize the visited dictionary and the list of times
visited = {city: 0 for city in graph}
times = []

# Perform depth-first search
dfs('Q', visited, [])

# Find the quickest route
quickest_route = min(times, key=lambda x: sum(visited[city] for city in x[0] if city in ('M', 'L')))

# Print the solution as a list of city names
print(quickest_route[0])
