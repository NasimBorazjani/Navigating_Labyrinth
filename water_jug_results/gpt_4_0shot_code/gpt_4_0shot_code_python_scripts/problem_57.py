
from collections import deque

def bfs(jugs, target):
    queue = deque([([], [0, 0, 0, 0])])
    visited = set()

    while queue:
        path, current = queue.popleft()
        if current == target:
            return path
        for i, jug in enumerate(jugs):
            for j in range(4):
                if current[j] + jug <= target[j] and all(current[j] + jug <= current[k] for k in range(j + 1, 4)):
                    new_state = current[:]
                    new_state[j] += jug
                    if tuple(new_state) not in visited:
                        queue.append((path + [('+', jug, j + 1)], new_state))
                        visited.add(tuple(new_state))
                if current[j] - jug >= 0 and all(current[j] - jug >= current[k] for k in range(j + 1, 4)):
                    new_state = current[:]
                    new_state[j] -= jug
                    if tuple(new_state) not in visited:
                        queue.append((path + [('-', jug, j + 1)], new_state))
                        visited.add(tuple(new_state))
    return None

jugs = [15, 20, 141, 104, 67, 14]
target = [230, 267, 278, 318]
print(bfs(jugs, target))
