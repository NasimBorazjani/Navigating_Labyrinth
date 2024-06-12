
def dfs(graph, city, visited, path):
    # Mark the city as visited
    visited[city] += 1

    # Add the city to the path
    path.append(city)

    # If both city 'H' and 'P' have been visited twice, return the path
    if visited['H'] == 2 and visited['P'] == 2:
        return path

    # Visit the neighboring cities
    for neighbor in graph[city]:
        if visited[neighbor] < 2 or (neighbor in ['H', 'P'] and visited[neighbor] < 2):
            result = dfs(graph, neighbor, visited, path)
            if result:
                return result

    # If no path is found, backtrack
    path.pop()
    visited[city] -= 1

    return None

# Create a graph from the adjacency matrix
graph = {
    'S': ['V', 'U', 'E', 'H'],
    'V': ['P'],
    'U': ['V', 'P', 'Q'],
    'W': ['S', 'V', 'Z'],
    'G': ['V', 'U'],
    'E': ['S', 'T'],
    'H': ['V', 'W', 'Z'],
    'P': ['E', 'H', 'T'],
    'T': ['G', 'P', 'Q'],
    'Q': ['H', 'P'],
    'Z': ['V', 'P', 'Q']
}

# Initialize the visited dictionary and the path list
visited = {city: 0 for city in graph}
path = []

# Start DFS from city 'G'
path = dfs(graph, 'G', visited, path)

# Print the path
print(path)
