
from collections import deque

# Define the capacities of the jugs and the target amounts in the buckets
jugs = [141, 116, 66, 83, 142]
buckets = [397, 401, 419, 425]

# Define the initial state
initial_state = ([0]*len(buckets), [])

# Define a function that generates all possible actions from a given state
def generate_actions(state):
    actions = []
    for i in range(len(jugs)):
        for j in range(len(buckets)):
            if state[0][j] + jugs[i] <= buckets[j] and (j == 0 or state[0][j] + jugs[i] <= state[0][j-1]):
                new_state = state[0][:]
                new_state[j] += jugs[i]
                actions.append((new_state, state[1] + [('+', i+1, j+1)]))
            if state[0][j] - jugs[i] >= 0:
                new_state = state[0][:]
                new_state[j] -= jugs[i]
                actions.append((new_state, state[1] + [('-', i+1, j+1)]))
    return actions

# Perform a breadth-first search to find the shortest sequence of actions
queue = deque([initial_state])
visited = set([initial_state[0]])
while queue:
    state = queue.popleft()
    if state[0] == buckets:
        print(state[1])
        break
    for action in generate_actions(state):
        if action[0] not in visited:
            queue.append(action)
            visited.add(action[0])
