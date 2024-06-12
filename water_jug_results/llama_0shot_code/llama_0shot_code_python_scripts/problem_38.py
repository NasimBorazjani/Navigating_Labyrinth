
from collections import deque

def bfs(jugs, buckets):
    # Initialize the queue and the parent list
    queue = deque([([0]*len(buckets), None)])
    parent = {tuple([0]*len(buckets)): None}

    while queue:
        # Dequeue a state
        state, prev_action = queue.popleft()

        # If this state is the final configuration, we have found a solution
        if state == buckets:
            return prev_action

        # Generate all possible next states
        for i, (capacity, _) in enumerate(jugs):
            for j, (target, _) in enumerate(buckets):
                # Check if we can add water to bucket j
                if state[j] + capacity <= target and state[j] + capacity <= buckets[j+1][1]:
                    next_state = list(state)
                    next_state[j] += capacity
                    if tuple(next_state) not in parent:
                        queue.append((next_state, (('+', capacity, j), prev_action)))
                        parent[tuple(next_state)] = (('+', capacity, j), prev_action)

                # Check if we can remove water from bucket j
                if state[j] - capacity >= 0:
                    next_state = list(state)
                    next_state[j] -= capacity
                    if tuple(next_state) not in parent:
                        queue.append((next_state, (('-', capacity, j), prev_action)))
                        parent[tuple(next_state)] = (('-', capacity, j), prev_action)

    # If no solution is found, return an empty list
    return []

# Test the function with the provided problem
jugs = [(117, 'A'), (128, 'B'), (36, 'C'), (129, 'D'), (103, 'E'), (53, 'F'), (21, 'G'), (119, 'H'), (105, 'I'), (26, 'J')]
buckets = [(394, 1), (425, 2), (426, 3)]

solution = bfs(jugs, buckets)
print(solution)
