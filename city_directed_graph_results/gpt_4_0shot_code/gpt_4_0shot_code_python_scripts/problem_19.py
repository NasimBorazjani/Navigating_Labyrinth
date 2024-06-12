
# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

# Define the cities
cities = ['J', 'X', 'U', 'I', 'R', 'T', 'Y', 'B', 'M', 'D', 'E']

# Define the start city
start_city = 'E'

# Define the destination cities
destination_cities = ['T', 'Y']

# Define the visited cities
visited_cities = []

# Define the path
path = []

# Define the DFS function
def dfs(city):
    # Add the city to the visited cities
    visited_cities.append(city)

    # Add the city to the path
    path.append(city)

    # If the city is a destination city
    if city in destination_cities:
        # Remove the city from the destination cities
        destination_cities.remove(city)

    # If all destination cities have been visited twice
    if not destination_cities:
        # Return the path
        return path

    # For each city
    for i in range(len(cities)):
        # If the city is connected and has not been visited
        if adjacency_matrix[cities.index(city)][i] == 1 and cities[i] not in visited_cities:
            # Call the DFS function on the city
            dfs(cities[i])

    # If the city is a destination city
    if city in destination_cities:
        # Add the city to the visited cities
        visited_cities.append(city)

        # Add the city to the path
        path.append(city)

    # Return the path
    return path

# Call the DFS function on the start city
print(dfs(start_city))
