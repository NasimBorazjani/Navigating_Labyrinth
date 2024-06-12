
from collections import deque

# capacities of the jugs
jug_capacities = [118, 15, 88, 145, 84, 14, 107, 31]

# target amounts of water in the buckets
bucket_targets = [226, 258, 296]

# initial state: all buckets are empty
initial_state = (0, 0, 0)

# queue for BFS, each item is a tuple (state, actions, depth)
queue = deque([(initial_state, [], 0)])

# dictionary to store the actions that led to each state
actions_to_state = {initial_state: []}

# perform BFS
while queue:
    state, actions, depth = queue.popleft()

    # check if the final state is reached
    if state == tuple(bucket_targets):
        print("Solution found:", actions)
        break

    # generate all possible next states and actions
    for i, (capacity, target) in enumerate(zip(jug_capacities, bucket_targets)):
        for j in range(3):
            # fill the bucket with the jug
            if state[j] + capacity <= target:
                next_state = list(state)
                next_state[j] += capacity
                next_actions = actions + [('+', capacity, j + 1)]
                if next_state not in actions_to_state:
                    queue.append((tuple(next_state), next_actions, depth + 1))
                    actions_to_state[tuple(next_state)] = next_actions

            # empty the bucket into the jug
            if state[j] >= capacity:
                next_state = list(state)
                next_state[j] -= capacity
                next_actions = actions + [('-', capacity, j + 1)]
                if next_state not in actions_to_state:
                    queue.append((tuple(next_state), next_actions, depth + 1))
                    actions_to_state[tuple(next_state)] = next_actions

print("Number of actions:", len(actions_to_state[tuple(bucket_targets)]))
