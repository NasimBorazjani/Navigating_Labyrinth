
from collections import deque

# Capacities of the water jugs
capacities = [45, 141, 50, 114, 104, 19, 78, 18, 23, 133]

# Target volumes of the unlabeled buckets
targets = [253, 337, 385]

# Initial state: all buckets are empty
initial_state = [0, 0, 0]

# Function to apply an action to a state
def apply_action(state, action):
    symbol, capacity, bucket = action
    if symbol == '+':
        return state[:bucket] + [min(state[bucket] + capacity, targets[bucket])] + state[bucket+1:]
    else:  # symbol == '-'
        return state[:bucket] + [state[bucket] - min(state[bucket], capacity)] + state[bucket+1:]

# Function to generate all possible next states from a given state
def next_states(state):
    for capacity in capacities:
        for bucket in range(len(state)):
            if state[bucket] > 0:
                yield ('-', capacity, bucket)  # Empty the bucket
            if state[bucket] < targets[bucket] and capacity <= targets[bucket] - state[bucket]:
                yield ('+', capacity, bucket)  # Fill the bucket

# Use BFS to find the shortest sequence of actions from the initial state to the final state
queue = deque([([], initial_state)])
visited = set()
while queue:
    actions, state = queue.popleft()
    if state not in visited and state[2] >= targets[2]:  # Final state reached
        print(actions)
        break
    visited.add(state)
    for action in next_states(state):
        if (actions + [action], apply_action(state, action)) not in visited:
            queue.append((actions + [action], apply_action(state, action)))
