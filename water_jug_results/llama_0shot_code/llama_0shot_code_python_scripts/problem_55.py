
from collections import deque

def bfs(initial_state, final_states, actions):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, actions = queue.popleft()
        if state in final_states:
            return actions
        for next_state, action in actions_from_state(state, actions, final_states):
            if next_state not in visited:
                queue.append((next_state, actions + [action]))
                visited.add(next_state)

def actions_from_state(state, actions, final_states):
    bucket_capacities = [170, 225, 238, 317]
    jug_capacities = [33, 87, 48, 30, 61, 60]
    buckets, jugs = state
    for i, (b, j) in enumerate(zip(buckets, jugs)):
        if b < bucket_capacities[i]:
            for x in jug_capacities:
                if x > j:
                    yield (list(buckets), list(jugs)), ('+', x, i)
                if j > 0:
                    yield (list(buckets), list(jugs)), ('-', x, i)

initial_state = ([0]*4, [0]*6)
final_states = [([170, 225, 238, 317], [33, 87, 48, 30, 61, 60])]

actions = bfs(initial_state, final_states, actions_from_state)
print(actions)
