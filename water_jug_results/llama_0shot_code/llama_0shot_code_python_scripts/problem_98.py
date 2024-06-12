
from collections import deque

def bfs(jugs, buckets):
    # Define the initial state and the final state
    initial_state = [0] * len(buckets)
    final_state = buckets

    # Define the possible actions
    actions = [('+', i, j) for i in jugs for j in range(len(buckets))]
    actions += [('-', i, j) for i in jugs for j in range(len(buckets))]

    # Initialize the queue with the initial state
    queue = deque([(initial_state, 0)])

    # Initialize the dictionary to store the states and the numbers of steps
    steps = {tuple(initial_state): 0}

    while queue:
        state, step = queue.popleft()

        # If this state is the final state, we have found a solution
        if state == final_state:
            # Retrieve the sequence of actions that led to this state
            actions = []
            while step:
                for action in actions_taken[step]:
                    if action not in actions:
                        actions.append(action)
                step -= 1
            return actions[::-1]

        # Otherwise, generate all possible next states
        for action in actions:
            new_state = list(state)
            jug_capacity, operation, bucket_id = action

            if operation == '+':
                # Add water to the bucket
                new_state[bucket_id] += jug_capacity
                if new_state[bucket_id] > buckets[bucket_id]:
                    new_state[bucket_id] = buckets[bucket_id]
            else:
                # Remove water from the bucket
                new_state[bucket_id] -= jug_capacity
                if new_state[bucket_id] < 0:
                    new_state[bucket_id] = 0

            new_state = tuple(new_state)

            # If we have not seen this state before, enqueue it
            if new_state not in steps:
                steps[new_state] = step + 1
                queue.append((new_state, step + 1))

    # If there is no solution, return an empty list
    return []

jugs = [137, 100, 82, 25, 21, 101, 118, 117, 26, 131]
buckets = [272, 439, 458, 590]
actions_taken = {}

solution = bfs(jugs, buckets)
print(solution)
