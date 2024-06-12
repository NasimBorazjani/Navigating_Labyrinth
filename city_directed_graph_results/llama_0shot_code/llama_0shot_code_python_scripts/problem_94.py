
# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0]
]

# Convert the adjacency matrix into a dictionary
graph = {chr(i+65): [chr(j+65) for j in range(len(matrix)) if matrix[i][j] == 1] for i in range(len(matrix))}

# Cities to visit twice
visit_twice = ['H', 'R']

# Recursive function for depth-first search
def dfs(city, visited, to_visit_twice):
    visited.append(city)
    if len(visited) == len(matrix):
        solutions.append(visited[:])
    else:
        for next_city in graph[city]:
            if next_city not in visited:
                dfs(next_city, visited, to_visit_twice)
    visited.pop()

# List of all solutions
solutions = []

# Start from city 'I'
dfs('I', [], visit_twice)

# The quickest route is the first solution
quickest_route = solutions[0]

# Print the quickest route in Python syntax
print(quickest_route)
