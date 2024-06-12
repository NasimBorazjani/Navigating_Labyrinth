
from collections import deque

def bfs(capacities, targets):
    # Initialize the queue with the initial state
    queue = deque([({}, [])])
    while queue:
        state, actions = queue.popleft()
        # Check if the state is a goal state
        if all(state.get(i, 0) == targets[i-1] for i in range(1, len(targets) + 1)):
            return actions
        # Generate all possible next states
        for i in range(len(targets) + 1):
            for cap in capacities:
                if state.get(i, 0) + cap <= targets[i-1]:
                    # Add water to the bucket
                    new_state = state.copy()
                    new_state[i] = state.get(i, 0) + cap
                    queue.append((new_state, actions + [('+', cap, i)]))
                elif state.get(i, 0) >= cap:
                    # Remove water from the bucket
                    new_state = state.copy()
                    new_state[i] = state.get(i, 0) - cap
                    queue.append((new_state, actions + [('-', cap, i)]))

# Test the function
capacities = [59, 104, 79, 23, 20, 60, 14, 15, 119, 105]
targets = [215, 403, 420, 504]
print(bfs(capacities, targets))
