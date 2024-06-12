
import numpy as np

# The adjacency matrix
adj_matrix = np.array([[0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                       [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                       [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                       [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]])

# The list of cities
cities = ['I', 'A', 'Y', 'K', 'F', 'H', 'W', 'D', 'L', 'U', 'N', 'R', 'Z', 'V', 'X']

# The starting city
start = 'R'

# The cities we need to visit twice
destinations = ['N', 'X']

# The path of the travel
path = [start]

# The visited cities
visited = {start: 0}

# The function to perform the depth-first search
def dfs(city):
    for next_city in cities[cities != city]:
        if next_city not in visited and adj_matrix[cities.index(city), cities.index(next_city)]:
            visited[next_city] = visited.get(city, 0) + 1
            path.append(next_city)
            dfs(next_city)

# Start the depth-first search
dfs(start)

# Print the path
print(path)
