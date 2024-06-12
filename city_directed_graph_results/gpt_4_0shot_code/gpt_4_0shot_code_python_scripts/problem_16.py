
# Define the adjacency matrix and the list of cities
matrix = [
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0]
]
cities = ['C', 'V', 'A', 'G', 'Y', 'P', 'Z', 'S', 'J', 'I']

# Define the DFS function
def dfs(city, path, p_count, g_count):
    if p_count == 2 and g_count == 2:
        return path
    if city == 'P':
        p_count += 1
    if city == 'G':
        g_count += 1
    for i in range(len(matrix[cities.index(city)])):
        if matrix[cities.index(city)][i] == 1:
            next_city = cities[i]
            if next_city not in path or (next_city in ['P', 'G'] and path.count(next_city) < 2):
                result = dfs(next_city, path + [next_city], p_count, g_count)
                if result:
                    return result

# Call the DFS function with the start city 'S'
print(dfs('S', ['S'], 0, 0))
