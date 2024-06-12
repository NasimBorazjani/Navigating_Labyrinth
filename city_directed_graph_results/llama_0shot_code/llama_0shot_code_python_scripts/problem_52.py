
from collections import defaultdict

# The adjacency matrix
matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0]
]

# Convert the adjacency matrix into a dictionary of lists
graph = defaultdict(list)
for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col == 1:
            graph[chr(i + 67)].append(chr(j + 67))

# The best path found so far
best_path = None

# The depth-first search function
def dfs(city, destinations, path):
    global best_path
    # If all destinations have been visited twice
    if all(destinations[city] == 0 for city in destinations):
        # Add the time to return to city 'C'
        time = graph[city][ord('C') - ord('A')]
        # Check if this path is quicker
        if best_path is None or sum(path) + time < sum(best_path):
            best_path = path + [city]
    else:
        # For each city that can be visited
        for next_city in graph[city]:
            # If the city has not been visited twice yet
            if destinations[next_city] > 0:
                # Visit the city
                destinations[next_city] -= 1
                # Call the dfs function recursively
                dfs(next_city, destinations, path + [city])
                # Return to the original state
                destinations[next_city] += 1

# Call the dfs function with 'C' as the starting city
destinations = {'J': 2, 'D': 2}
dfs('C', destinations, [])

# Print the best path found
print(best_path)
