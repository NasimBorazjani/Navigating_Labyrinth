
from collections import deque

# Define the capacities of the jugs and the target amounts in the buckets
jugs = [30, 26, 116, 76, 98, 48, 46, 45]
buckets = [201, 269, 315, 333]

# Initialize the BFS queue with the initial state
queue = deque([([], [0]*4)])

# Keep track of the visited states to avoid loops
visited = set()

while queue:
    # Pop the next state from the queue
    actions, amounts = queue.popleft()

    # If this state has been visited before, skip it
    if tuple(amounts) in visited:
        continue
    visited.add(tuple(amounts))

    # If the target state has been reached, return the actions that led to it
    if amounts == buckets:
        print(actions)
        break

    # Try all possible actions from the current state
    for i, jug in enumerate(jugs):
        for j in range(4):
            # If the jug can be poured into the bucket without overflowing it
            if amounts[j] + jug <= buckets[j] and (j == 0 or amounts[j] + jug <= amounts[j-1]):
                # Add the action and the resulting state to the queue
                new_amounts = amounts.copy()
                new_amounts[j] += jug
                queue.append((actions + [('+', jug, j+1)], new_amounts))
            # If the bucket can be emptied
            if amounts[j] > 0:
                # Add the action and the resulting state to the queue
                new_amounts = amounts.copy()
                new_amounts[j] = 0
                queue.append((actions + [('-', jug, j+1)], new_amounts))
