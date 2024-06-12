
from collections import deque

# capacities of the water jugs
jug_capacities = [32, 73, 55, 68, 61, 107, 44, 45, 74, 113]

# target volumes for the buckets
bucket_volumes = [203, 429, 433, 477]

# possible actions: ('+', X, Y) or ('-', X, Y)
actions = [('+', x, y) for x in jug_capacities for y in range(4)] + \
          [('-', x, y) for x in range(4)]

# initial state: all buckets are empty
initial_state = (0, 0, 0, 0)

# use BFS to find the shortest sequence of actions
queue = deque([(initial_state, None)])
visited = set()
parent = {}
while queue:
    state, action = queue.popleft()
    if state not in visited:
        visited.add(state)
        if state == (bucket_volumes[0], bucket_volumes[1], bucket_volumes[2], bucket_volumes[3]):
            break
        for next_action in actions:
            next_state = apply_action(state, next_action)
            if next_state not in visited:
                queue.append((next_state, next_action))
                parent[next_state] = state

# backtrack to find the sequence of actions
sequence = []
while action is not None:
    sequence.append(action)
    state = parent[state]
    action = parent.get(state)

# reverse the sequence to get the correct order
sequence.reverse()

# print the sequence of actions
print(sequence)
