
from collections import deque

# Define the capacities of the jugs and the target amounts in the buckets
jugs = [57, 98, 149, 99, 105, 28]
targets = [281, 401, 423, 427]

# Initialize the BFS queue with the initial state
queue = deque([([], [0]*4)])

# Keep track of the visited states to avoid loops
visited = set()

while queue:
    # Pop the next state from the queue
    actions, amounts = queue.popleft()

    # If this state is the target state, we have found a solution
    if amounts == targets:
        print(actions)
        break

    # If we have already visited this state, skip it
    if tuple(amounts) in visited:
        continue

    # Mark this state as visited
    visited.add(tuple(amounts))

    # Try all possible actions from this state
    for i, jug in enumerate(jugs):
        for j in range(4):
            # Try filling bucket j with jug i
            if amounts[j] + jug <= targets[j] and (j == 0 or amounts[j] + jug <= amounts[j-1]):
                new_amounts = amounts[:]
                new_amounts[j] += jug
                new_actions = actions + [('+', i+1, j+1)]
                queue.append((new_actions, new_amounts))

            # Try emptying bucket j
            if amounts[j] > 0:
                new_amounts = amounts[:]
                new_amounts[j] = 0
                new_actions = actions + [('-', i+1, j+1)]
                queue.append((new_actions, new_amounts))
