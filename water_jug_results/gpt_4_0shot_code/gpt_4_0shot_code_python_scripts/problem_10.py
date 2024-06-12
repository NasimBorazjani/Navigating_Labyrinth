
from collections import deque

# Define the capacities of the jugs and the target amounts of water in the buckets
jugs = [14, 119, 62, 18, 133, 13]
targets = [218, 272, 314]

# Define the initial state of the system
initial_state = (0, 0, 0)

# Define a function that generates all possible actions from a given state
def generate_actions(state):
    actions = []
    for i, amount in enumerate(state):
        for j, capacity in enumerate(jugs):
            if amount < capacity:
                actions.append(('+', j+1, i+1))
            if amount > 0:
                actions.append(('-', j+1, i+1))
    return actions

# Define a function that applies an action to a state and returns the new state
def apply_action(state, action):
    new_state = list(state)
    if action[0] == '+':
        new_state[action[2]-1] = min(new_state[action[2]-1] + jugs[action[1]-1], targets[action[2]-1])
    else:
        new_state[action[2]-1] = max(new_state[action[2]-1] - jugs[action[1]-1], 0)
    return tuple(new_state)

# Perform a breadth-first search to find the shortest sequence of actions that leads to the target state
queue = deque([(initial_state, [])])
visited = set([initial_state])
while queue:
    state, actions = queue.popleft()
    if state == tuple(targets):
        print(actions)
        break
    for action in generate_actions(state):
        new_state = apply_action(state, action)
        if new_state not in visited and all(new_state[i] <= new_state[i+1] for i in range(len(new_state)-1)):
            queue.append((new_state, actions + [action]))
            visited.add(new_state)
