
from collections import deque

# Capacities of the water jugs
capacities = [19, 122, 104, 145, 38, 141, 126, 82, 37, 33]

# Target volumes of the unlabeled buckets
targets = [256, 399, 410]

# Initial state: all buckets are empty
initial_state = [0, 0, 0]

# Function to apply an action to a state
def apply_action(state, action):
    symbol, capacity, bucket = action
    if symbol == '+':
        return state[:bucket] + [min(state[bucket] + capacity, targets[bucket])] + state[bucket+1:]
    else: # symbol == '-'
        return state[:bucket] + [state[bucket] - min(state[bucket], capacity)] + state[bucket+1:]

# Function to generate all possible next states from a given state
def next_states(state):
    for capacity in capacities:
        for bucket in range(len(state)):
            if state[bucket] > 0:
                yield ('-', capacity, bucket)
            if state[bucket] < targets[bucket] and state[bucket] + capacity <= targets[bucket]:
                yield ('+', capacity, bucket)

# Use BFS to find the shortest sequence of actions from the initial state to the final state
queue = deque([(initial_state, [])])
seen = set()
while queue:
    state, actions = queue.popleft()
    if state not in seen and state[2] >= targets[2]:
        seen.add(state)
        if state == targets:
            return actions
        for action in next_states(state):
            queue.append((apply_action(state, action), actions + [action]))

# If no solution is found, print a message
print("No solution found")
