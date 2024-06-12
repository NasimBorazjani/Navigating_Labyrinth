
def dfs(city, visited, path, graph, target_cities, target_count, current_count):
    visited[city] = True
    path.append(city)

    if city in target_cities:
        if current_count[target_cities.index(city)] < target_count[target_cities.index(city)]:
            current_count[target_cities.index(city)] += 1
        else:
            visited[city] = False
            path.pop()
            return

    if all(count == target for count, target in zip(current_count, target_count)):
        print(path)
        return

    for next_city, connected in enumerate(graph[city]):
        if connected == 1 and not visited[next_city]:
            dfs(next_city, visited, path, graph, target_cities, target_count, current_count)

    visited[city] = False
    path.pop()

# Adjacency matrix representing the connections between cities
graph = [
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
]

# Starting city
start_city = 'B'

# Target cities and the number of times to visit each
target_cities = ['E', 'N']
target_count = [2, 2]

# Initialize visited cities and current count of visits
visited = {chr(ord('A') + i): False for i in range(len(graph))}
current_count = [0] * len(target_cities)

# Find the quickest route
dfs(ord(start_city) - ord('A'), visited, [], graph, [ord(city) - ord('A') for city in target_cities], target_count, current_count)
