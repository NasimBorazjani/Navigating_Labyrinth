
from collections import deque

# Define the capacities of the jugs and the target amounts in the buckets
jugs = [87, 13, 27, 106, 18, 91, 17, 138]
buckets = [205, 365, 391, 414]

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

    # Mark this state as visited
    visited.add(tuple(amounts))

    # If this state is the target state, return the actions that lead to it
    if amounts == buckets:
        print(actions)
        break

    # Try all possible actions from this state
    for i in range(len(jugs)):
        for j in range(len(buckets)):
            # If the jug can be poured into the bucket without overflowing it
            if amounts[j] + jugs[i] <= buckets[j] and (j == 0 or amounts[j] + jugs[i] <= amounts[j-1]):
                # Add the action and the resulting state to the queue
                queue.append((actions + [('+', i+1, j+1)], amounts[:j] + [amounts[j] + jugs[i]] + amounts[j+1:]))
            # If the bucket can be emptied
            if amounts[j] > 0:
                # Add the action and the resulting state to the queue
                queue.append((actions + [('-', i+1, j+1)], amounts[:j] + [0] + amounts[j+1:]))
