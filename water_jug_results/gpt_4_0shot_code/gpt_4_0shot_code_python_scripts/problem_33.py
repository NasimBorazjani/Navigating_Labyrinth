
from collections import deque

# Define the capacities of the jugs and the target amounts of water in the buckets
jugs = [146, 57, 69, 52, 132, 80, 145]
buckets = [456, 538, 549]

# Initialize the BFS queue with the initial state and an empty sequence of actions
queue = deque([((0, 0, 0), [])])

# Keep track of the visited states to avoid loops
visited = set()

while queue:
    # Pop the next state and sequence of actions from the queue
    state, actions = queue.popleft()

    # If this state has been visited before, skip it
    if state in visited:
        continue

    # Mark this state as visited
    visited.add(state)

    # If this state is the target state, return the sequence of actions
    if state == tuple(buckets):
        print(actions)
        break

    # Try all possible actions from this state
    for i, jug in enumerate(jugs):
        for j in range(3):
            # If the jug can be poured into the bucket without overfilling it
            if state[j] + jug <= buckets[j] and (j == 2 or state[j] + jug <= state[j + 1]):
                # Add the new state and the updated sequence of actions to the queue
                new_state = list(state)
                new_state[j] += jug
                queue.append((tuple(new_state), actions + [('+', i + 1, j + 1)]))

            # If the bucket can be emptied
            if state[j] > 0:
                # Add the new state and the updated sequence of actions to the queue
                new_state = list(state)
                new_state[j] = 0
                queue.append((tuple(new_state), actions + [('-', i + 1, j + 1)]))
