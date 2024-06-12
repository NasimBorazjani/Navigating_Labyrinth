
from collections import deque

def bfs(jugs, buckets):
    initial_state = ([jug for jug in jugs if jug <= bucket], [jug for jug in jugs if jug > bucket]) for bucket in buckets
    queue = deque([(initial_state, [])])
    while queue:
        state, actions = queue.popleft()
        if all(len(bucket) == i + 1 and (bucket[i] == amount or bucket[i] == 0) for i, (bucket, amount) in enumerate(zip(state, buckets))):
            return actions
        for i, (bucket, full_jugs, empty_jugs) in enumerate(zip(state, full_jugs, empty_jugs)):
            if bucket:
                for j, jug in enumerate(full_jugs):
                    new_state = list(state)
                    new_state[i] = [jug for jug in full_jugs if jug != jug]
                    new_state[(i + 1) % len(state)] = [jug for jug in empty_jugs if jug != jug]
                    queue.append((new_state, actions + [('-', jug, i)]))
            if i < len(state) - 1:
                for j, jug in enumerate(empty_jugs):
                    if jug <= buckets[i]:
                        new_state = list(state)
                        new_state[i] = [jug for jug in full_jugs if jug != jug]
                        new_state[(i + 1) % len(state)] = [jug for jug in empty_jugs if jug != jug]
                        queue.append((new_state, actions + [('+', jug, i)]))
    return None

jugs = [117, 118, 23, 86, 109, 128, 104, 61]
buckets = [367, 390, 400, 470]

actions = bfs(jugs, buckets)
print(actions)
