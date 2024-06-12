
# Adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 0]
]

# Convert adjacency matrix into dictionary
graph = {city: [] for city in 'UWAXJKEHTR'}
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == 1:
            graph[chr(i + 65)].append(chr(j + 65))

# DFS function
def dfs(city, visit_count, path):
    if city == 'X' and visit_count[city] == 2 or city == 'W' and visit_count[city] == 2:
        total_time = time_to_E[city] + sum(time_to_E[city] for city in path)
        if total_time < best_solution[0]:
            best_solution[0] = total_time
            best_solution[1] = path + [city]
    elif visit_count[city] < 2:
        for next_city in graph[city]:
            if visit_count[next_city] < 2:
                dfs(next_city, {city: visit_count[city] + 1 if city != next_city else visit_count[city] for city in visit_count}, path + [city])

# Time to reach each city from 'E'
time_to_E = {'E': 0, 'U': 1, 'W': 2, 'A': 3, 'J': 4, 'K': 5, 'H': 6, 'X': 7, 'R': 8, 'T': 9}

# Start DFS from 'E'
best_solution = [float('inf'), []]
dfs('E', {'E': 1}, ['E'])

# Print the best solution
print(best_solution[1])
