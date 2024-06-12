
from collections import deque

def bfs(initial_state, final_states, actions):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, actions = queue.popleft()
        if state in final_states:
            return actions
        for next_state, action in actions_to_next_states(state, actions, final_states):
            if next_state not in visited:
                queue.append((next_state, actions + [action]))
                visited.add(next_state)

def actions_to_next_states(state, actions, final_states):
    buckets, jugs = state
    for i in range(len(buckets)):
        for j in range(len(jugs)):
            new_buckets = list(buckets)
            new_jugs = list(jugs)
            if actions[-1][0] == '+' and actions[-1][2] == i:
                continue
            if new_buckets[i] < jugs[j]:
                new_buckets[i] += jugs[j]
                new_jugs[j] = 0
                new_state = (tuple(new_buckets), tuple(new_jugs))
                if new_state not in final_states:
                    yield (new_state, ('+', j, i))
            if new_jugs[j] < buckets[i]:
                new_jugs[j] += buckets[i]
                new_buckets[i] = 0
                new_state = (tuple(new_buckets), tuple(new_jugs))
                if new_state not in final_states:
                    yield (new_state, ('-', j, i))

initial_state = ((0, 0, 0, 0), (122, 121, 124, 28, 89, 73))
final_states = [((270, 311, 372, 389), (122, 121, 124, 28, 89, 73))]
actions = bfs(initial_state, final_states, actions_to_next_states)
print(actions)
