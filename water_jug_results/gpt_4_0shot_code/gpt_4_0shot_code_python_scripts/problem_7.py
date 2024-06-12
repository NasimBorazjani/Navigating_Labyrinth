
from collections import deque

# Define the capacities of the jugs and the target amounts in the buckets
jugs = [22, 48, 29, 111, 92, 28]
targets = [164, 233, 289]

# Initialize the BFS queue with the initial state
queue = deque([([], [0, 0, 0])])

# Keep track of the visited states to avoid loops
visited = set()

while queue:
    # Pop the next state from the queue
    actions, amounts = queue.popleft()

    # If this state has been visited before, skip it
    if tuple(amounts) in visited:
        continue
    visited.add(tuple(amounts))

    # If this state is the target, return the actions that led to it
    if amounts == targets:
        print(actions)
        break

    # Try all possible actions
    for i, jug in enumerate(jugs):
        for j in range(3):
            # If the jug can be poured into the bucket without overfilling it
            if amounts[j] + jug <= targets[j]:
                # If the bucket is not the first one, or it is the first one and it is empty
                if j == 0 or amounts[j-1] <= amounts[j] + jug:
                    # Add the action and the resulting state to the queue
                    new_actions = actions + [('+', i+1, j+1)]
                    new_amounts = amounts.copy()
                    new_amounts[j] += jug
                    queue.append((new_actions, new_amounts))
            # If the bucket can be emptied
            if amounts[j] > 0:
                # If the bucket is not the last one, or it is the last one and it is full
                if j == 2 or amounts[j+1] >= amounts[j]:
                    # Add the action and the resulting state to the queue
                    new_actions = actions + [('-', i+1, j+1)]
                    new_amounts = amounts.copy()
                    new_amounts[j] -= jug
                    queue.append((new_actions, new_amounts))
