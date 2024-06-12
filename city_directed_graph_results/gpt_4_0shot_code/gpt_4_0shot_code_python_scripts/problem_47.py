
# Define the adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
]

# Define the cities
cities = ['Z', 'O', 'F', 'M', 'C', 'K', 'B', 'U', 'D', 'R', 'S', 'J']

# Define the start city
start = 'Z'

# Define the destination cities
destinations = ['C', 'D']

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
        # If the city is connected and has not been visited or is a destination city
        if matrix[cities.index(city)][i] == 1 and (cities[i] not in visited or cities[i] in destinations):
            # Call the DFS function
            dfs(cities[i], visited, path)

    # Remove the city from the path
    path.pop()

    # Remove the city from the visited list
    visited.remove(city)

# Call the DFS function
dfs(start, visited, path)
