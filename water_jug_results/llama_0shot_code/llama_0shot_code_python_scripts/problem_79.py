
from collections import deque

def bfs(jugs, buckets):
    initial_state = ([0] * len(buckets), 0, 0)
    final_state = (buckets, 0, 0)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        (state, actions) = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if state == final_state:
            return actions
        next_states = generate_next_states(state, jugs)
        for next_state in next_states:
            queue.append((next_state, actions + [next_state[1]]))

def generate_next_states(state, jugs):
    next_states = []
    (buckets, jug, amount) = state
    for i in range(len(jugs)):
        if amount == 0:
            next_states.append((buckets, i, jugs[i]))
        elif amount <= jugs[i]:
            next_states.append((buckets_after_fill(buckets, amount), i, 0))
        if amount >= jugs[i]:
            next_states.append((buckets_after_empty(buckets, amount - jugs[i]), i, amount - jugs[i]))
    return next_states

def buckets_after_fill(buckets, amount):
    new_buckets = list(buckets)
    for i in range(len(buckets)):
        if buckets[i] + amount <= buckets[i + 1]:
            new_buckets[i] += amount
            break
        else:
            amount -= buckets[i + 1] - buckets[i]
            new_buckets[i] = buckets[i + 1]
    return tuple(new_buckets)

def buckets_after_empty(buckets, amount):
    new_buckets = list(buckets)
    for i in range(len(buckets) - 1, -1, -1):
        if buckets[i] - amount >= (buckets[i - 1] if i > 0 else 0):
            new_buckets[i] -= amount
            break
        else:
            amount += buckets[i] - (buckets[i - 1] if i > 0 else 0)
            new_buckets[i] = (buckets[i - 1] if i > 0 else 0)
    return tuple(new_buckets)

jugs = [99, 47, 122, 123, 72, 136, 51, 71]
buckets = [274, 292, 361, 438]

actions = bfs(jugs, buckets)
print(actions)
