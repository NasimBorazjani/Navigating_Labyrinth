
from collections import deque

matrix = [
    "0000101001110",
    "1000000000011",
    "0001000000000",
    "0100000000011",
    "0000000011000",
    "0001000000000",
    "0010000000000",
    "1000100001000",
    "0110000100000",
    "0000110000000",
    "0001000000000",
    "1011000000000",
    "0000000001000"
]

graph = {city: [] for city in 'ABCDEFGXMQUORNKE'}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '1':
            graph[chr(i+65)].append(chr(j+65))

start = 'A'
destinations = {'D': 2, 'E': 2}

queue = deque([(start, [start])])
visited = set()

while queue:
    city, path = queue.popleft()
    if city in destinations:
        destinations[city] -= 1
        if destinations[city] == 0:
            print(path)
            break
    if city not in visited:
        visited.add(city)
        for neighbor in graph[city]:
            queue.append((neighbor, path + [neighbor]))
