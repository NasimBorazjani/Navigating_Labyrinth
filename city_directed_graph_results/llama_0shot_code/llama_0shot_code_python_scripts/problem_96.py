
# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0]
]

# Create a dictionary of lists from the matrix
graph = {city: [] for city in 'ROJEYALTKCNBZXS'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i+65)].append(chr(j+65))

# DFS function
def dfs(city, path):
    path = path + city
    if len(path) == len(graph)*2:  # If all cities are visited twice
        solutions.append(path)
    else:
        for neighbor in graph[city]:  # Visit each neighbor
            if neighbor not in path:  # If the neighbor is not visited yet
                dfs(neighbor, path)

# List to store all possible solutions
solutions = []

# Start from city 'O'
dfs('O', '')

# Print the quickest route
print(min(solutions, key=len))
