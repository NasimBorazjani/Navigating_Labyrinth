
# Adjacency matrix
adj_matrix = [
    "01000000000100000000",
    "0000000100001100000",
    "0000000000000100001",
    "1000000101000000011",
    "1100000010000101000",
    "0000000101100110010",
    "0010000000011101000",
    "0000000000000000001",
    "0001000100001101010",
    "0010100000000000011",
    "0000000000000000001",
    "1100000000011100111",
    "1000000001110100000",
    "0000000000000000001",
]

# Convert adjacency matrix into dictionary
adj_dict = {city: [] for city in 'ABCDEFGHIORPSTUWYZ'}
for i, row in enumerate(adj_matrix):
    for j, col in enumerate(row):
        if col == '1':
            adj_dict[chr(i + 67)].append(chr(j + 67))

# Depth-first search
def dfs(city, path, visited):
    path.append(city)
    visited.add(city)

    if len(visited) == len(adj_dict) and path.count('R') == 2 and path.count('G') == 2:
        return path

    for next_city in adj_dict[city]:
        if next_city not in visited:
            result = dfs(next_city, path.copy(), visited.copy())
            if result:
                return result

    path.pop()
    visited.remove(city)

# Start depth-first search from city 'F'
best_path = dfs('F', [], set())
print(best_path)
