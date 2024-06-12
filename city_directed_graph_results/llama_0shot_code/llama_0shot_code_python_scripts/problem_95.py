
import sys

# The adjacency matrix
adj_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# The list of cities
cities = ['E', 'K', 'G', 'C', 'U', 'A', 'J', 'O', 'N', 'R', 'W', 'M', 'B', 'H', 'Q']

# The starting city
start = 'C'

# The function to perform the depth-first search
def dfs(city, visited_e, visited_q, path):
    # If we have visited 'E' and 'Q' exactly twice, we have found a solution
    if visited_e == 2 and visited_q == 2:
        return [city] + path

    # Otherwise, we continue the search
    for i in range(len(cities)):
        if adj_matrix[cities.index(city)][i] == 1 and (cities[i] != 'E' or visited_e < 2) and (cities[i] != 'Q' or visited_q < 2):
            new_visited_e = visited_e + (1 if cities[i] == 'E' else 0)
            new_visited_q = visited_q + (1 if cities[i] == 'Q' else 0)
            result = dfs(cities[i], new_visited_e, new_visited_q, [city] + path)
            if result is not None:
                return result

    return None

# Perform the depth-first search
result = dfs(start, 0, 0, [])

# Print the result
print(result)
