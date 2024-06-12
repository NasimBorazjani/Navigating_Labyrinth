
from collections import deque, defaultdict
from heapq import *

def shortest_path(graph, start, end1, end2):
    queue = deque([([start], 0)])
    visited = set([start])
    while queue:
        path, length = queue.popleft()
        city = path[-1]
        if (city == end1 and end2 in path) or (city == end2 and end1 in path):
            if len(path) >= 10:
                heappush(queue, (length, path))
            else:
                heappush(queue, (length+1, path+[city]))
        for next_city in graph[city]:
            if next_city not in visited:
                visited.add(next_city)
                queue.append((path+[next_city], length+1))
    return heappop(queue)[1] if queue else None

graph = {
    'P': ['N', 'Y', 'L', 'Q', 'H', 'C', 'G', 'U', 'K', 'J', 'B', 'R', 'T'],
    'N': ['P', 'Y', 'C', 'R'],
    'Y': ['P', 'N', 'B'],
    'L': ['P', 'N', 'Y', 'C', 'K', 'J'],
    'Q': ['P', 'H', 'T'],
    'H': ['P', 'Q', 'C', 'J'],
    'C': ['P', 'N', 'L', 'K', 'J', 'R', 'B'],
    'G': ['P', 'L', 'K'],
    'U': ['P', 'C', 'J'],
    'K': ['P', 'L', 'G', 'U', 'C', 'H', 'J', 'B', 'R'],
    'J': ['P', 'L', 'H', 'U', 'K', 'C', 'B', 'R', 'T'],
    'B': ['P', 'Y', 'L', 'K', 'J', 'C', 'R', 'T'],
    'R': ['P', 'N', 'C', 'K', 'J', 'B'],
    'T': ['P', 'Q', 'J', 'B', 'R']
}

print(shortest_path(graph, 'P', 'N', 'R'))
