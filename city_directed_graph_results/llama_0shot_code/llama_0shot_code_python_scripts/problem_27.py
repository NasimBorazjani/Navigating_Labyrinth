
import sys

# The adjacency matrix representing the connections between the cities
adj_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
]

# The list of city names
city_names = ['J', 'H', 'K', 'W', 'X', 'I', 'B', 'U', 'D', 'Z', 'G']

# The list of cities that we need to visit exactly twice
visit_twice = ['H', 'Z']

# The list of cities that we have already visited
visited = ['D']

# The list of cities that we are currently visiting
current_path = ['D']

# The list of all possible routes
routes = []

def dfs(current_index):
    global routes
    for i in range(len(adj_matrix)):
        # If there is a direct road from the current city to the next city
        if adj_matrix[current_index][i] == 1:
            # And we have not visited the next city yet
            if city_names[i] not in visited:
                # Mark the next city as visited
                visited.append(city_names[i])
                # Add the next city to the current path
                current_path.append(city_names[i])
                # If the next city is in the visit_twice list
                if city_names[i] in visit_twice:
                    # And we have not visited it twice yet
                    if visited.count(city_names[i]) < 2:
                        # Then continue the search from the next city
                        dfs(i)
                else:
                    # If the next city is not in the visit_twice list
                    # Then continue the search from the next city
                    dfs(i)
                # After we have visited all possible cities from the next city
                # Remove the next city from the current path
                current_path.pop()
                # And remove it from the visited list
                visited.pop()
    # When we have visited all possible cities from the current city
    # Add the current path to the list of all possible routes
    routes.append(current_path[:])

# Start the search from the city 'D'
dfs(city_names.index('D'))

# Find the quickest route
quickest_route = min(routes, key=len)

# Print the quickest route in Python syntax
print(quickest_route)
