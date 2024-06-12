
def dfs(city, path, visited, count_F, count_U, adj_matrix, target_F, target_U):
    path.append(city)
    visited.add(city)

    if city == target_F:
        count_F += 1
    elif city == target_U:
        count_U += 1

    if count_F == 2 and count_U == 2:
        return path

    for i, connected in enumerate(adj_matrix[city]):
        if connected == 1 and i not in visited:
            new_path = dfs(i, path.copy(), visited.copy(), count_F, count_U, adj_matrix, target_F, target_U)
            if new_path:
                return new_path

    return None

adj_matrix = [
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0]
]

start_city = 'I'
target_F = 'F'
target_U = 'U'

path = dfs(10, [], set(), 0, 0, adj_matrix, target_F, target_U)  # Start from city 'I' (index 10)
city_names = ['H', 'T', 'R', 'F', 'L', 'U', 'Q', 'G', 'N', 'E', 'Y', 'I', 'X']

if path:
    print([city_names[city] for city in path])
else:
    print("No valid path found")
