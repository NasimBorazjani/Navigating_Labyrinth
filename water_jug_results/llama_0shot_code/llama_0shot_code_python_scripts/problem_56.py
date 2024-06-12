
from collections import deque

def bfs(initial_state, final_states, actions):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, actions = queue.popleft()
        if state in final_states:
            return actions
        for next_state, action in actions_from_state(state, actions):
            if next_state not in visited:
                queue.append((next_state, actions + [action]))
                visited.add(next_state)

def actions_from_state(state, actions):
    bucket_capacities = [260, 295, 331, 394]
    jug_capacities = [12, 88, 148, 87, 143, 131]
    buckets, jugs = state
    for i, (b, j) in enumerate(zip(buckets, jugs)):
        if b < bucket_capacities[i]:
            yield (list(buckets), list(jugs))  # fill bucket i from jug i
        if b > 0:
            yield (list(buckets), list(jugs))  # empty bucket i to jug i
        for k, (b_k, j_k) in enumerate(zip(buckets, jugs)):
            if i != k and b_k > 0 and b_k <= b_k + j_k:
                yield (list(buckets), list(jugs))  # move water from bucket i to bucket k

initial_state = ([0]*4, [0]*6)
final_states = [([260, 295, 331, 394], [0]*6)]

actions = bfs(initial_state, final_states, actions_from_state)
print(actions)
