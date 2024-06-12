
from collections import deque

def bfs(start, target, jugs, buckets):
    queue = deque([(start, [])])
    seen = set([start])
    while queue:
        state, actions = queue.popleft()
        if state == target:
            return actions
        for i, jug in enumerate(jugs):
            for j, bucket in enumerate(buckets):
                if state[j] + jug <= bucket:
                    new_state = list(state)
                    new_state[j] += jug
                    new_state = tuple(new_state)
                    if new_state not in seen:
                        queue.append((new_state, actions + [('+', jug, j+1)]))
                        seen.add(new_state)
                if state[j] - jug >= 0:
                    new_state = list(state)
                    new_state[j] -= jug
                    new_state = tuple(new_state)
                    if new_state not in seen:
                        queue.append((new_state, actions + [('-', jug, j+1)]))
                        seen.add(new_state)
    return None

jugs = [59, 20, 21, 62, 61, 60]
buckets = [149, 156, 173, 186]
start = (0, 0, 0, 0)
target = tuple(buckets)

actions = bfs(start, target, jugs, buckets)
print(actions)
