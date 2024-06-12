
import sys

# The adjacency matrix
matrix = [
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
]

# The list of cities
cities = ['S', 'X', 'G', 'E', 'P', 'B', 'O', 'C', 'L', 'J', 'M', 'Y', 'T', 'W']

# The current city and the destination cities
current_city = 'Y'
destinations = ['B', 'M']

# The visited cities
visited = [current_city]

# The path
path = []

# The function to perform the depth-first search
def dfs(city):
    global path
    if city in destinations and city not in path:
        path.append(city)
        return True
    for i, connected in enumerate(matrix[cities.index(city)]):
        if connected == 1 and cities[i] not in visited:
            visited.append(cities[i])
            if dfs(cities[i]):
                path.append(cities[i])
                return True
            visited.remove(cities[i])
    return False

# Perform the depth-first search
dfs(current_city)

# Print the path
print(path)
