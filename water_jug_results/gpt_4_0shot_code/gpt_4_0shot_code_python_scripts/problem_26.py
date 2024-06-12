
from collections import deque

# Define the capacities of the jugs and the target amounts of water in the buckets
jugs = [24, 132, 149, 62, 120, 61, 42]
buckets = [298, 430, 468]

# Initialize the queue for the BFS algorithm with the initial state
queue = deque([([], [0, 0, 0])])

# Keep track of the shortest sequence of actions that leads to each state
visited = {tuple([0, 0, 0]): []}

while queue:
    # Dequeue the next state and its corresponding sequence of actions
    actions, amounts = queue.popleft()

    # If this state is the target state, return the sequence of actions
    if amounts == buckets:
        print(actions)
        break

    # Try all possible actions
    for i, jug in enumerate(jugs):
        for j in range(3):
            # If the jug can be poured into the bucket without overfilling it
            if amounts[j] + jug <= buckets[j]:
                # If the resulting state has not been visited yet, or if the new sequence of actions is shorter
                new_amounts = amounts[:]
                new_amounts[j] += jug
                if tuple(new_amounts) not in visited or len(actions) + 1 < len(visited[tuple(new_amounts)]):
                    # Enqueue the new state and its corresponding sequence of actions
                    new_actions = actions + [('+', i+1, j+1)]
                    queue.append((new_actions, new_amounts))
                    visited[tuple(new_amounts)] = new_actions

            # If the jug can be emptied from the bucket without violating the constraints
            if amounts[j] - jug >= 0 and (j == 2 or amounts[j] - jug >= amounts[j+1]):
                # If the resulting state has not been visited yet, or if the new sequence of actions is shorter
                new_amounts = amounts[:]
                new_amounts[j] -= jug
                if tuple(new_amounts) not in visited or len(actions) + 1 < len(visited[tuple(new_amounts)]):
                    # Enqueue the new state and its corresponding sequence of actions
                    new_actions = actions + [('-', i+1, j+1)]
                    queue.append((new_actions, new_amounts))
                    visited[tuple(new_amounts)] = new_actions
