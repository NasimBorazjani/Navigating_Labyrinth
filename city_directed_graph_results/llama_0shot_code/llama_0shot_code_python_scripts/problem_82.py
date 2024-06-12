
import sys

# The adjacency matrix
adj_matrix = [
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
]

# The list of cities
cities = ['C', 'K', 'U', 'F', 'Q', 'B', 'N', 'W', 'H', 'J', 'T', 'X', 'R', 'L']

# The start city
start = 'J'

# The function to perform the depth-first search
def dfs(city, path, counts, time):
    # If we have visited all cities twice
    if all(count == 2 for count in counts):
        # If this path is quicker than the current best path
        if time < best_time:
            # Update the best path and its time
            global best_path, best_time
            best_path = path.copy()
            best_time = time
        return

    # For each city we can visit
    for i, adj in enumerate(adj_matrix[cities.index(city)]):
        if adj == 1 and counts[i] < 2:
            # Visit the city
            path.append(cities[i])
            counts[i] += 1
            time += 1

            # Continue the search
            dfs(cities[i], path, counts, time)

            # Backtrack
            path.pop()
            counts[i] -= 1
            time -= 1

# Initialize the best path and its time
best_path = None
best_time = sys.maxsize

# Perform the depth-first search
dfs(start, [start], [0] * len(cities), 0)

# Print the best path
print(best_path)
