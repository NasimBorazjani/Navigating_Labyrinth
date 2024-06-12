
from collections import deque

# capacities of the water jugs
capacities = [20, 142, 147, 48, 29, 113, 17, 18, 112, 68]

# target volumes of the buckets
targets = [287, 423, 583]

# initial state: all buckets are empty
initial_state = [0, 0, 0]

# function to apply an action to a state
def apply_action(state, action):
    symbol, capacity, bucket = action
    if symbol == '+':
        return state[:bucket] + [min(state[bucket] + capacity, targets[bucket])] + state[bucket+1:]
    else: # symbol == '-'
        return state[:bucket] + [state[bucket] - min(state[bucket], capacity)] + state[bucket+1:]

# function to generate all possible next states from a given state
def next_states(state):
    for capacity in capacities:
        for bucket in range(len(state)):
            if state[bucket] > 0:
                yield ('-', capacity, bucket)
            if state[bucket] < targets[bucket]:
                yield ('+', capacity, bucket)

# use BFS to find the shortest sequence of actions from the initial state to the final state
queue = deque([([], initial_state)])
visited = set()
while queue:
    actions, state = queue.popleft()
    if state not in visited and state[2] >= targets[2]:
        visited.add(state)
        if state == targets:
            return actions
        for action in next_states(state):
            queue.append((actions + [action], apply_action(state, action)))

print("No solution found")
