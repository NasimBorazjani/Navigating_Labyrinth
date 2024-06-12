
import sys

# The adjacency matrix
matrix = [
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
]

# The list of cities
cities = ['A', 'P', 'Z', 'O', 'R', 'I', 'L', 'X', 'E', 'T', 'W', 'D', 'S', 'G', 'Q']

# The start city
start = 'E'

# The target cities and the number of times we want to visit each of them
targets = {'A': 2, 'P': 2}

# The best path and its cost
best_path = None
best_cost = sys.maxsize

# The current path and the number of visits to each city
current_path = [start]
current_visits = {city: 0 for city in cities}
current_visits[start] = 1

# The recursive function that explores all possible paths
def dfs(current_cost):
    global best_path, best_cost
    city = current_path[-1]
    if all(current_visits[target] == targets[target] for target in targets):
        # If we have visited all the target cities the required number of times,
        # update the best path and its cost if the current path is quicker
        if current_cost < best_cost:
            best_path = current_path[:]
            best_cost = current_cost
    else:
        # If we have not visited all the target cities yet, extend the current path
        for i, adjacent in enumerate(matrix[cities.index(city)]):
            if adjacent and current_visits[cities[i]] < (targets.get(cities[i], 1)):
                current_path.append(cities[i])
                current_visits[cities[i]] += 1
                dfs(current_cost + 1)
                current_path.pop()
                current_visits[cities[i]] -= 1

# Start the depth-first search
dfs(0)

# Print the best path
print(best_path)
