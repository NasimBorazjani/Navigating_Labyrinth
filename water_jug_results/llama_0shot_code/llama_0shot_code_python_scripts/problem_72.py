
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
    buckets, jugs = state
    for i, (b, j) in enumerate(zip(buckets, jugs)):
        if b < final_states[i]:
            if j > 0:
                new_buckets = list(buckets)
                new_buckets[i] += min(j, final_states[i] - b)
                new_jugs = list(jugs)
                new_jugs[i] -= min(j, final_states[i] - b)
                yield (tuple(new_buckets), tuple(new_jugs)), ('+', i, min(j, final_states[i] - b))
        elif b > final_states[i]:
            yield (tuple(list(buckets[:i]) + [final_states[i]] + list(buckets[i+1:])), jugs), ('-', i, b - final_states[i])

initial_state = ((0, 0, 0, 0), (57, 98, 149, 99, 105))
final_states = ((281, 401, 423, 427), (57, 98, 149, 99, 105))

actions = bfs(initial_state, final_states, actions_from_state)
print(actions)
