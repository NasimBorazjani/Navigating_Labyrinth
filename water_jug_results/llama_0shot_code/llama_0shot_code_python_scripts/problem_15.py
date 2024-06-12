
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
            actions = []
            while prev_action is not None:
                actions.append(prev_action)
                prev_action = parent[tuple(state)]
            return actions[::-1]  # Reverse the list to get the correct order of actions

        # Generate all possible next states
        for i, (x, y) in enumerate(jugs):
            for j in range(len(buckets)):
                if state[j] + x <= buckets[j] and state[j] + x >= 0:
                    new_state = list(state)
                    new_state[j] += x
                    action = ('+', x, j+1)
                    if tuple(new_state) not in parent:
                        queue.append((new_state, action))
                        parent[tuple(new_state)] = prev_action
                if state[j] - x >= 0:
                    new_state = list(state)
                    new_state[j] -= x
                    action = ('-', x, j+1)
                    if tuple(new_state) not in parent:
                        queue.append((new_state, action))
                        parent[tuple(new_state)] = prev_action

    # If no solution is found, return an empty list
    return []

jugs = [(19, 1), (50, 2), (12, 3), (63, 4), (143, 5), (13, 6)]
buckets = [160, 170, 330]

actions = bfs(jugs, buckets)
print(actions)
