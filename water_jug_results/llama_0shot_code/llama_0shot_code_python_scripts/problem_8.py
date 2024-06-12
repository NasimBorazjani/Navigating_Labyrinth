
from collections import deque

def bfs(jugs, buckets):
    # Initialize the queue and the parent list
    queue = deque([([0]*len(buckets), None)])
    parent = {tuple([0]*len(buckets)): None}

    while queue:
        state, prev_action = queue.popleft()
        if state == buckets:  # If this state is the final configuration
            # Backtrack to find the sequence of actions
            actions = []
            while prev_action is not None:
                actions.append(prev_action)
                state = tuple(parent[state])
            # Reverse the list of actions to get the correct order
            actions.reverse()
            return actions
        # Generate all possible next states
        for i, (capacity, _) in enumerate(jugs):
            for j, (amount, _) in enumerate(buckets):
                if amount + capacity <= amount:  # If adding water does not overflow
                    new_state = list(state)
                    new_state[j] += capacity
                    if tuple(new_state) not in parent:  # If this state has not been visited yet
                        queue.append((tuple(new_state), ('+', capacity, j+1)))
                        parent[tuple(new_state)] = state
                if state[j] >= capacity and state[j] - capacity >= 0:  # If removing water does not underflow
                    new_state = list(state)
                    new_state[j] -= capacity
                    if tuple(new_state) not in parent:  # If this state has not been visited yet
                        queue.append((tuple(new_state), ('-', capacity, j+1)))
                        parent[tuple(new_state)] = state
    return []  # If no solution is found

jugs = [(59, 'A'), (68, 'B'), (104, 'C'), (106, 'D'), (69, 'E'), (42, 'F')]
buckets = [(196, '1'), (210, '2'), (238, '3')]

actions = bfs(jugs, [x[0] for x in buckets])
print(actions)
