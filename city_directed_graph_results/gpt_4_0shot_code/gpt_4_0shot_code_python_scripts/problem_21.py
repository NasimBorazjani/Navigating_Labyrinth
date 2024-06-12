
# Define the adjacency matrix
adj_matrix = {
    'I': ['M', 'H', 'C', 'V'],
    'K': ['M'],
    'D': ['R', 'W'],
    'M': ['I'],
    'Y': ['K', 'D'],
    'H': ['K', 'D', 'M', 'C', 'V', 'Q'],
    'C': ['K', 'M', 'Y', 'H', 'V'],
    'R': ['M', 'V', 'Q'],
    'V': ['Y', 'R'],
    'W': ['I', 'M', 'Y'],
    'Q': ['K', 'D', 'Y', 'C', 'R', 'W']
}

# Define the start city
start_city = 'Y'

# Define the destination cities
dest_cities = ['I', 'Q']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    visited.add(city)

    # If the path includes each destination city twice, print the path
    if all(path.count(city) == 2 for city in dest_cities):
        print(path)

    # Otherwise, continue to the next city
    else:
        for next_city in adj_matrix[city]:
            if next_city not in visited or (next_city in dest_cities and path.count(next_city) < 2):
                find_route(next_city, visited.copy(), path.copy())

# Find the quickest route
find_route(start_city, set(), [])
