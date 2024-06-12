
import sys

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
]

# List of city names
city_names = list('OMULQPDASBKEVZ')

# Function to perform depth-first search
def dfs(city, path, visited):
    # Add current city to path
    path.append(city)
    # Mark current city as visited
    visited[city] = True

    # If we have visited all cities twice, we have found a solution
    if path.count(city_names[0]) == 2 and path.count(city_names[10]) == 2:
        return path

    # Try to visit each directly connected city
    for i in range(len(matrix[city])):
        if matrix[city][i] == 1 and (visited[i] == False or (i == 0 or i == 10)):
            result = dfs(i, path, visited)
            # If we have found a solution, return it
            if result is not None:
                return result

    # Backtrack: remove current city from path and mark it as unvisited
    path.pop()
    visited[city] = False

    return None

# Start from city 'M'
result = dfs(city_names.index('M'), [], [False]*len(city_names))

# Print result
print(result)
