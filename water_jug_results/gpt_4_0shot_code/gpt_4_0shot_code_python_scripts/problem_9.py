
from collections import deque

# Define the capacities of the jugs and the target amounts of water in the buckets
jugs = [129, 57, 45, 105, 128, 78]
targets = [344, 376, 386]

# Define the initial state of the system
initial_state = (0, 0, 0)

# Define a function that generates all possible actions from a given state
def generate_actions(state):
    actions = []
    for i, jug in enumerate(jugs):
        for j in range(3):
            if state[j] + jug <= targets[j] and (j == 0 or state[j] + jug <= state[j - 1]):
                actions.append(('+', i, j))
            if state[j] >= jug:
                actions.append(('-', i, j))
    return actions

# Define a function that applies an action to a state
def apply_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]] += jugs[action[1]]
    else:
        new_state[action[2]] -= jugs[action[1]]
    return tuple(new_state)

# Perform a breadth-first search to find the shortest sequence of actions
queue = deque([(initial_state, [])])
visited = set([initial_state])
while queue:
    state, actions = queue.popleft()
    if state == tuple(targets):
        print(actions)
        break
    for action in generate_actions(state):
        new_state = apply_action(state, action)
        if new_state not in visited:
            queue.append((new_state, actions + [action]))
            visited.add(new_state)
