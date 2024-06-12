
# Define the adjacency matrix
adj_matrix = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0]
]

# Define the city names
cities = ['O', 'Z', 'J', 'K', 'E', 'M', 'T', 'W', 'N', 'Q', 'U', 'Y']

# Define the start city
start_city = 'O'

# Define the destination cities
dest_cities = ['N', 'T']

# Define a function to find the quickest route
def find_route(start, dests, matrix, path=[]):
    path = path + [start]
    if start in dests:
        dests.remove(start)
    if not dests:
        return path
    for city in range(len(matrix[cities.index(start)])):
        if matrix[cities.index(start)][city] and cities[city] not in path:
            newpath = find_route(cities[city], dests[:], matrix, path)
            if newpath:
                return newpath
    return None

# Find the quickest route
route = find_route(start_city, dest_cities*2, adj_matrix)

# Print the route
print(route)
