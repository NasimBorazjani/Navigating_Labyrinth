
from collections import deque

def bfs(jugs, buckets):
    initial_state = (0, 0, 0, 0) + tuple(jugs)
    final_state = buckets
    queue = deque([((), initial_state)])
    visited = set()

    while queue:
        path, state = queue.popleft()
        if state not in visited:
            visited.add(state)
            if state == final_state:
                return path
            for i in range(len(jugs)):
                for j in range(4):
                    if state[j] < buckets[j]:
                        new_state = list(state)
                        new_state[j] += jugs[i]
                        if new_state[j] <= buckets[j]:
                            queue.append((path + (('+', jugs[i], j + 1),), tuple(new_state)))
                    if state[j] > 0:
                        new_state = list(state)
                        removed = min(state[j], jugs[i])
                        new_state[j] -= removed
                        new_state[4 + i] += removed
                        queue.append((path + (('-', jugs[i], j + 1),), tuple(new_state)))
    return None

jugs = [19, 42, 18, 127, 106, 32, 22, 137]
buckets = [245, 252, 264, 314]

print(bfs(jugs, buckets))
