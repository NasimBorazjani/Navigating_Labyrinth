
from collections import deque

# Define the capacities of the jugs and the target amounts of water in the buckets
jugs = [102, 130, 82, 131, 133, 116]
targets = [265, 368, 378]

# Define the initial state
initial_state = (0, 0, 0)

# Define a function that generates all possible actions
def generate_actions(state):
    actions = []
    for i, jug in enumerate(jugs):
        for j in range(3):
            if state[j] < jug:
                actions.append(('+', i+1, j+1))
            if state[j] > 0:
                actions.append(('-', i+1, j+1))
    return actions

# Define a function that applies an action to a state
def apply_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]-1] += jugs[action[1]-1]
    else:
        new_state[action[2]-1] -= jugs[action[1]-1]
    return tuple(new_state)

# Perform a breadth-first search
queue = deque([(initial_state, [])])
visited = set([initial_state])
while queue:
    state, actions = queue.popleft()
    if state == tuple(targets):
        print(actions)
        break
    for action in generate_actions(state):
        new_state = apply_action(state, action)
        if new_state not in visited and all(new_state[i] <= new_state[i+1] for i in range(2)):
            queue.append((new_state, actions + [action]))
            visited.add(new_state)
