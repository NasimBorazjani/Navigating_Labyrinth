
import sys

# The adjacency matrix representing the connections between the cities
adj_matrix = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
]

# The list of city names
city_names = list('MYQTEAJSWVFNZCI')

# The list to store the visited cities
visited = [0] * len(city_names)

# The list to store the path
path = []

def dfs(city, depth):
    # If the city has been visited twice, then we backtrack
    if visited[city] == 2:
        return

    # Mark the city as visited
    visited[city] += 1

    # Add the city to the path
    path.append(city_names[city])

    # If we have visited all cities twice, then we have found a solution
    if visited.count(2) == len(city_names):
        print(path)
        sys.exit(0)

    # Visit each city that can be reached directly from the current city
    for next_city in range(len(adj_matrix)):
        if adj_matrix[city][next_city] == 1 and visited[next_city] < 2:
            dfs(next_city, depth + 1)

    # Backtrack
    path.pop()
    visited[city] -= 1

# Start the search from city 'S'
start_city = city_names.index('S')
dfs(start_city, 0)
