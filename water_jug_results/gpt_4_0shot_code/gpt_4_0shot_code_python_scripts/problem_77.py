
from collections import deque

jugs = [60, 59, 72, 93, 39, 74, 71, 84]
buckets = [166, 239, 286, 421]
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
                new_state = list(state)
                new_state[j] += jug
                if j > 0 and new_state[j] > new_state[j-1]:
                    continue
                if j < 3 and new_state[j] > new_state[j+1]:
                    new_state[j+1] = new_state[j]

                new_state = tuple(new_state)
                if new_state not in visited and all(x <= y for x, y in zip(buckets, new_state)):
                    visited.add(new_state)
                    queue.append(new_state)
                    actions.append(('+', i+1, j+1))

        for i, jug in enumerate(jugs):
            for j in range(4):
                if state[j] >= jug:
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
