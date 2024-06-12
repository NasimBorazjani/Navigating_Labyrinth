
from collections import deque

def bfs(start, end, capacities):
    visited = set()
    queue = deque([([], start)])

    while queue:
        path, current = queue.popleft()
        if current == end:
            return path
        if current in visited:
            continue
        visited.add(current)

        for i, x in enumerate(capacities):
            if x <= current[0]:
                new_state = list(current)
                new_state[0] -= x
                new_state.sort()
                queue.append((path + [('-', x, 1)], tuple(new_state)))
            for j in range(1, 4):
                if x + current[j] <= current[j - 1]:
                    new_state = list(current)
                    new_state[j] += x
                    new_state.sort()
                    queue.append((path + [('+', x, j + 1)], tuple(new_state)))

    return None

capacities = [44, 128, 127, 85, 40, 125]
start = (0, 0, 0, 0)
end = (283, 295, 428, 428)

print(bfs(start, end, capacities))
