
# Define the adjacency matrix
adjacency_matrix = [
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0]
]

# Define the city names
city_names = ['G', 'P', 'H', 'I', 'J', 'X', 'D', 'V', 'Q', 'L', 'Y']

# Find the nearest city that needs to be visited twice
nearest_city = city_names[adjacency_matrix[city_names.index('D')].index(1)]

# Construct the route
route = ['D', nearest_city, nearest_city, 'Q', 'Q', 'V']

# Print the route
print(route)
