
import sys

# The adjacency matrix representing the connections between the cities
adjacency_matrix = [
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
]

# The list of city names
city_names = list('JHXLFAPMDRTZNK')

# The list of cities that we have visited
visited = [False] * len(city_names)

# The list of cities that we have to visit
to_visit = [2] * len(city_names)
to_visit[city_names.index('K')] = 0
to_visit[city_names.index('N')] = 0

# The current path
path = ['X']

# The function to perform the depth-first search
def dfs(current):
    visited[current] = True
    path.append(city_names[current])
    for i in range(len(city_names)):
        if not visited[i] and adjacency_matrix[current][i] == 1 and to_visit[i] > 0:
            to_visit[i] -= 1
            dfs(i)
            if len(path) == len(city_names):
                return
            path.pop()
            to_visit[i] += 1
    visited[current] = False
    path.pop()

# Perform the depth-first search
dfs(city_names.index('X'))

# Print the solution
print(path)
