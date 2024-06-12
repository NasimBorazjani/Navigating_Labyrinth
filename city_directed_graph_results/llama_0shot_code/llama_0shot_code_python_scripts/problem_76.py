
import sys

# The adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
]

# The list of cities
cities = ['Q', 'A', 'E', 'R', 'D', 'G', 'X', 'K', 'B', 'Z', 'W', 'F', 'O', 'L']

# The current city
current_city = 'D'

# The list of visited cities
visited = [0] * len(cities)

# The list of cities to visit
to_visit = [2, 2]  # We need to visit 'X' and 'K' twice

# The list of cities in our path
path = [current_city]

# The function to perform the depth-first search
def dfs(city_index):
    global current_city
    global path
    global visited
    global to_visit

    # Mark the current city as visited
    visited[city_index] += 1

    # Check if we have visited the current city twice
    if visited[city_index] == 2 and city_index in [0, 1]:
        to_visit[city_index] -= 1

    # Add the current city to the path
    path.append(cities[city_index])

    # Visit all the cities that can be reached directly from the current city
    for i in range(len(matrix)):
        if matrix[city_index][i] == 1 and visited[i] < 2:
            dfs(i)

    # Backtrack
    path.pop()
    visited[city_index] -= 1

# Perform the depth-first search
for i in range(len(matrix)):
    if matrix[current_city_index][i] == 1 and visited[i] < 2:
        dfs(i)

# Print the path
print(path)
