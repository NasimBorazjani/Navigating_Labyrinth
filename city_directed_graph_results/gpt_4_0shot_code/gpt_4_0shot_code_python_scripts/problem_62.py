
# Define the adjacency matrix
matrix = [
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
]

# Define the cities
cities = ['Z', 'C', 'M', 'X', 'N', 'A', 'B', 'L', 'U', 'K', 'G', 'Y', 'O']

# Define the start city
start = 'K'

# Define the destination cities
destinations = ['U', 'Y']

# Define the visited cities
visited = []

# Define the path
path = []

# Define the DFS function
def dfs(city, visited, path):
    # Add the city to the visited list
    visited.append(city)

    # Add the city to the path
    path.append(city)

    # If the path contains the destination cities twice, print the path
    if path.count(destinations[0]) == 2 and path.count(destinations[1]) == 2:
        print(path)

    # For each city connected to the current city
    for i in range(len(matrix[cities.index(city)])):
        # If the city is connected and has not been visited
        if matrix[cities.index(city)][i] == 1 and cities[i] not in visited:
            # Call the DFS function
            dfs(cities[i], visited, path)

    # Remove the city from the path
    path.pop()

    # Remove the city from the visited list
    visited.pop()

# Call the DFS function
dfs(start, visited, path)
