
from collections import defaultdict

# Define the adjacency matrix
adjacency_matrix = {
    'S': ['E'],
    'A': ['U', 'B', 'L', 'F'],
    'J': ['B', 'L'],
    'U': ['S', 'N', 'P'],
    'E': ['A'],
    'B': ['E', 'N', 'P', 'X'],
    'N': ['A', 'U', 'E', 'B', 'X', 'F'],
    'P': ['S', 'N', 'L'],
    'L': ['J', 'B', 'X', 'F'],
    'X': ['J', 'U', 'L'],
    'F': ['A', 'U', 'L']
}

# Define the start city
start_city = 'J'

# Define the destination cities
destination_cities = ['U', 'E']

# Define the visited cities
visited_cities = defaultdict(int)

# Define the path
path = []

# Define the DFS function
def dfs(city):
    # Add the city to the path
    path.append(city)

    # Mark the city as visited
    visited_cities[city] += 1

    # If the city is a destination city and it has been visited twice, return
    if city in destination_cities and visited_cities[city] == 2:
        return

    # Visit each of the city's neighbors
    for neighbor in adjacency_matrix[city]:
        # If the neighbor is a destination city and it has been visited less than twice, or if the neighbor is not a destination city and it has not been visited, visit the neighbor
        if (neighbor in destination_cities and visited_cities[neighbor] < 2) or (neighbor not in destination_cities and visited_cities[neighbor] == 0):
            dfs(neighbor)

    # If all the destination cities have been visited twice, return
    if all(visited_cities[city] == 2 for city in destination_cities):
        return

    # Remove the city from the path
    path.pop()

    # Mark the city as not visited
    visited_cities[city] -= 1

# Call the DFS function
dfs(start_city)

# Print the path
print(path)
