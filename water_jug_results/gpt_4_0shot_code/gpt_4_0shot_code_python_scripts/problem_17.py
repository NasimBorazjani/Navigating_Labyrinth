
from collections import deque

# Define the capacities of the jugs and the target amounts of water in the buckets
jugs = [143, 117, 116, 103, 84, 87]
targets = [398, 440, 440]

# Define the initial state of the system
initial_state = (0, 0, 0)

# Define a function that generates all possible actions from a given state
def generate_actions(state):
    actions = []
    for i, amount in enumerate(state):
        for j, capacity in enumerate(jugs):
            if amount < capacity:
                actions.append(('+', j, i))
            if amount > 0:
                actions.append(('-', j, i))
    return actions

# Define a function that applies an action to a state and returns the new state
def apply_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]] = min(new_state[action[2]] + jugs[action[1]], targets[action[2]])
    else:
        new_state[action[2]] = max(new_state[action[2]] - jugs[action[1]], 0)
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
