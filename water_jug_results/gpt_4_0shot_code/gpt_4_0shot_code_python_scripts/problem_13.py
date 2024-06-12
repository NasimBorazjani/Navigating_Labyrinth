
from collections import deque

# Define the capacities of the jugs and the target amounts in the buckets
jugs = [57, 84, 47, 76, 85, 69]
targets = [203, 217, 334]

# Define the initial state (empty buckets) and the final state
initial_state = (0, 0, 0)
final_state = tuple(targets)

# Create a dictionary to store the shortest sequence of actions that leads to each state
actions = {initial_state: []}

# Create a queue for the BFS algorithm and add the initial state
queue = deque([initial_state])

while queue:
    # Pop the next state from the queue
    state = queue.popleft()

    # If this is the final state, we are done
    if state == final_state:
        break

    # Try all possible actions from this state
    for i, jug in enumerate(jugs):
        for j in range(3):
            # Try to add water to bucket j
            if state[j] + jug <= targets[j] and all(state[j] + jug <= state[k] for k in range(j+1, 3)):
                new_state = state[:j] + (state[j] + jug,) + state[j+1:]
                if new_state not in actions:
                    actions[new_state] = actions[state] + [('+', jug, j+1)]
                    queue.append(new_state)

            # Try to remove water from bucket j
            if state[j] - jug >= 0 and all(state[j] - jug >= state[k] for k in range(j)):
                new_state = state[:j] + (state[j] - jug,) + state[j+1:]
                if new_state not in actions:
                    actions[new_state] = actions[state] + [('-', jug, j+1)]
                    queue.append(new_state)

# Print the shortest sequence of actions that leads to the final state
print(actions[final_state])
