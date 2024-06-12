
from collections import deque

# Capacities of the water jugs
capacities = [76, 63, 111, 59, 11, 108, 16, 66, 75, 67]

# Target volumes of the unlabeled buckets
targets = [191, 269, 328]

# Initial state: all buckets are empty
initial_state = [0, 0, 0]

# Function to apply an action to a state
def apply_action(state, action):
    symbol, capacity, bucket = action
    if symbol == '+':
        return state[:bucket] + [min(state[bucket] + capacity, targets[bucket])] + state[bucket+1:]
    else:  # symbol == '-'
        return state[:bucket] + [max(state[bucket] - capacity, 0)] + state[bucket+1:]

# Function to generate all possible next states from a given state
def next_states(state):
    for capacity in capacities:
        for bucket in range(len(state)):
            if state[bucket] < targets[bucket]:
                yield ('+', capacity, bucket)
            if state[bucket] > 0:
                yield ('-', capacity, bucket)

# Use BFS to find the shortest sequence of actions from the initial state to the final state
queue = deque([(initial_state, [])])
visited = set()
while queue:
    state, actions = queue.popleft()
    if state not in visited and state[2] >= targets[2]:
        visited.add(state)
        if state[0] == targets[0] and state[1] == targets[1] and state[2] == targets[2]:
            return actions
        for action in next_states(state):
            next_state = apply_action(state, action)
            queue.append((next_state, actions + [action]))

# If no solution is found, return an empty list
return []

# Print the solution as a list of action tuples
print(solution)
