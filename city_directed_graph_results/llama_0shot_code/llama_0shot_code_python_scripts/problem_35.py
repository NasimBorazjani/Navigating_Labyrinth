
# Adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Convert matrix to dictionary
graph = {city: [] for city in 'AVNQPSEMLHWG'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i+65)].append(chr(j+65))

# DFS function
def dfs(city, path, visited):
    # Add city to path and mark as visited
    path.append(city)
    visited[city] = True

    # If city is 'P' or 'L', check if we've visited twice
    if city in ('P', 'L') and path.count(city) == 2:
        # Check if this path is quicker
        global quickest_path
        if len(path) < len(quickest_path):
            quickest_path = path[:]

    # If we've visited all cities except 'P' and 'L' once, visit 'P' and 'L'
    elif set(graph.keys()) - visited.keys() == {'P', 'L'}:
        for dest in ('P', 'L'):
            if not visited.get(dest, False):
                dfs(dest, path, visited)

    # Visit unvisited cities
    else:
        for next_city in graph[city]:
            if not visited.get(next_city, False):
                dfs(next_city, path, visited)

    # Backtrack
    path.pop()
    visited[city] = False

# Start DFS from 'G'
quickest_path = []
dfs('G', [], {})

# Print quickest path
print(quickest_path)
