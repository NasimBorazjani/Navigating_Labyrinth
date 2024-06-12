
# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
]

# Define the cities
cities = ['I', 'A', 'Y', 'K', 'F', 'H', 'W', 'D', 'L', 'U', 'N', 'R', 'Z', 'V', 'X']

# Define the start city
start_city = 'R'

# Define the destination cities
destination_cities = ['N', 'X']

# Define the visited cities
visited_cities = []

# Define the path
path = []

# Define the DFS function
def dfs(city, visited_cities, path):
    # Add the city to the visited cities
    visited_cities.append(city)

    # Add the city to the path
    path.append(city)

    # If the path contains the destination cities twice, print the path
    if path.count(destination_cities[0]) == 2 and path.count(destination_cities[1]) == 2:
        print(path)

    # For each city connected to the current city
    for i in range(len(cities)):
        if adjacency_matrix[cities.index(city)][i] == 1 and (cities[i] not in visited_cities or cities[i] in destination_cities):
            # Call the DFS function
            dfs(cities[i], visited_cities, path)

    # Remove the city from the visited cities
    visited_cities.remove(city)

    # Remove the city from the path
    path.remove(city)

# Call the DFS function
dfs(start_city, visited_cities, path)
