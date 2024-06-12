
from collections import deque

matrix = """0 0 1 0 0 1 0 1 0 1 0 0 0 
1 0 0 0 1 0 1 1 0 0 0 1 1 
0 1 0 0 0 0 0 1 0 1 0 0 0 
0 0 0 0 0 0 0 1 0 0 0 0 0 
0 0 1 1 0 0 0 0 1 1 0 1 0 
0 0 0 1 0 0 0 1 1 0 0 0 0 
0 0 0 0 0 1 0 0 0 1 0 0 0 
1 0 0 0 1 0 0 0 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 1 0 0 0 
0 0 0 0 0 1 0 0 0 0 1 0 0 
0 1 0 0 1 1 0 1 1 0 0 0 0 
0 0 0 0 0 1 1 0 0 0 0 0 1 
0 0 0 0 1 0 0 1 0 0 0 0 0"""

graph = {}
cities = 'Z N R F O U P L J I S Q G'.split()
for i, line in enumerate(matrix.split()):
    for j, dist in enumerate(map(int, line.split())):
        if dist:
            if i not in graph:
                graph[i] = []
            graph[i].append(j)

destinations = {'N': 0, 'J': 0}

queue = deque([('F', [])])
visited = set()

while queue:
    city, path = queue.popleft()
    if city not in visited:
        visited.add(city)
        path = path + [city]
        if city in destinations:
            destinations[city] += 1
        if destinations['N'] == 2 and destinations['J'] == 2:
            path = path + [city]
            return path
        for next_city in graph[city]:
            if next_city not in visited or (next_city in destinations and destinations[next_city] < 2):
                queue.append((next_city, path))

print("No solution")
