
import sys

# The adjacency matrix
adj_matrix = [
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
]

# The list of cities
cities = ['D', 'E', 'Z', 'R', 'N', 'I', 'K', 'G', 'L', 'B']

# The start city
start = 'L'

# The destinations
destinations = ['D', 'N']

# The minimum travel time
min_time = sys.maxsize

# The minimum path
min_path = None

# The DFS function
def dfs(city, time, path, visited):
    global min_time, min_path
    # If we have visited all destinations twice
    if path.count(destinations[0]) == 2 and path.count(destinations[1]) == 2:
        # If the total travel time is less than the current minimum
        if time < min_time:
            min_time = time
            min_path = path[:]
        return
    # For each city
    for i in range(len(cities)):
        # If there is a direct road from the current city to the next city
        if adj_matrix[cities.index(city)][i] == 1:
            # If we have not visited the next city or we have visited it once
            if cities[i] not in visited or (cities[i] in visited and path.count(cities[i]) == 1):
                # Visit the next city
                path.append(cities[i])
                # Update the visited cities
                visited.add(cities[i])
                # Continue the search
                dfs(cities[i], time + 1, path, visited)
                # Backtrack
                path.pop()
                visited.remove(cities[i])

# Start the search
dfs(start, 0, [start], set())

# Print the result
print(min_path)
