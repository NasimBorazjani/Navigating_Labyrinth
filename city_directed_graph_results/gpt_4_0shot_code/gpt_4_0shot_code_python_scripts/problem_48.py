
# Define the adjacency matrix
matrix = [
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
]

# Define the cities
cities = ['A', 'Q', 'S', 'O', 'N', 'V', 'I', 'X', 'D', 'B', 'E', 'Y']

# Define the start city
start = 'I'

# Define the destination cities
destinations = ['A', 'X']

# Define the visited cities
visited = []

# Define the path
path = []

# Define the DFS function
def dfs(city, visited, path):
    # Add the city to the visited list and the path
    visited.append(city)
    path.append(city)

    # If the path contains the destination cities twice, print the path
    if path.count(destinations[0]) == 2 and path.count(destinations[1]) == 2:
        print(path)

    # For each city connected to the current city
    for i in range(len(matrix[cities.index(city)])):
        # If the city has not been visited and is connected to the current city
        if cities[i] not in visited and matrix[cities.index(city)][i] == 1:
            # Call the DFS function on the city
            dfs(cities[i], visited, path)

    # Remove the city from the visited list and the path
    visited.remove(city)
    path.remove(city)

# Call the DFS function on the start city
dfs(start, visited, path)
