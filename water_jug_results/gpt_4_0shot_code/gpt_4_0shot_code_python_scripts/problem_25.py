
from collections import deque

# Define the capacities of the jugs and the target amounts of water in the buckets
jugs = [75, 20, 64, 106, 88, 13, 107, 131]
targets = [287, 394, 455]

# Initialize the BFS queue with the initial state and an empty sequence of actions
queue = deque([((0, 0, 0), [])])

# Keep track of the visited states to avoid loops
visited = set()

while queue:
    # Pop the next state and sequence of actions from the queue
    state, actions = queue.popleft()

    # If this state is the target, we have found a solution
    if state == tuple(targets):
        print(actions)
        break

    # If we have already visited this state, skip it
    if state in visited:
        continue

    # Mark this state as visited
    visited.add(state)

    # Try all possible actions
    for i, jug in enumerate(jugs):
        for j in range(3):
            # If the jug can be poured into the bucket without overflowing it
            if state[j] + jug <= targets[j] and (j == 2 or state[j] + jug <= state[j + 1]):
                # Add the new state and sequence of actions to the queue
                new_state = list(state)
                new_state[j] += jug
                queue.append((tuple(new_state), actions + [('+', i + 1, j + 1)]))

            # If the bucket can be emptied
            if state[j] > 0:
                # Add the new state and sequence of actions to the queue
                new_state = list(state)
                new_state[j] = 0
                queue.append((tuple(new_state), actions + [('-', i + 1, j + 1)]))
