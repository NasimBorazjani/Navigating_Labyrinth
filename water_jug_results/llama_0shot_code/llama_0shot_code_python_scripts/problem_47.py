
from collections import deque

# Capacities of the water jugs
capacities = [141, 101, 126, 26, 120, 75, 110, 108, 97, 100]

# Target volumes of the unlabeled buckets
targets = [254, 456, 579]

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
                yield ('-', capacity, bucket)
            if state[bucket] < targets[bucket] and state[bucket] + capacity <= targets[bucket]:
                yield ('+', capacity, bucket)

# Use BFS to find the shortest sequence of actions from the initial state to the final state
queue = deque([(initial_state, [])])
seen = set()
while queue:
    state, actions = queue.popleft()
    if state not in seen and all(t <= s for s, t in zip(state, targets)):
        if all(s == t for s, t in zip(state, targets)):
            return actions
        seen.add(state)
        for action in next_states(state):
            queue.append((apply_action(state, action), actions + [action]))

# If no solution is found, return an empty list
return []

# Print the solution as a list of action tuples
print(actions)
