
from collections import deque

jugs = [54, 89, 26, 70, 71, 128]
buckets = [240, 242, 246, 329]
actions = []

def bfs():
    queue = deque([([0]*4, [])])
    visited = set()

    while queue:
        state, action = queue.popleft()
        if tuple(state) in visited:
            continue
        visited.add(tuple(state))
        if state == buckets:
            return action
        for i, jug in enumerate(jugs):
            for j in range(4):
                if state[j] + jug <= buckets[j] and (j == 0 or state[j] + jug <= state[j-1]):
                    new_state = state.copy()
                    new_state[j] += jug
                    queue.append((new_state, action + [('+', jug, j+1)]))
                if state[j] - jug >= 0:
                    new_state = state.copy()
                    new_state[j] -= jug
                    queue.append((new_state, action + [('-', jug, j+1)]))

actions = bfs()
print(actions)
