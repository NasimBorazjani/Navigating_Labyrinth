
from collections import deque

# Define the capacities of the jugs and the target amounts in the buckets
jugs = [14, 42, 113, 131, 41, 147]
buckets = [240, 257, 350, 369]

# Initialize the queue for the BFS algorithm with the initial state
queue = deque([([], [0]*4)])

# Keep track of the visited states to avoid loops
visited = set()

while queue:
    # Dequeue the next state
    actions, amounts = queue.popleft()

    # If this state is the target state, return the actions that lead to it
    if amounts == buckets:
        print(actions)
        break

    # If this state has been visited before, skip it
    if tuple(amounts) in visited:
        continue

    # Mark this state as visited
    visited.add(tuple(amounts))

    # Try all possible actions from this state
    for i in range(4):
        for j in range(6):
            # Try adding water to the bucket
            if amounts[i] + jugs[j] <= (amounts[i+1] if i < 3 else float('inf')):
                new_amounts = amounts[:]
                new_amounts[i] += jugs[j]
                new_actions = actions + [('+', j+1, i+1)]
                queue.append((new_actions, new_amounts))

            # Try removing water from the bucket
            if amounts[i] - jugs[j] >= 0:
                new_amounts = amounts[:]
                new_amounts[i] -= jugs[j]
                new_actions = actions + [('-', j+1, i+1)]
                queue.append((new_actions, new_amounts))
