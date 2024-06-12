
# Define the adjacency matrix
matrix = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0]
]

# Define the cities
cities = ['Q', 'A', 'E', 'R', 'D', 'G', 'X', 'K', 'B', 'Z', 'W', 'F', 'O', 'L']

# Define the start city
start = 'D'

# Define the destination cities
destinations = ['K', 'X']

# Define the visited cities
visited = {city: 0 for city in cities}
visited[start] = 1

# Define the path
path = [start]

# Define the DFS function
def dfs(city, visited, path):
    # If we have visited the destination cities twice, return the path
    if visited[destinations[0]] == 2 and visited[destinations[1]] == 2:
        return path

    # Get the index of the current city
    index = cities.index(city)

    # Iterate over the cities
    for i in range(len(cities)):
        # If the city is reachable and we have not visited it or it is a destination city
        if matrix[index][i] == 1 and (visited[cities[i]] == 0 or cities[i] in destinations):
            # Visit the city
            visited[cities[i]] += 1

            # Add the city to the path
            path.append(cities[i])

            # Recursively call the DFS function
            result = dfs(cities[i], visited, path)

            # If we have found a path, return it
            if result:
                return result

            # Backtrack
            visited[cities[i]] -= 1
            path.pop()

# Call the DFS function
result = dfs(start, visited, path)

# Print the result
print(result)
