
# Define the adjacency matrix
adjacency_matrix = {
    'Q': ['Z'],
    'T': ['Q', 'A', 'X'],
    'A': ['M'],
    'X': ['M', 'Z', 'B', 'S'],
    'M': ['Q', 'B', 'E'],
    'Y': ['T', 'A', 'X'],
    'Z': ['M', 'Y', 'B'],
    'B': ['Q', 'T', 'A'],
    'S': ['T', 'Y', 'E'],
    'E': ['A', 'X', 'M', 'S', 'B']
}

# Define the start city and the destination cities
start_city = 'Q'
destination_cities = ['T', 'E']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    visited.add(city)

    # If the path includes each destination city twice, print the path
    if all(path.count(destination) == 2 for destination in destination_cities):
        print(path)

    # Otherwise, continue to the next city
    else:
        for next_city in adjacency_matrix[city]:
            if next_city not in visited or next_city in destination_cities:
                find_route(next_city, visited.copy(), path.copy())

# Call the function to find the quickest route
find_route(start_city, set(), [])
