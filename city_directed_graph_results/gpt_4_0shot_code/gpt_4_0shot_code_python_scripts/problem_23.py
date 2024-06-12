
# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]
]

# Define the cities
cities = ['N', 'W', 'X', 'P', 'J', 'E', 'L', 'M', 'I', 'K', 'Q']

# Define the start city
start_city = 'K'

# Define the destination cities
destination_cities = ['P', 'N']

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

    # If the destination cities are in the path twice, print the path
    if path.count(destination_cities[0]) == 2 and path.count(destination_cities[1]) == 2:
        print(path)
        return

    # For each city connected to the current city
    for i in range(len(adjacency_matrix[cities.index(city)])):
        # If the city is connected and has not been visited or is a destination city
        if adjacency_matrix[cities.index(city)][i] == 1 and (cities[i] not in visited_cities or cities[i] in destination_cities):
            # Call the DFS function for the city
            dfs(cities[i])

            # Remove the city from the path
            path.pop()

            # If the city is not a destination city, remove it from the visited cities
            if cities[i] not in destination_cities:
                visited_cities.remove(cities[i])

# Call the DFS function for the start city
dfs(start_city)
