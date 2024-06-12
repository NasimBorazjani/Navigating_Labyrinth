
# Define the adjacency matrix
adj_matrix = {
    'H': ['T'],
    'F': ['R', 'L', 'D'],
    'C': ['L'],
    'E': ['C', 'V'],
    'T': ['H', 'M', 'Z', 'D'],
    'V': ['F', 'C', 'I'],
    'R': ['I', 'M', 'D'],
    'I': ['F', 'C', 'E', 'M'],
    'M': ['H', 'C'],
    'Z': ['H', 'R', 'M'],
    'L': ['C', 'T', 'R', 'M'],
    'D': ['H', 'F', 'C', 'V', 'I', 'M', 'Z', 'L']
}

# Define the start city and destination cities
start_city = 'E'
dest_cities = ['D', 'T']

# Define a function to find the quickest route
def find_route(city, visited, path):
    # Add the current city to the path
    path.append(city)
    visited.add(city)

    # If the path includes the destination cities twice, print the path
    if path.count(dest_cities[0]) == 2 and path.count(dest_cities[1]) == 2:
        print(path)
        return

    # Visit each city connected to the current city
    for next_city in adj_matrix[city]:
        if next_city not in visited or next_city in dest_cities:
            find_route(next_city, visited.copy(), path.copy())

# Call the function to find the quickest route
find_route(start_city, set(), [])
