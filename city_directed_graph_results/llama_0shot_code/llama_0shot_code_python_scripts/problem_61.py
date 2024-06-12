
from collections import deque

# Adjacency matrix
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1]
]

# Convert matrix to dictionary
graph = {chr(i+65): [] for i in range(13)}
for i in range(13):
    for j in range(13):
        if matrix[i][j]:
            graph[chr(i+65)].append(chr(j+65))

# BFS
start = 'J'
destinations = {'M': 2, 'Z': 2}
path = deque([start])
visited = set([start])
queue = deque([(start, [])])

while queue:
    city, history = queue.popleft()
    for next_city in graph[city]:
        if next_city not in visited:
            visited.add(next_city)
            queue.append((next_city, history + [next_city]))
            path = deque(history + [next_city])
            if next_city in destinations and destinations[next_city] - 1 == 0:
                destinations[next_city] -= 1
            elif next_city not in destinations:
                destinations[next_city] = 0
        elif next_city in destinations and destinations[next_city] > 0:
            destinations[next_city] -= 1
            if all(value == 0 for value in destinations.values()):
                break

print(list(path))
