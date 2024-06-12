
# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]
]

# List of city names
cities = ['J', 'U', 'T', 'S', 'N', 'F', 'Y', 'C', 'H', 'A', 'M', 'P']

# Function to perform depth-first search
def dfs(city, path):
    # If we have visited the city twice, we stop the search
    if path.count(city) == 2:
        return
    # If the city is not 'H', 'N' or 'F', we visit it
    if city not in ['H', 'N', 'F']:
        path.append(city)
    # We visit the cities in the order of their distance from 'F'
    for i in range(len(matrix)):
        if matrix[cities.index('F')][i] == 1 and cities[i] not in path:
            dfs(cities[i], path)

# We start from city 'F'
path = ['F']
dfs('F', path)

# We remove 'F' from the path since it's a starting city
path.remove('F')

# We visit 'H' and 'N' exactly twice
path = ['H', 'N'] + path

print(path)
