
# Adjacency matrix
adjacency_matrix = [
    "0000100000",
    "0001010010",
    "0000100100",
    "1000001100",
    "0100000000",
    "0010110101",
    "1001100011",
    "0010001101",
    "0100101100",
    "0010010011",
]

# Convert adjacency matrix into dictionary
graph = {}
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == "1":
            if i not in graph:
                graph[i] = []
            graph[i].append(j)

# DFS function
def dfs(path, visited):
    # Base case: if path length is 8, then we've visited all cities twice
    if len(path) == 8:
        routes.append(path)
        return

    # Iterate over all neighbors
    for node in graph[path[-1]]:
        # If node has not been visited twice, visit it
        if visited.get(node, 0) < 2:
            dfs(path + [node], visited)

# Initialize routes
routes = []

# Perform DFS from city 'J' (index 2)
dfs([2], {2: 1})

# Find shortest route
shortest_route = min(routes, key=lambda route: sum(graph[route[i-1]][route[i]] for i in range(1, len(route))))

# Convert route indices to city names
city_names = ['S', 'A', 'J', 'U', 'E', 'B', 'N', 'P', 'L', 'X', 'F']
shortest_route_city_names = [city_names[i] for i in shortest_route]

print(shortest_route_city_names)
