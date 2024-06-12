
# Adjacency matrix
matrix = [
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
]

# Convert matrix into dictionary of lists
graph = {city: [] for city in 'ABCDEFGHIJKLMNO'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            graph[chr(i + 65)].append(chr(j + 65))

# DFS function
def dfs(city, path, visited, m_count, j_count):
    # Mark city as visited
    visited.add(city)
    path.append(city)

    # Visit M and J twice
    if city in ('M', 'J'):
        if city == 'M':
            m_count += 1
        else:
            j_count += 1
        if m_count == 2 and j_count == 2:
            return path
        return dfs('A', path, visited, m_count, j_count)

    # Visit other cities once
    for neighbor in graph[city]:
        if neighbor not in visited:
            result = dfs(neighbor, path, visited, m_count, j_count)
            if result:
                return result

    # Backtrack
    path.pop()
    visited.remove(city)
    if city in ('M', 'J'):
        if city == 'M':
            m_count -= 1
        else:
            j_count -= 1

# Start DFS from city 'A'
path = dfs('A', [], set(), 0, 0)
print(path)
