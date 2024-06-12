
from collections import deque

# Define the capacities of the jugs and the target amounts for the buckets
jugs = [128, 67, 44, 31, 127, 15]
buckets = [258, 261, 415, 430]

# Initialize the queue for the BFS with the initial state
queue = deque([([], [0]*4)])

# Keep track of the visited states to avoid loops
visited = set()

while queue:
    # Pop the next state from the queue
    actions, amounts = queue.popleft()

    # If this state is the target state, we have found a solution
    if amounts == buckets:
        print(actions)
        break

    # If we have already visited this state, skip it
    if tuple(amounts) in visited:
        continue

    # Mark this state as visited
    visited.add(tuple(amounts))

    # Try all possible actions from this state
    for i in range(len(jugs)):
        for j in range(len(amounts)):
            # Try adding water to the bucket
            if amounts[j] + jugs[i] <= buckets[j] and (j == 0 or amounts[j] + jugs[i] <= amounts[j-1]):
                new_amounts = amounts.copy()
                new_amounts[j] += jugs[i]
                new_actions = actions + [('+', i+1, j+1)]
                queue.append((new_actions, new_amounts))

            # Try removing water from the bucket
            if amounts[j] - jugs[i] >= 0 and (j == len(amounts)-1 or amounts[j] - jugs[i] >= amounts[j+1]):
                new_amounts = amounts.copy()
                new_amounts[j] -= jugs[i]
                new_actions = actions + [('-', i+1, j+1)]
                queue.append((new_actions, new_amounts))
