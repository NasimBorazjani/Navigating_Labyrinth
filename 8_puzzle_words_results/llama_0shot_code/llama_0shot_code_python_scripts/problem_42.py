
from collections import deque

def bfs(start, target):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        current, swaps = queue.popleft()
        if current == target:
            return swaps
        if current not in visited:
            visited.add(current)
            for i in range(len(current)):
                if current[i] == '_':
                    for j in range(1, 5):
                        new_current = current[:i] + current[i+1:i+j] + ['_'] + current[i:i+j-1] + current[i+j:]
                        new_current = ' '.join(new_current)
                        new_swaps = swaps + [j]
                        queue.append((new_current, new_swaps))
    return None

start = ['_', 'j', 'a', 'r', 'e', 'b'], ['z', 'o', 'y', 's', 'i', 'i'], ['r', 'e', 'r', 's', 't', 'y'], ['g', 'e', 'i', 'q', 'u', 'a']
start = ' '.join([''.join(row) for row in start])

target = ['jerib', 'zoysia', 'reesty', 'griqua']
target = ' '.join(target)

swaps = bfs(start, target)
print(swaps)
