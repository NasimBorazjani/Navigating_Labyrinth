
from collections import deque

def bfs(graph, start, end, districts):
    queue = deque([(start, [start], 0, {districts[start]} )])
    visited = {start: 0}
    while queue:
        (node, path, time, visited_districts) = queue.popleft()
        for neighbor, travel_time in graph[node]:
            new_time = time + travel_time
            new_districts = visited_districts | {districts[neighbor]}
            if neighbor not in visited or new_time < visited[neighbor]:
                visited[neighbor] = new_time
                new_path = path + [neighbor]
                if neighbor == end and len(new_districts) == 3:
                    return new_path
                queue.append((neighbor, new_path, new_time, new_districts))
    return None

# Convert the matrix map into a graph and a district map
graph = {}
districts = {}
for i in range(13):
    for j in range(13):
        if matrix[i][j] != 'x':
            graph[(i, j)] = []
            if i < 4:
                districts[(i, j)] = 1
            elif i < 6:
                districts[(i, j)] = 2
            else:
                districts[(i, j)] = 3
            if i > 0 and matrix[i-1][j] != 'x':
                graph[(i, j)].append(((i-1, j), matrix[i-1][j]))
            if i < 12 and matrix[i+1][j] != 'x':
                graph[(i, j)].append(((i+1, j), matrix[i+1][j]))
            if j > 0 and matrix[i][j-1] != 'x':
                graph[(i, j)].append(((i, j-1), matrix[i][j-1]))
            if j < 12 and matrix[i][j+1] != 'x':
                graph[(i, j)].append(((i, j+1), matrix[i][j+1]))

# Find the shortest path
path = bfs(graph, (3, 0), (6, 12), districts)
print(path)
