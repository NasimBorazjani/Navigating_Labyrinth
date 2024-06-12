
from collections import deque

def bfs(jugs, buckets):
    initial_state = (0, 0, 0, 0, 0, 0, 0, 0)
    final_states = [(230, 0, 0, 0), (267, 0, 0, 0), (278, 0, 0, 0), (318, 0, 0, 0)]
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, actions = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if state[3:] == final_states:
            return actions
        for i in range(len(jugs)):
            for j in range(4):
                if state[i] + state[j + 4] <= buckets[j]:
                    queue.append(((state[i] + state[j + 4], state[j + 4], state[4], state[5], state[6], state[7], state[(j + 4) % 4]), actions + [('+', jugs[i], j + 1)]))
                if state[i] >= state[j + 4] and state[j + 4] > 0:
                    queue.append(((state[i] - state[j + 4], state[j + 4], state[4], state[5], state[6], state[7], state[(j + 4) % 4]), actions + [('-', jugs[i], j + 1)]))

print(bfs([15, 20, 141, 104, 67, 14], [4, 67, 141, 230]))
