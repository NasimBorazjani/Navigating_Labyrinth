
from collections import deque

jugs = [52, 55, 84, 135, 136, 47, 139, 76]
buckets = [292, 325, 496, 516]
actions = []

def bfs():
    queue = deque([(0, 0, 0, 0)])
    visited = set([(0, 0, 0, 0)])

    while queue:
        state = queue.popleft()
        if state == tuple(buckets):
            return True

        for i, jug in enumerate(jugs):
            for j in range(4):
                if state[j] + jug <= buckets[j] and all(state[j] + jug <= state[k] for k in range(j+1, 4)):
                    new_state = list(state)
                    new_state[j] += jug
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
                        actions.append(('+', i+1, j+1))

                if state[j] - jug >= 0 and all(state[j] - jug >= state[k] for k in range(j+1, 4)):
                    new_state = list(state)
                    new_state[j] -= jug
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
                        actions.append(('-', i+1, j+1))

    return False

if bfs():
    print(actions)
else:
    print("No solution found")
