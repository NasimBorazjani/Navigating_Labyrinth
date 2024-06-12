
from collections import deque

# Define the capacities of the jugs and the target amounts in the buckets
jugs = [145, 101, 17, 75, 102, 129]
buckets = [260, 287, 413]

# Define the initial state (empty buckets) and the final state
initial_state = (0, 0, 0)
final_state = tuple(buckets)

# Define the possible actions
actions = [(+1, i, j) for i in range(len(jugs)) for j in range(len(buckets))] + \
          [(-1, i, j) for i in range(len(jugs)) for j in range(len(buckets))]

# Use a dictionary to keep track of how we reached each state
prev = {initial_state: None}

# Use a queue to perform a breadth-first search
queue = deque([initial_state])
while queue:
    state = queue.popleft()
    if state == final_state:
        break
    for action in actions:
        new_state = list(state)
        new_state[action[2]] += action[0] * jugs[action[1]]
        if new_state[action[2]] < 0 or new_state[action[2]] > buckets[action[2]]:
            continue
        if action[2] > 0 and new_state[action[2]] < new_state[action[2] - 1]:
            continue
        if action[2] < len(buckets) - 1 and new_state[action[2]] > new_state[action[2] + 1]:
            continue
        new_state = tuple(new_state)
        if new_state not in prev:
            prev[new_state] = (state, action)
            queue.append(new_state)

# Reconstruct the sequence of actions
actions = []
while state != initial_state:
    state, action = prev[state]
    actions.append(action)
actions.reverse()

# Print the sequence of actions
for action in actions:
    print(('+' if action[0] == +1 else '-', jugs[action[1]], action[2] + 1))
