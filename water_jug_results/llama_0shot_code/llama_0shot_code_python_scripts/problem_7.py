
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
        for i, (capacity, _) in enumerate(jugs):
            for j, (amount, _) in enumerate(buckets):
                if amount + capacity <= amount:  # Check that we don't overflow the bucket
                    new_state = list(state)
                    new_state[j] += capacity
                    if tuple(new_state) not in parent:  # Avoid revisiting states
                        queue.append((new_state, ('+', capacity, j+1)))
                        parent[tuple(new_state)] = prev_action
                if amount - capacity >= 0:  # Check that we don't underflow the bucket
                    new_state = list(state)
                    new_state[j] -= capacity
                    if tuple(new_state) not in parent:  # Avoid revisiting states
                        queue.append((new_state, ('-', capacity, j+1)))
                        parent[tuple(new_state)] = prev_action

    # If we exit the loop without finding a solution, there is no solution
    return None

# Test the function with the problem's parameters
jugs = [(22, 'A'), (48, 'B'), (29, 'C'), (111, 'D'), (92, 'E'), (28, 'F')]
buckets = [(164, 1), (233, 2), (289, 3)]
print(bfs(jugs, [b[0] for b in buckets]))
