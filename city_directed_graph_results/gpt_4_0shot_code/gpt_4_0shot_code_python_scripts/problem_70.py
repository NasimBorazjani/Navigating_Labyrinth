
# Define the adjacency matrix
adj_matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Define the cities
cities = ['K', 'I', 'E', 'B', 'Y', 'J', 'U', 'D', 'L', 'A', 'X', 'C', 'F', 'V']

# Define the start city
start_city = 'V'

# Define the destination cities
dest_cities = ['E', 'U']

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

    # Check if the destination cities have been visited twice
    if path.count(dest_cities[0]) == 2 and path.count(dest_cities[1]) == 2:
        return path

    # Get the index of the city
    city_index = cities.index(city)

    # Iterate over the cities
    for i in range(len(cities)):
        # Check if the city is connected and has not been visited or is a destination city
        if adj_matrix[city_index][i] == 1 and (cities[i] not in visited_cities or cities[i] in dest_cities):
            # Call the DFS function
            result = dfs(cities[i], visited_cities, path)

            # Check if the result is not None
            if result is not None:
                return result

    # Remove the city from the path
    path.pop()

    # Remove the city from the visited cities
    visited_cities.remove(city)

# Call the DFS function
result = dfs(start_city, visited_cities, path)

# Print the result
print(result)
