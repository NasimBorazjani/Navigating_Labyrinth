
from collections import deque

def bfs(jugs, buckets):
    # Initialize the queue and the parent list
    queue = deque([([0]*len(buckets), None)])
    parent = {tuple([0]*len(buckets)): None}

    while queue:
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
                if amount + capacity <= amount:  # Check if the bucket can hold the additional water
                    new_state = list(state)
                    new_state[j] += capacity
                    if tuple(new_state) not in parent:  # If we have not visited this state before
                        queue.append((new_state, ('+', capacity, j+1)))
                        parent[tuple(new_state)] = prev_action
                if state[j] >= capacity and new_state[j] - capacity >= 0:  # Check if the bucket has enough water
                    new_state = list(state)
                    new_state[j] -= capacity
                    if tuple(new_state) not in parent:  # If we have not visited this state before
                        queue.append((new_state, ('-', capacity, j+1)))
                        parent[tuple(new_state)] = prev_action

    return None  # If no solution is found

# Test the function with the given problem
jugs = [(62, 'A'), (144, 'B'), (80, 'C'), (72, 'D'), (100, 'E'), (127, 'F'), (18, 'G'), (82, 'H'), (42, 'I'), (99, 'J')]
buckets = [258, 310, 514]
print(bfs(jugs, buckets))
