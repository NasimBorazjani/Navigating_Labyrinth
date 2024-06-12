
import sys

# The adjacency matrix
adj_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0]
]

# The list of cities
cities = ['R', 'S', 'W', 'B', 'P', 'G', 'Q', 'E', 'N', 'D', 'J']

# The visited cities
visited = [False] * len(cities)

# The current path
path = ['G']

# The function to perform the DFS
def dfs(city_idx):
    # Mark the city as visited
    visited[city_idx] = True

    # Add the city to the path
    path.append(cities[city_idx])

    # If the city is 'E' or 'S', we need to visit it twice
    if cities[city_idx] in ['E', 'S']:
        # If we have not visited the city twice yet
        if path.count(cities[city_idx]) < 2:
            # Visit the city again
            dfs(city_idx)

    # Visit the unvisited cities
    for next_city_idx in range(len(cities)):
        if not visited[next_city_idx] and adj_matrix[city_idx][next_city_idx] == 1:
            dfs(next_city_idx)

    # Backtrack
    path.pop()
    visited[city_idx] = False

# Start the DFS from city 'G'
dfs(cities.index('G'))

# Print the path
print(path)
