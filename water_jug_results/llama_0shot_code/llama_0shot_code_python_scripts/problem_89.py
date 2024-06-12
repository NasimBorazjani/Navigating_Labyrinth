
from collections import deque

def bfs(jugs, buckets):
    # Initialize the queue and the parent list
    queue = deque([([0]*len(buckets), None)])
    parent = {tuple([0]*len(buckets)): None}

    while queue:
        state, prev_action = queue.popleft()
        if state == buckets:  # If this state is the final configuration
            # Backtrack to find the shortest sequence of actions
            actions = []
            while prev_action is not None:
                actions.append(prev_action)
                state = tuple(parent[state])
            # Reverse the list of actions to get the correct order
            actions.reverse()
            return actions
        # Generate all possible next states
        for i, (capacity, _) in enumerate(jugs):
            for j, bucket in enumerate(state):
                if bucket + capacity <= buckets[j]:  # If we can add water without exceeding
                    next_state = list(state)
                    next_state[j] += capacity
                    if tuple(next_state) not in parent:  # If we have not visited this state before
                        queue.append((tuple(next_state), ('+', capacity, j+1)))
                        parent[tuple(next_state)] = state
                if state[j] >= capacity:  # If we can remove water without going below 0
                    next_state = list(state)
                    next_state[j] -= capacity
                    if tuple(next_state) not in parent:  # If we have not visited this state before
                        queue.append((tuple(next_state), ('-', capacity, j+1)))
                        parent[tuple(next_state)] = state

    return None  # If no solution is found

jugs = [(30, 'A'), (26, 'B'), (116, 'C'), (76, 'D'), (98, 'E'), (48, 'F'), (46, 'G'), (45, 'H')]
buckets = [201, 269, 315, 333]

actions = bfs(jugs, buckets)
print(actions)
