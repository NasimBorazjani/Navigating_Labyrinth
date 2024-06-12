
from collections import deque

# Define the capacities of the jugs and the target amounts in the buckets
jugs = [33, 87, 48, 30, 61, 60]
buckets = [170, 225, 238, 317]

# Initialize the queue for the BFS algorithm with the initial state
queue = deque([([], [0]*4)])

# Keep track of the visited states to avoid repeating the same work
visited = set()

while queue:
    # Pop the next state from the queue
    actions, amounts = queue.popleft()

    # If this state has been visited before, skip it
    if tuple(amounts) in visited:
        continue

    # Mark this state as visited
    visited.add(tuple(amounts))

    # If we have reached the target state, return the actions that led to it
    if amounts == buckets:
        print(actions)
        break

    # Try all possible actions
    for i, jug in enumerate(jugs):
        for j in range(4):
            # If the jug can be poured into the bucket without overflowing it
            if amounts[j] + jug <= buckets[j] and (j == 0 or amounts[j] + jug <= amounts[j-1]):
                # Create a new state by performing the action
                new_amounts = amounts[:]
                new_amounts[j] += jug
                new_actions = actions + [('+', i+1, j+1)]
                # Add the new state to the queue
                queue.append((new_actions, new_amounts))

            # If the bucket can be emptied
            if amounts[j] > 0:
                # Create a new state by performing the action
                new_amounts = amounts[:]
                new_amounts[j] = 0
                new_actions = actions + [('-', i+1, j+1)]
                # Add the new state to the queue
                queue.append((new_actions, new_amounts))
