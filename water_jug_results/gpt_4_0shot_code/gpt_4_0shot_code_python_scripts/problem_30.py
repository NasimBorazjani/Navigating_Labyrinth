
from collections import deque

# Define the capacities of the jugs and the target amounts for the buckets
jugs = [111, 84, 17, 22, 63, 75, 148, 64]
targets = [253, 280, 448]

# Initialize the BFS queue with the initial state
queue = deque([([], [0, 0, 0])])

# Keep track of the visited states to avoid loops
visited = set()

while queue:
    # Dequeue the next state
    actions, amounts = queue.popleft()

    # If this state has been visited before, skip it
    if tuple(amounts) in visited:
        continue

    # Mark this state as visited
    visited.add(tuple(amounts))

    # If this state is the target state, return the actions that led to it
    if amounts == targets:
        print(actions)
        break

    # Try all possible actions
    for i, jug in enumerate(jugs):
        for j in range(3):
            # If the jug can be poured into the bucket without overflowing it
            if amounts[j] + jug <= targets[j] and (j == 2 or amounts[j] + jug <= amounts[j + 1]):
                # Enqueue the resulting state and the corresponding action
                queue.append((actions + [('+', i + 1, j + 1)], amounts[:j] + [amounts[j] + jug] + amounts[j + 1:]))
            # If the bucket can be emptied
            if amounts[j] > 0:
                # Enqueue the resulting state and the corresponding action
                queue.append((actions + [('-', i + 1, j + 1)], amounts[:j] + [0] + amounts[j + 1:]))
